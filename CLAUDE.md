# News-Daily 운영 절차 (Claude용)

매일 아침 예약 작업이 이 절차를 그대로 실행한다. 모든 산출물은 한국어.

## 0. 준비
- 날짜 = 오늘(KST, YYYY-MM-DD). `git pull`로 최신 상태를 받는다.
- 원자료: `data/raw/<날짜>/*.json` (GitHub Actions `collect.yml`이 04:47 KST에 RSS로 수집해 커밋).
- 원자료가 없거나 총 0건이면: `gh workflow run collect.yml`로 수집을 한 번 실행하고 끝나기를 기다린 뒤 `git pull`. 그래도 없으면 분석하지 말고 원인(`_summary.json`, 워크플로 로그)을 보고하고 종료한다. 웹 검색으로 뉴스를 지어내지 않는다.

## 1. 팀원 (9개국)
- 국가별로 Agent(subagent)를 하나씩, 병렬로 띄운다. 각자 `prompts/team-member.md` 기준으로 자기 나라 `data/raw/<날짜>/<팀>.json`을 읽어
  번역(title_ko, summary_ko)·분야 태그(tags)를 붙이고 중복을 묶어 `data/work/<날짜>/<팀>.json`에 저장한다.
- 원자료에 없는 기사·링크를 추가하지 않는다 (작업 환경에서 방송사 사이트 직접 접속은 막혀 있음).
- 임시 파일은 `data/work/<날짜>/tmp/<팀>/` 에만 (공용 스크래치패드 금지 — 병렬 팀원끼리 덮어쓴다).
- 다 끝나면 9개 파일이 모두 있고 각 파일의 `team` 값이 파일명과 같은지 확인한다. 틀리면 그 팀원만 다시 실행한다.

## 2. 팀장 — 선별
- `prompts/team-lead.md` + `prompts/analysis-framework.md` 적용. 9개 팀 work 파일을 모두 읽고 국가별 3–5개, 국가 횡단 TOP 10 선별 → `data/work/<날짜>/_lead.json`.

## 3. 임원 — 초안
- `prompts/executive.md` 적용. 팀장 결과를 8개 분야로 나누고 피쉬본(머리=본질, 큰 뼈=분야, 잔뼈=뉴스, links=분야 간 연쇄)과 분야별 해설 작성.
- 팀장이 놓친 연결이 보이면 팀장 결과를 보강한다(협업).
- `briefings/<날짜>.json` 초안 작성 (스키마 `briefings/SCHEMA.md`) → `python template/verify.py <날짜>` 통과.

## 4. 팀장 — 검토 (임원과 협업)
- `prompts/team-lead.md`의 "검토 모드"로 초안을 점검 → `data/work/<날짜>/_review.md` (`[필수 수정]`/`[권고]`, 판정).

## 5. 임원 — 최종
- 검토의 `[필수 수정]` 전부 반영, `[권고]`는 판단 반영 → `briefings/<날짜>.json` 갱신.
- `python template/verify.py <날짜>` 가 통과해야 다음 단계로 간다. 판정이 `수정 필요`였는데 필수 수정이 남아 있으면 4–5단계를 한 번 더 한다.

## 6. 산출
- `python template/render.py <날짜>` → `site/briefing.html`.
- Artifact 도구로 게시: 기존 "News-Daily 브리핑" 아티팩트 URL이 `site/ARTIFACT_URL`에 있으면 그 URL로 갱신(먼저 read), 없으면 새로 게시하고 URL을 그 파일에 저장.
- `git add briefings data/work site && git commit && git push`.
- 마지막에 SendUserMessage로 오늘의 본질 한 문장 + 핵심 3가지 + 가설 판정 + 검토에서 고친 것 개수 + 아티팩트 링크를 보낸다.

## 원칙
- 출처 없는 문장 금지. 선별 뉴스마다 방송사명 + 원자료 URL.
- 작업 가설은 검증 대상: 반박 증거를 반드시 찾고 표기한다.
- 국영·관영 매체(state_media=true)는 "메시지"로 읽는다.
- 단일 출처 수치·주장은 "단일 출처·미확인"으로 표시하고 핵심 근거로 쓰지 않는다.

---

# 주간 브리핑 (매주 일요일, 최신 편향 교정)

일요일 아침 예약 작업이 실행한다. 새 뉴스를 찾지 않고 그 주 일일 브리핑과 원자료만 다시 읽는다.

## W0. 준비
- 기간 = 이번 ISO 주의 월요일 ~ 일요일(오늘). 주 이름 = `YYYY-Www` (예: `2026-W44`, `date +%G-W%V`). `git pull`.
- 그 주 `briefings/<날짜>.json`이 몇 일분 있는지 확인한다. 0일이면 분석하지 말고 원인을 보고하고 종료한다.

## W1. 임원 — 주간 초안
- `prompts/weekly.md` + `prompts/analysis-framework.md` 적용 → `briefings/weekly/<주>.json` (스키마 `briefings/WEEKLY_SCHEMA.md`).
- `python template/verify_weekly.py <주>` 통과. 임시 파일은 `data/work/weekly/<주>/tmp/` 에만.

## W2. 팀장 — 주간 검토
- 점검: 이어진 흐름이 정말 여러 날에 걸쳐 있는가(일일 브리핑에서 날짜 확인), 사라진 소음 판정이 공정한가,
  예측 채점에 근거가 있는가(근거 없는 적중 금지), 반박 증거 누락 → `data/work/weekly/<주>/_review.md` (`[필수 수정]`/`[권고]`, 판정).

## W3. 임원 — 주간 최종
- 필수 수정 전부 반영 → `python template/verify_weekly.py <주>` 통과.

## W4. 산출
- `python template/render_weekly.py <주>` → `site/weekly.html`.
- Artifact 도구로 게시: `site/WEEKLY_ARTIFACT_URL`에 URL이 있으면 그 URL로 갱신(먼저 read), 없으면 새로 게시(title "News-Daily 주간 브리핑")하고 URL을 그 파일에 저장.
- `git add briefings/weekly data/work/weekly site && git commit && git push`.
- 마지막 메시지: 이번 주의 본질, 이어진 흐름 TOP 3, 사라진 소음 개수와 대표 1건, 예측 채점(적중/빗나감/진행중/확인불가), 가설 주간 판정, 페이지 링크.
