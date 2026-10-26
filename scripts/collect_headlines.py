#!/usr/bin/env python3
"""각국 방송사·신문사 RSS 헤드라인 수집기 (표준 라이브러리만 사용).

사용 예:
    python3 scripts/collect_headlines.py --country us --date 2026-10-26
    python3 scripts/collect_headlines.py --country all

결과: data/<date>/raw/<country>.json
실패한 매체는 ok=false 와 error 를 남긴다. 팀원 에이전트는 이를 보고
homepage 를 WebFetch/WebSearch 로 대체 수집한다.
"""
import argparse
import datetime as dt
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "config" / "sources.json"
UA = "Mozilla/5.0 (News-Daily headline collector)"
KST = dt.timezone(dt.timedelta(hours=9))


def local(tag):
    return tag.rsplit("}", 1)[-1]


def child_text(el, name):
    for c in el:
        if local(c.tag) == name:
            if name == "link" and c.get("href"):
                return c.get("href")
            return (c.text or "").strip()
    return ""


def clean(text, limit=None):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit] if limit else text


def parse_date(raw):
    if not raw:
        return None
    try:
        d = email.utils.parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d


def parse_feed(data):
    root = ET.fromstring(data)
    items = [el for el in root.iter() if local(el.tag) in ("item", "entry")]
    out = []
    for el in items:
        published = parse_date(
            child_text(el, "pubDate") or child_text(el, "published")
            or child_text(el, "updated") or child_text(el, "date")
        )
        out.append({
            "title": clean(child_text(el, "title")),
            "link": child_text(el, "link"),
            "published": published.isoformat() if published else None,
            "summary": clean(child_text(el, "description") or child_text(el, "summary"), 300),
        })
    return [i for i in out if i["title"]]


def fetch(source, limit, since):
    result = {k: source.get(k) for k in ("name", "type", "url", "homepage", "note") if source.get(k)}
    try:
        req = urllib.request.Request(source["url"], headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as resp:
            items = parse_feed(resp.read())
        if since:
            items = [i for i in items if not i["published"] or dt.datetime.fromisoformat(i["published"]) >= since]
        result.update(ok=True, items=items[:limit])
    except Exception as e:  # noqa: BLE001 - 매체별 실패는 기록만 하고 계속 진행
        result.update(ok=False, error=f"{type(e).__name__}: {e}", items=[])
    return result


def collect(code, cfg, date, limit, hours):
    now = dt.datetime.now(dt.timezone.utc)
    since = now - dt.timedelta(hours=hours) if hours else None
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda s: fetch(s, limit, since), cfg["sources"]))
    payload = {
        "country": code,
        "country_name": cfg["name"],
        "date": date,
        "collected_at": now.astimezone(KST).isoformat(),
        "sources": results,
    }
    out = ROOT / "data" / date / "raw" / f"{code}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(r["ok"] for r in results)
    n = sum(len(r["items"]) for r in results)
    print(f"[{code}] {ok}/{len(results)} 매체 성공, 헤드라인 {n}건 -> {out.relative_to(ROOT)}")
    for r in results:
        if not r["ok"]:
            print(f"  - 실패: {r['name']} ({r['error'][:100]})")


def main():
    config = json.loads(SOURCES.read_text(encoding="utf-8"))
    countries = [k for k in config if not k.startswith("_")]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--country", required=True, help=f"{', '.join(countries)} 또는 all")
    p.add_argument("--date", default=dt.datetime.now(KST).strftime("%Y-%m-%d"), help="YYYY-MM-DD (기본: 오늘, KST)")
    p.add_argument("--limit", type=int, default=15, help="매체당 최대 헤드라인 수")
    p.add_argument("--hours", type=int, default=36, help="최근 N시간 이내 기사만 (0=제한 없음)")
    args = p.parse_args()

    targets = countries if args.country == "all" else [args.country]
    for code in targets:
        if code not in config:
            sys.exit(f"알 수 없는 국가 코드: {code} (가능: {', '.join(countries)})")
        collect(code, config[code], args.date, args.limit, args.hours)


if __name__ == "__main__":
    main()
