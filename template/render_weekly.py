#!/usr/bin/env python3
"""briefings/weekly/YYYY-Www.json → site/weekly.html (주간 브리핑 아티팩트로 게시할 페이지)

사용: python template/render_weekly.py 2026-W44
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    week = sys.argv[1]
    data = json.load(open(os.path.join(ROOT, "briefings", "weekly", f"{week}.json"), encoding="utf-8"))
    tpl = open(os.path.join(ROOT, "template", "weekly.html"), encoding="utf-8").read()
    # </script> 조기 종료 방지
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = tpl.replace("__BRIEFING_JSON__", payload)
    os.makedirs(os.path.join(ROOT, "site"), exist_ok=True)
    path = os.path.join(ROOT, "site", "weekly.html")
    open(path, "w", encoding="utf-8").write(out)
    print(path)


if __name__ == "__main__":
    main()
