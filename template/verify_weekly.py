#!/usr/bin/env python3
"""briefings/weekly/YYYY-Www.json 검증 — 출처가 그 주 원자료에 있는지, 날짜·구조가 맞는지 확인한다.

사용: python template/verify_weekly.py 2026-W44
문제가 있으면 목록을 출력하고 종료 코드 1. 렌더링·게시 전에 실행한다.
"""
import json
import os
import sys
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = {"industry", "business", "stocks", "crypto", "monetary", "legislation", "forecast", "geopolitics"}
COUNTRIES = {"us", "kr", "jp", "de", "uk", "fr", "il", "ru", "cn"}
OUTCOMES = {"적중", "빗나감", "진행중", "확인불가"}


def raw_urls(days):
    urls = set()
    for d in days:
        for sub in ("raw", "work"):
            folder = os.path.join(ROOT, "data", sub, d)
            if not os.path.isdir(folder):
                continue
            for name in os.listdir(folder):
                if name.endswith(".json") and not name.startswith("_"):
                    doc = json.load(open(os.path.join(folder, name), encoding="utf-8"))
                    urls.update(h.get("url") for h in doc.get("headlines", []) if h.get("url"))
    return urls


def check(week):
    data = json.load(open(os.path.join(ROOT, "briefings", "weekly", f"{week}.json"), encoding="utf-8"))
    problems = []
    start = date.fromisoformat(data["period"]["from"])
    days = [(start + timedelta(days=i)).isoformat() for i in range(7)]
    if data["period"].get("to") != days[-1]:
        problems.append(f"period: to 는 from+6일({days[-1]})이어야 함")
    for d in data.get("days_covered", []):
        if d not in days:
            problems.append(f"days_covered: 기간 밖 날짜 {d}")
        elif not os.path.exists(os.path.join(ROOT, "briefings", f"{d}.json")):
            problems.append(f"days_covered: briefings/{d}.json 이 없음")
    known = raw_urls(days)

    def sources(where, srcs):
        for s in srcs or []:
            if s.get("url") not in known:
                problems.append(f"{where}: 그 주 원자료에 없는 URL {s.get('name')} {s.get('url')}")

    for i, p in enumerate(data.get("persistent", [])):
        where = f"persistent[{i}] {p.get('topic', '')[:24]}"
        if not p.get("sources"):
            problems.append(f"{where}: 출처 없음")
        sources(where, p.get("sources"))
        if len(p.get("days", [])) < 3 and len(p.get("countries", [])) < 3:
            problems.append(f"{where}: 3일 이상 또는 3개국 이상이 아님")
        for d in p.get("days", []):
            if d not in days:
                problems.append(f"{where}: 기간 밖 날짜 {d}")
        for c in p.get("countries", []):
            if c not in COUNTRIES:
                problems.append(f"{where}: 알 수 없는 국가 {c}")
    for i, s in enumerate(data.get("scenario_check", [])):
        where = f"scenario_check[{i}]"
        if s.get("outcome") not in OUTCOMES:
            problems.append(f"{where}: outcome 은 {sorted(OUTCOMES)} 중 하나")
        sources(where, s.get("sources"))

    fb = data.get("fishbone", {})
    ids = set()
    for bone in fb.get("bones", []):
        if bone.get("field") not in FIELDS:
            problems.append(f"fishbone: 알 수 없는 분야 {bone.get('field')}")
        for item in bone.get("items", []):
            if item.get("id") in ids:
                problems.append(f"fishbone: 중복 id {item.get('id')}")
            ids.add(item.get("id"))
    for link in fb.get("links", []):
        for end in ("from", "to"):
            if link.get(end) not in ids:
                problems.append(f"fishbone link: 없는 잔뼈 id {link.get(end)}")

    hw = data.get("hypothesis_week", {})
    if not hw.get("against"):
        problems.append("hypothesis_week: 반박 증거(against)가 비어 있음 — 없으면 '이번 주 반박 증거 없음'을 명시")
    if not data.get("faded") and not data.get("bias_notes"):
        problems.append("faded·bias_notes 가 모두 비어 있음 — 사라진 뉴스가 없었다면 그 사실과 이유를 bias_notes 에 적는다")
    return problems


def main():
    week = sys.argv[1]
    problems = check(week)
    if problems:
        print(f"검증 실패 {len(problems)}건:")
        for p in problems:
            print(f"- {p}")
        sys.exit(1)
    print("검증 통과: 주간 출처가 모두 그 주 원자료에 있음, 구조 정상")


if __name__ == "__main__":
    main()
