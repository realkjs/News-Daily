#!/usr/bin/env python3
"""briefings/YYYY-MM-DD.json → site/briefing.html (아티팩트로 게시할 페이지)

사용: python template/render.py 2026-10-27
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    date = sys.argv[1]
    data = json.load(open(os.path.join(ROOT, "briefings", f"{date}.json"), encoding="utf-8"))
    tpl = open(os.path.join(ROOT, "template", "briefing.html"), encoding="utf-8").read()
    # </script> 조기 종료 방지
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = tpl.replace("__BRIEFING_JSON__", payload)
    os.makedirs(os.path.join(ROOT, "site"), exist_ok=True)
    path = os.path.join(ROOT, "site", "briefing.html")
    open(path, "w", encoding="utf-8").write(out)
    print(path)


if __name__ == "__main__":
    main()
