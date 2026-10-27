# briefings/weekly/YYYY-Www.json 스키마 (주간 브리핑)

일일 브리핑은 그날 뉴스에 무게가 쏠린다(최신 편향). 주간 브리핑은 지난 7일치 일일 브리핑을 다시 읽어
**며칠 동안 이어진 흐름**과 **하루 크게 보였다가 사라진 소음**을 가르고, 지난주 예측이 맞았는지 채점한다.

```json
{
  "week": "2026-W44",
  "period": {"from": "2026-10-26", "to": "2026-11-01"},
  "generated_at": "2026-11-01 08:52 KST",
  "days_covered": ["2026-10-26", "2026-10-27"],
  "missing_days": ["2026-10-28"],

  "essence": {
    "headline": "이번 주의 본질 한 문장 (7일치를 근거로)",
    "derivation": {"assumptions": "", "decomposition": "", "rebuild": ""},
    "vs_daily": "일일 브리핑들이 과장했거나 놓친 것 — 최신 편향 교정 요지"
  },

  "persistent": [
    {"topic": "이어진 흐름 이름", "days": ["2026-10-26", "2026-10-27"], "countries": ["us", "il"],
     "trend": "확대|유지|약화", "fields": ["geopolitics"], "summary": "7일 동안 어떻게 전개됐나",
     "sources": [{"name": "Reuters", "url": "https://...", "date": "2026-10-27"}]}
  ],

  "faded": [
    {"topic": "하루 크게 다뤘다가 이어지지 않은 뉴스", "peak_date": "2026-10-26", "daily_importance": 5,
     "why_faded": "후속 보도가 없었던 이유(일회성·단일 출처·반박됨 등)", "lesson": "다음에 같은 유형을 어떻게 볼지"}
  ],

  "scenario_check": [
    {"from_date": "2026-10-26", "field": "geopolitics", "expected": "그날 제시한 시나리오/관찰 신호",
     "outcome": "적중|빗나감|진행중|확인불가", "evidence": "판정 근거",
     "sources": [{"name": "", "url": "", "date": ""}]}
  ],

  "hypothesis_week": {
    "daily_verdicts": [{"date": "2026-10-26", "verdict": "약화"}],
    "support": ["주간 누계 지지 증거 (여러 날·여러 매체로 확인된 것 우선)"],
    "against": ["주간 누계 반박 증거"],
    "verdict": "강화|유지|약화",
    "note": "일일 판정이 흔들린 이유, 주간으로 보면 어떤가"
  },

  "fields": [
    {"id": "industry", "week_summary": "이번 주 이 분야에서 이어진 것", "shift": "주 초 대비 주 말에 바뀐 것"}
  ],

  "fishbone": {
    "head": "이번 주의 본질(짧게)",
    "bones": [{"field": "industry", "items": [{"id": "w1", "label": "주간 흐름 라벨", "country": "us", "days": 3}]}],
    "links": [{"from": "w1", "to": "w5", "from_label": "", "to_label": "", "logic": "왜 연결되는지"}]
  },

  "watch_next_week": ["다음 주 확인할 일정·신호"],
  "bias_notes": ["최신 편향 점검 메모 — 예: 단일 출처 수치가 이후 확인됐는지"]
}
```

- `persistent`는 **3일 이상** 또는 **3개국 이상**에서 이어진 흐름만. `days`는 그 흐름이 일일 브리핑(선별·피쉬본)에 나온 날짜.
- `faded`의 `daily_importance`는 그날 팀장이 매긴 점수(1–5).
- 모든 `sources[].url`은 해당 주의 `data/raw/<날짜>/` 원자료에 있어야 한다 (`python template/verify_weekly.py <주>`).
- field id, country 코드는 일일 스키마와 같다.
