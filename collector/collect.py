#!/usr/bin/env python3
"""News-Daily 헤드라인 수집기 (GitHub Actions에서 실행).

config/sources.json의 방송사별 RSS를 읽고, RSS가 없거나 최근 기사가 부족하면
Google News의 site: 검색 RSS로 대체한다. 결과는 data/raw/YYYY-MM-DD/<team>.json.
표준 라이브러리만 사용한다.
"""
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from urllib.parse import quote_plus

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KST = timezone(timedelta(hours=9))
UA = "Mozilla/5.0 (News-Daily headline collector; +https://github.com/realkjs/news-daily)"
WINDOW_HOURS = 36
PER_SOURCE = 8
MIN_DIRECT = 3


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", unescape(s or ""))
    return re.sub(r"\s+", " ", s).strip()


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = parsedate_to_datetime(s)
    except (TypeError, ValueError):
        d = None
    if d is None:
        try:
            d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d


def local(tag):
    return tag.rsplit("}", 1)[-1].lower()


def parse_feed(raw):
    """RSS 2.0 / RDF / Atom 공통 파서 → [{title, link, published, summary}]"""
    root = ET.fromstring(raw)
    items = []
    for el in root.iter():
        name = local(el.tag)
        if name not in ("item", "entry"):
            continue
        rec = {"title": "", "link": "", "published": None, "summary": ""}
        for ch in el:
            n = local(ch.tag)
            if n == "title":
                rec["title"] = strip_tags(ch.text)
            elif n == "link":
                rec["link"] = (ch.get("href") or ch.text or "").strip() or rec["link"]
            elif n in ("pubdate", "published", "updated", "date") and not rec["published"]:
                rec["published"] = parse_date(ch.text)
            elif n in ("description", "summary") and not rec["summary"]:
                rec["summary"] = strip_tags(ch.text)[:400]
        if rec["title"]:
            items.append(rec)
    return items


def google_news_url(domain, gn):
    q = quote_plus(f"site:{domain} when:1d")
    return f"https://news.google.com/rss/search?q={q}&hl={gn['hl']}&gl={gn['gl']}&ceid={gn['ceid']}"


def recent(items, now):
    cutoff = now - timedelta(hours=WINDOW_HOURS)
    out = [i for i in items if i["published"] is None or i["published"] >= cutoff]
    out.sort(key=lambda i: i["published"] or now, reverse=True)
    return out


def collect_source(src, gn, now):
    log = []
    items, method = [], None
    if src.get("rss"):
        try:
            items = recent(parse_feed(fetch(src["rss"])), now)
            method = "rss"
        except Exception as e:  # noqa: BLE001
            log.append(f"rss 실패: {type(e).__name__}: {e}")
    if len(items) < MIN_DIRECT:
        try:
            g = recent(parse_feed(fetch(google_news_url(src["domain"], gn))), now)
            # Google News 제목 끝의 " - 매체명" 제거
            for i in g:
                i["title"] = re.sub(r"\s+-\s+[^-]{1,60}$", "", i["title"])
            if len(g) > len(items):
                items, method = g, "google_news"
        except Exception as e:  # noqa: BLE001
            log.append(f"google_news 실패: {type(e).__name__}: {e}")
    out = []
    for i in items[:PER_SOURCE]:
        out.append({
            "source": src["name"],
            "title_original": i["title"],
            "summary_original": i["summary"],
            "url": i["link"],
            "published": i["published"].astimezone(KST).isoformat() if i["published"] else None,
            "via": method,
            "state_media": bool(src.get("state_media")),
        })
    return out, log


def main():
    now = datetime.now(timezone.utc)
    date = sys.argv[1] if len(sys.argv) > 1 else now.astimezone(KST).strftime("%Y-%m-%d")
    cfg = json.load(open(os.path.join(ROOT, "config", "sources.json"), encoding="utf-8"))
    outdir = os.path.join(ROOT, "data", "raw", date)
    os.makedirs(outdir, exist_ok=True)
    summary = {}
    for tid, team in cfg["teams"].items():
        heads, unavailable, logs = [], [], {}
        for src in team["sources"]:
            got, log = collect_source(src, team["google_news"], now)
            heads += got
            if not got:
                unavailable.append(src["name"])
            if log:
                logs[src["name"]] = log
        doc = {
            "team": tid,
            "team_name_ko": team["name_ko"],
            "collected_at": now.astimezone(KST).isoformat(),
            "headlines": heads,
            "unavailable_sources": unavailable,
            "errors": logs,
        }
        with open(os.path.join(outdir, f"{tid}.json"), "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        summary[tid] = {"headlines": len(heads), "unavailable": unavailable}
        print(f"[{tid}] {len(heads)}건, 실패: {', '.join(unavailable) or '없음'}")
    with open(os.path.join(outdir, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    total = sum(v["headlines"] for v in summary.values())
    print(f"총 {total}건 → {outdir}")
    if total == 0:
        sys.exit("수집 0건 — 네트워크 또는 피드 점검 필요")


if __name__ == "__main__":
    main()
