# News-Daily

9개국 뉴스를 모아 팀원 → 팀장 → 임원 구조로 분석하는 브리핑 프로젝트.

- 실행: `/briefing [YYYY-MM-DD]` (`.claude/commands/briefing.md`)
- 분석 기준: **`prompts/analysis-framework.md` (사용자 설정 프롬프트) — 모든 분석 단계에서 반드시 따른다.**
- 에이전트: `.claude/agents/` — `reporter-<cc>` 9개, `team-lead`, `executive`
- 매체 목록: `config/sources.json`
- 스크립트: `scripts/collect_headlines.py` (RSS 수집), `scripts/fishbone.py` (피쉬본 SVG). 둘 다 표준 라이브러리만 사용.

규칙
- 헤드라인·사실·출처를 지어내지 않는다. 수집 실패는 실패로 기록한다.
- 사실에는 출처 ID(`[US-3]`), 해석·가설에는 표시를 단다.
- 날짜 기준은 KST.
