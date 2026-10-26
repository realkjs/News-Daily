#!/usr/bin/env python3
"""briefings/YYYY-MM-DD.json 검증 — 출처가 실제 원자료에 있는지, 피쉬본 구조가 맞는지 확인한다.

사용: python template/verify.py 2026-10-27
문제가 있으면 목록을 출력하고 종료 코드 1. 임원 최종본 작성 후, 렌더링·게시 전에 실행한다.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = {"industry", "business", "stocks", "crypto", "monetary", "legislation", "forecast", "geopolitics"}
COUNTRIES = {"us", "kr", "jp", "de", "uk", "fr", "il", "ru", "cn"}


def raw_urls(date):
    urls = set()
    for sub in ("raw", "work"):
        d = os.path.join(ROOT, "data", sub, date)
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if name.endswith(".json") and not name.startswith("_"):
                doc = json.load(open(os.path.join(d, name), encoding="utf-8"))
                urls.update(h.get("url") for h in doc.get("headlines", []) if h.get("url"))
    return urls


def check(date):
    data = json.load(open(os.path.join(ROOT, "briefings", f"{date}.json"), encoding="utf-8"))
    known = raw_urls(date)
    problems = []
    if not known:
        problems.append(f"data/raw/{date}, data/work/{date} 에 헤드라인이 없음")

    picks = [("top10", i, p) for i, p in enumerate(data.get("top10", []))]
    for cc, items in data.get("by_country", {}).items():
        if cc not in COUNTRIES:
            problems.append(f"by_country: 알 수 없는 국가 코드 {cc}")
        picks += [(f"by_country.{cc}", i, p) for i, p in enumerate(items)]
    for where, i, p in picks:
        label = f"{where}[{i}] {p.get('headline_ko', '')[:30]}"
        sources = p.get("sources") or []
        if not sources:
            problems.append(f"{label}: 출처 없음")
        for s in sources:
            if s.get("url") not in known:
                problems.append(f"{label}: 원자료에 없는 URL {s.get('name')} {s.get('url')}")
        for f in p.get("fields", []):
            if f not in FIELDS:
                problems.append(f"{label}: 알 수 없는 분야 {f}")

    fb = data.get("fishbone", {})
    ids = set()
    for bone in fb.get("bones", []):
        if bone.get("field") not in FIELDS:
            problems.append(f"fishbone: 알 수 없는 분야 {bone.get('field')}")
        for item in bone.get("items", []):
            if item.get("id") in ids:
                problems.append(f"fishbone: 중복 id {item.get('id')}")
            ids.add(item.get("id"))
            if item.get("country") not in COUNTRIES:
                problems.append(f"fishbone {item.get('id')}: 알 수 없는 국가 {item.get('country')}")
    for link in fb.get("links", []):
        for end in ("from", "to"):
            if link.get(end) not in ids:
                problems.append(f"fishbone link: 없는 잔뼈 id {link.get(end)}")
        if not link.get("logic"):
            problems.append(f"fishbone link {link.get('from')}→{link.get('to')}: 연결 논리 없음")

    missing = FIELDS - {f.get("id") for f in data.get("fields", [])}
    if missing:
        problems.append(f"fields: 해설 없는 분야 {sorted(missing)}")
    if not data.get("hypothesis_check", {}).get("against"):
        problems.append("hypothesis_check: 반박 증거(against)가 비어 있음 — 없으면 '오늘 반박 증거 없음'을 명시")
    return problems, len(picks)


def main():
    date = sys.argv[1]
    problems, n = check(date)
    if problems:
        print(f"검증 실패 {len(problems)}건:")
        for p in problems:
            print(f"- {p}")
        sys.exit(1)
    print(f"검증 통과: 선별 뉴스 {n}건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상")


if __name__ == "__main__":
    main()
