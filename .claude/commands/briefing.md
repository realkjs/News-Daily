---
description: 9개국 팀원 → 팀장 → 임원 순서로 글로벌 뉴스 브리핑을 생성한다
argument-hint: "[YYYY-MM-DD] (생략 시 오늘, KST)"
---

글로벌 뉴스 브리핑을 생성한다. 날짜: `$ARGUMENTS` (비어 있으면 `TZ=Asia/Seoul date +%F` 로 오늘 날짜를 구해 DATE로 쓴다).

## 1단계 — 팀원 수집 (병렬)
한 번의 응답에서 아래 9개 서브에이전트를 **동시에** 실행한다. 각각에 `DATE=<DATE>` 를 전달한다.
`reporter-us`, `reporter-kr`, `reporter-jp`, `reporter-de`, `reporter-uk`, `reporter-fr`, `reporter-il`, `reporter-ru`, `reporter-cn`

모두 끝나면 `data/<DATE>/teams/` 에 9개 파일이 있는지 확인한다. 빠진 나라는 해당 팀원을 한 번 더 실행하고, 그래도 실패하면 공백으로 기록하고 진행한다.

## 2단계 — 팀장 선별
`team-lead` 를 `mode=digest, DATE=<DATE>` 로 실행 → `data/<DATE>/lead_digest.md`

## 3단계 — 임원 초안
`executive` 를 `mode=draft, DATE=<DATE>` 로 실행 → 피쉬본 JSON/SVG + `data/<DATE>/exec_draft.md`

## 4단계 — 팀장 검토 (임원·팀장 협력)
`team-lead` 를 `mode=review, DATE=<DATE>` 로 실행 → `data/<DATE>/lead_review.md`

## 5단계 — 임원 최종본
`executive` 를 `mode=final, DATE=<DATE>` 로 실행 → `briefings/<DATE>/briefing.md`
(검토 판정이 `수정 필요` 였고 최종본에 필수 수정이 남아 있으면 4~5단계를 한 번 더 반복한다.)

## 마무리
- 사용자에게 보고: 최종 브리핑 경로, 오늘의 본질 한 문장, 3줄 요약, 수집 실패 매체.
- 사용자가 커밋을 요청한 경우에만 `data/<DATE>/` (raw 제외)와 `briefings/<DATE>/` 를 커밋한다.
