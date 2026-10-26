#!/usr/bin/env python3
"""피쉬본(이시카와) 다이어그램 SVG 생성기 (표준 라이브러리만 사용).

입력 JSON 형식:
{
  "title": "주식 — 반도체 랠리의 배경",
  "head": "AI 연산력 = 새로운 원유",          # 물고기 머리: 결과/본질
  "bones": [                                 # 큰 뼈: 원인 범주 (2~8개 권장)
    {"label": "미국", "items": ["엔비디아 실적 [US-3]", "수출통제 완화 [US-7]"]},
    {"label": "중국", "items": ["희토류 수출 제한 [CN-2]"]}
  ]
}
items 는 짧게(20자 내외) 쓰고 끝에 팀장 다이제스트 ID([US-3] 등)를 붙인다.

사용 예:
    python3 scripts/fishbone.py spec.json out.svg
    python3 scripts/fishbone.py --dir data/2026-10-26/fishbone --out briefings/2026-10-26
"""
import argparse
import json
import math
import unicodedata
from html import escape
from pathlib import Path

FONT = "'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif"
PALETTE = ["#2563eb", "#dc2626", "#059669", "#d97706", "#7c3aed", "#0891b2", "#db2777", "#4b5563"]
SLOT = 400          # 뼈 한 쌍(위/아래)이 차지하는 가로 폭
BONE_H = 240        # 큰 뼈의 세로 길이
BONE_DX = 160       # 큰 뼈의 기울기(가로 이동량)
WRAP = 16           # 항목 한 줄 최대 폭(전각 문자 기준)


def text_width(s):
    return sum(1.0 if unicodedata.east_asian_width(c) in "WF" else 0.6 for c in s)


def wrap(s, width):
    """단어(공백) 단위로 줄바꿈해 [US-3] 같은 출처 ID가 쪼개지지 않게 한다. 최대 2줄."""
    lines, cur = [], ""
    for word in s.split(" "):
        cand = f"{cur} {word}" if cur else word
        if text_width(cand) <= width or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    if len(lines) > 2:
        lines = [lines[0], " ".join(lines[1:])]
    if text_width(lines[-1]) > width * 1.15:
        tail = lines[-1]
        while text_width(tail + "…") > width * 1.15:
            tail = tail[:-1]
        lines[-1] = tail + "…"
    return lines


def tspans(lines, x, y, size, anchor):
    out = [f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" text-anchor="{anchor}" font-family="{FONT}" fill="#111827">']
    for i, line in enumerate(lines):
        out.append(f'<tspan x="{x:.0f}" dy="{0 if i == 0 else size + 3}">{escape(line)}</tspan>')
    out.append("</text>")
    return "".join(out)


def render(spec):
    bones = spec["bones"]
    cols = max(1, math.ceil(len(bones) / 2))
    head_w, margin = 260, 40
    title_h = 60 if spec.get("title") else 20
    width = margin + cols * SLOT + 40 + head_w + margin
    height = title_h + 2 * BONE_H + 120
    spine_y = title_h + BONE_H + 60
    spine_x0, spine_x1 = margin, margin + cols * SLOT + 40

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="#ffffff"/>',
    ]
    if spec.get("title"):
        svg.append(f'<text x="{margin}" y="38" font-size="22" font-weight="700" font-family="{FONT}" fill="#111827">{escape(spec["title"])}</text>')

    # 척추 + 머리
    svg.append(f'<line x1="{spine_x0}" y1="{spine_y}" x2="{spine_x1}" y2="{spine_y}" stroke="#111827" stroke-width="5"/>')
    hx, hy = spine_x1, spine_y - 55
    svg.append(f'<path d="M{hx},{hy} L{hx + head_w - 30},{hy} L{hx + head_w},{spine_y} L{hx + head_w - 30},{hy + 110} L{hx},{hy + 110} Z" fill="#111827"/>')
    head_lines = wrap(spec.get("head", ""), 12)
    svg.append(tspans(head_lines, hx + (head_w - 30) / 2, spine_y - (len(head_lines) - 1) * 10 + 6, 16, "middle").replace('fill="#111827"', 'fill="#ffffff" font-weight="700"'))

    for i, bone in enumerate(bones):
        col, up = i // 2, i % 2 == 0
        color = PALETTE[i % len(PALETTE)]
        jx = margin + (col + 1) * SLOT            # 척추 위 접점
        tx = jx - BONE_DX                          # 뼈 끝점
        ty = spine_y - BONE_H if up else spine_y + BONE_H
        svg.append(f'<line x1="{jx}" y1="{spine_y}" x2="{tx}" y2="{ty}" stroke="{color}" stroke-width="3"/>')

        # 범주 라벨
        label = bone["label"]
        lw = text_width(label) * 15 + 24
        ly = ty - 34 if up else ty + 6
        svg.append(f'<rect x="{tx - lw / 2:.0f}" y="{ly}" width="{lw:.0f}" height="28" rx="6" fill="{color}"/>')
        svg.append(f'<text x="{tx}" y="{ly + 19}" font-size="15" font-weight="700" text-anchor="middle" font-family="{FONT}" fill="#ffffff">{escape(label)}</text>')

        # 잔뼈: 뼈를 따라 균등 배치, 왼쪽으로 가로선 + 텍스트
        items = bone.get("items", [])[:6]
        for k, item in enumerate(items):
            t = (k + 1) / (len(items) + 1)
            px, py = tx + t * (jx - tx), ty + t * (spine_y - ty)
            svg.append(f'<line x1="{px - 240:.0f}" y1="{py:.0f}" x2="{px:.0f}" y2="{py:.0f}" stroke="{color}" stroke-width="1.5"/>')
            svg.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3" fill="{color}"/>')
            lines = wrap(item, WRAP)
            base = py - 6 - (len(lines) - 1) * 15
            svg.append(tspans(lines, px - 26, base, 12, "end"))

    svg.append("</svg>")
    return "\n".join(svg)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("spec", nargs="?", help="입력 JSON")
    p.add_argument("output", nargs="?", help="출력 SVG")
    p.add_argument("--dir", help="이 폴더의 모든 *.json 을 변환")
    p.add_argument("--out", help="--dir 사용 시 출력 폴더")
    args = p.parse_args()

    if args.dir:
        out_dir = Path(args.out or args.dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        pairs = [(f, out_dir / f"fishbone-{f.stem}.svg") for f in sorted(Path(args.dir).glob("*.json"))]
    elif args.spec and args.output:
        pairs = [(Path(args.spec), Path(args.output))]
    else:
        p.error("spec/output 또는 --dir 를 지정하세요")

    for src, dst in pairs:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(render(json.loads(src.read_text(encoding="utf-8"))), encoding="utf-8")
        print(f"{src} -> {dst}")


if __name__ == "__main__":
    main()
