# News-Daily

9개국 주요 방송사 헤드라인을 매일 아침 모아, 팀원 → 팀장 → 임원 단계로 선별·분석하는 뉴스 브리핑.

| 단계 | 담당 | 하는 일 | 위치 |
|---|---|---|---|
| 수집 | GitHub Actions (05:20 KST) | 방송사 RSS / Google News 대체 수집 | `collector/`, `data/raw/` |
| 팀원 | Claude 하위 에이전트 9개 (미·한·일·독·영·프·이스라엘·러·중) | 번역, 분야 태그, 중복 정리 | `prompts/team-member.md`, `data/work/` |
| 팀장 | Claude | 중요 뉴스 선별 + 이유 + 출처 | `prompts/team-lead.md` |
| 임원 | Claude | 8개 분야 피쉬본 다이어그램 + 해설 + 시나리오 | `prompts/executive.md` |
| 산출 | Claude | `briefings/날짜.json` → 브리핑 페이지 게시 | `template/`, `site/` |

분석 기준: `prompts/analysis-framework.md` (진석님 설정 프롬프트 — 업무 흐름, 제1원칙 사고, 세계관, 검증 대상 가설)

분야: 산업 · 비즈니스 · 주식 · 코인 · 각국 통화정책 · 신규·처리중 법안 · 미래 예측 · 국제 지정학

방송사 추가/변경: `config/sources.json`
