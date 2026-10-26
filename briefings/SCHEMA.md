# briefings/YYYY-MM-DD.json 스키마

```json
{
  "date": "2026-10-27",
  "generated_at": "2026-10-27 06:52 KST",
  "essence": {
    "headline": "오늘의 본질 한 문장",
    "derivation": {"assumptions": "가정 의심", "decomposition": "근본 요소 분해", "rebuild": "재조립"}
  },
  "fishbone": {
    "head": "머리(결과) 문장 — 보통 essence.headline과 같거나 짧은 형태",
    "bones": [
      {"field": "industry", "items": [{"id": "n1", "label": "짧은 뉴스 라벨(25자 내외)", "country": "us"}]}
    ],
    "links": [
      {"from": "n1", "to": "n7", "from_label": "라벨", "to_label": "라벨", "logic": "왜 연결되는지 한 문장"}
    ]
  },
  "fields": [
    {"id": "industry", "phenomenon": "", "precedent": "", "cause": "", "essence": "", "counter": "",
     "scenarios": [{"name": "기본", "desc": "", "signal": ""}, {"name": "상방", "desc": "", "signal": ""}, {"name": "하방", "desc": "", "signal": ""}]}
  ],
  "hypothesis_check": {"support": [""], "against": [""], "verdict": "강화|유지|약화", "note": ""},
  "top10": [
    {"headline_ko": "", "importance": 5, "why": "", "sources": [{"name": "BBC", "url": "https://..."}],
     "fields": ["geopolitics"], "hypothesis": "지지|반박|무관"}
  ],
  "by_country": {"us": [/* top10과 같은 형식, 3–5개 */]},
  "watch": ["내일 지켜볼 신호"],
  "coverage": {"us": {"headlines": 40, "unavailable": ["AP"]}}
}
```

field id: industry, business, stocks, crypto, monetary, legislation, forecast, geopolitics
country: us, kr, jp, de, uk, fr, il, ru, cn
