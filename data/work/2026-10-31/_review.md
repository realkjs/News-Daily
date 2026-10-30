# 2026-10-31 임원 초안 검토 (팀장 · 검토 모드)

- 대상: `briefings/2026-10-31.json` (generated_at 2026-10-31 06:28 KST)
- 대조 기준: `data/raw/2026-10-31/<팀>.json`의 title_original / summary_original / published (보조: work 번역본, `_lead.json`)
- 시각 기준: 미 증시 마감 05:00 KST(10-30 EDT 16:00), 원유 정산 03:30 KST
- `python template/verify.py 2026-10-31` 결과: **검증 통과: 선별 뉴스 55건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상**
- TOP 10 누락: 없음 (`_lead.json` top10 10건과 브리핑 top10이 같음)

---

## [필수 수정]

### 필수 1. CENTCOM이 '유조선 피격 주장'을 부인했다고 씀 — 원문을 잘못 읽음 (유형 5)
- 위치: `essence.headline`("호르무즈에서는 피격 주장과 부인이 엇갈린다"), `essence.derivation.rebuild`("미군이 부인해"), `hypothesis_check.support[0]`("CENTCOM은 부인"), `hypothesis_check.note`("척수 불일치, 미군 부인"), `fishbone.bones.geopolitics` n40 라벨("·부인")
- 문제: 원자료에서 CENTCOM이 거짓이라고 한 것은 **IRGC의 '미 해군 무인정 격파' 주장**이다. 유조선 3~4척 화재 주장을 직접 부인한 원문은 없다. CBS 원문도 '항로가 열려 있고 이란 해군은 파괴됐다'는 사령관 **주장(claims)**일 뿐 유조선 피격을 부인하는 내용은 없다.
- 원문 근거:
  - Interfax(ru37): "Утверждение КСИР об уничтожении … американского военного морского беспилотника … является ложным … как и многие другие заявления КСИР, прозвучавшие на этой неделе"
  - CBS(us29): "Strait of Hormuz routes remain clear, CENTCOM chief **claims**"
  - AP(us59) "Iran says 3 tankers strike mines…", Reuters(uk32) "IRGC Navy says four tankers catch fire" — 유조선에 대한 미측 반응은 원자료에 없다.
- 제안 문안:
  - headline: "…호르무즈에서는 이란 측의 유조선 피격 주장과 미군의 '항로 정상' 주장이 엇갈린다(유조선 주장에 대한 미측 직접 반응은 원자료에 없음)."
  - support[0]: "이란의 호르무즈 유조선 피격 주장(AP '3척'·Reuters '4척' — 독립 확인 없음; CENTCOM은 '항로 열려 있음'(CBS)이라 했고 IRGC의 무인정 격파 주장을 거짓이라 함(Interfax))"
  - n40 라벨: "CENTCOM '항로 열려 있다'·무인정 주장 부인"

### 필수 2. 단일 출처(연합뉴스)인 'FBI·비밀경호국 수사 착수'를 "복수 출처로 단단한 사실"에 넣음 (유형 4)
- 위치: `essence.derivation.rebuild` ②("바이낸스 63억 달러 해킹과 미 수사 착수")
- 문제: 수사 착수는 원자료 전체에서 연합뉴스 1건(kr46)뿐이다. 다른 FBI 언급(AP us60 코미, Guardian uk52)은 무관하다. 해킹·금액은 복수 출처지만 '미 수사 착수'는 단일 출처다.
- 원문 근거: 연합뉴스(kr46) "美 FBI·비밀경호국, '8.4조원 해킹' 바이낸스 공조수사 착수(종합)" — 같은 내용을 담은 다른 원자료 없음.
- 제안: "② 바이낸스 63억 달러 해킹(복수 출처; 북한 소행은 의혹 단계 — 미 수사 착수는 연합뉴스 단일·미확인)".

### 필수 3. 국방부의 '대러 발언 자제' 요구를 확인된 사실·복수 출처 근거로 씀 — 실제로는 소식통 전언 (유형 4·5)
- 위치: `essence.headline`("유럽에 대러 발언 자제를 요구하고"), `essence.derivation.rebuild` ③("복수 출처로 단단한 사실 … 미 국방부의 대러 어조 완화 요구"), `hypothesis_check.note`("…국방부의 대러 어조 완화 요구·올레시키 국지 휴전이 … (각각 복수 출처)"), `fields.geopolitics.phenomenon`("…낮추라고 했다")
- 문제: 원자료는 모두 익명 소식통·전언이다. CGTN은 관영이라 교차 확인으로 칠 수 없고, 매일경제는 "전해졌다"로 썼다. 공식 확인은 없다. 이 내용은 판정 '약화'의 근거('분쟁 장기화' 균열)로도 쓰였다.
- 원문 근거: Japan Times(jp92) "Pentagon tells Europeans to cool their rhetoric on Russia, **sources say**"; CGTN(cn12, 관영) 속보 제목; 매일경제(kr100) "…요구한 것으로 **전해졌다**".
- 제안:
  - headline: "…유럽에 대러 발언 자제를 요구했다는 소식통 보도(Japan Times; 관영 CGTN 전재)도 나왔고…"
  - rebuild ③: "유럽 재원의 패트리엇 판매 승인(복수 출처). 국방부의 어조 완화 요구는 소식통 보도 단계(공식 확인 없음)."
  - note: "(각각 복수 출처)"를 "(트럼프 발언·카타르 중재·올레시키는 복수 출처, 국방부 요구는 소식통 보도)"로 고친다. watch[3]의 '공식 확인 여부'와 맞춘다.

### 필수 4. '인텔 1970년대 이후 최악'을 5개 매체에 귀속 — CNBC에만 있는 내용 (유형 1)
- 위치: `hypothesis_check.against[0]`("인텔 1970년대 이후 최악의 하루(CNBC·Bloomberg·n-tv·Handelsblatt·Reuters)")
- 문제: '1970년대 이후 최악'은 CNBC만 썼다. Bloomberg는 '29% 폭락', n-tv는 '30%', Handelsblatt는 '30% 넘게', Reuters는 '사상 최악의 하루로 향함(on course for worst day ever, 마감 전 표현)'이다.
- 원문 근거: CNBC(us42) "worst day since 1970s"; Bloomberg(us52) "Intel Plunges 29%"; n-tv(de27) "Kursrutsch von 30 Prozent"; Handelsblatt(de40) "Intel verliert über 30 Prozent"; Reuters(uk30) "on course for worst day ever".
- 제안: "인텔 하루 29~30% 급락(Bloomberg·n-tv·Handelsblatt; CNBC '1970년대 이후 최악', Reuters '사상 최악의 하루로 향함')".

### 필수 5. '이틀 연속 … (복수 출처)' — 전날 자료를 오늘 복수 출처 근거처럼 씀 (유형 7·4)
- 위치: `hypothesis_check.against[0]` 끝("이틀 연속 AI 투자 기업이 시장·신용 검증을 받음(복수 출처)")
- 문제: '이틀 연속' 중 하루(10-30)는 오늘 원자료가 아니라 직전 브리핑이다. 게다가 10-30 브리핑은 그 근거('AI 회사채 기록', Bloomberg)를 "단일 출처라 판정 근거에서 뺀다"고 적었다. 따라서 '복수 출처'라는 표기는 틀렸다.
- 원문 근거: `briefings/2026-10-30.json` hypothesis_check.note "…AI 회사채 기록(Bloomberg)…은 단일 출처라 판정…"; 오늘 원자료에는 전날 상황을 담은 기사가 없다.
- 제안: 문장을 지우거나 "🔎 (10-30 브리핑의 AI 회사채 기록은 단일 출처였음 — 오늘 자료만으로 판단)"으로 바꾼다.

### 필수 6. by_country.il[4] ZIM 선박 침몰 — 10-29 자료이고 10-30 브리핑에 이미 들어감 (유형 7)
- 위치: `by_country.il[4]`
- 문제: 출처 Globes(il45)의 published가 **2026-10-29T22:36 KST**다. 같은 사건이 `briefings/2026-10-30.json`에 'ZIM 화물선 침몰'로 이미 실렸다. 오늘의 새 뉴스처럼 국가별 선별에 넣으면 안 된다.
- 원문 근거: Globes(il45) "ZIM-operated ship sinks in Black Sea after drone strike", published 2026-10-29T22:36:00+09:00.
- 제안: il[4]를 빼고 오늘 자료로 바꾼다(예: i24 il6 Goldberg '압박 캠페인은 트럼프에게도 시한' 또는 다른 10-30~31 기사). 남기려면 headline에 "(10-29 보도·전날 브리핑 기재)"를 달고 importance를 낮춘다.

### 필수 7. '금 3,900달러 아래' — 관영 단일 출처 수치를 TOP10 헤드라인·피쉬본 라벨에 표기 없이 씀 (유형 3·4)
- 위치: `top10[9].headline_ko`("금값 3,900$ 아래"), `fishbone.bones.monetary` n21 라벨("금 3,900$ 아래·금은 1년래 최저", country "de"), 링크 n11→n21 to_label
- 문제: 3,900달러라는 수치는 Xinhua(관영) 1건뿐이다. Handelsblatt는 수치 없이 '금·은이 1년 만에 최저 수준'이라고만 썼다. 헤드라인과 라벨에는 관영·단일 표시가 없고, 라벨의 국가는 de로 붙어 있다.
- 원문 근거: Xinhua(cn18, state_media=true) "国际金价跌破每盎司3900美元"; Handelsblatt(de40) "Die Preise für Gold und Silber liegen derweil so niedrig wie seit einem Jahr nicht mehr."
- 제안: headline "…연준 '매파적 동결' 평가, 금·은 1년 만에 최저(Handelsblatt)"; n21 "금·은 1년래 최저(관영 '3,900$ 아래')". why의 Xinhua 문장에 "단일" 표기를 추가한다.

### 필수 8. 라브로프-루비오 '나쁘지 않은 대화'를 3개 매체에 귀속 — Interfax에만 있음 (유형 1)
- 위치: `top10[4].why`("라브로프는 루비오와 짧지만 나쁘지 않은 대화를 했다고 밝혔다(Interfax·Vedomosti·RBC)"), `essence.derivation.decomposition`("라브로프-루비오 '나쁘지 않은 대화'(Interfax·Vedomosti·RBC)")
- 문제: '나쁘지 않은(неплохой)'이라는 평가는 Interfax만 전했다. RBC는 '짧았고 양자관계·다자 협력을 논의했다'고만 썼고, Vedomosti는 제목만 있다('루비오와의 협상에 대해 말했다').
- 원문 근거: Interfax(ru35) "Был у нас неплохой разговор, короткий…"; RBC(ru67) "встреча продолжалась недолго … обсудили двусторонние отношения…"; Vedomosti(ru57) 요약 없음.
- 제안: "라브로프는 루비오와 짧은 대화를 했다고 밝혔고(Interfax·Vedomosti·RBC), Interfax에 따르면 '나쁘지 않은 대화'라고 평가했다."

---

## [권고]

1. **유가 기사와 장 마감 뒤 사건의 병치** — `by_country.us[3].why`, `hypothesis_check.support[0]`
   - 문제: 호르무즈 유조선 주장(AP 05:13·Reuters 05:40 KST), CENTCOM 반응(05:32·05:54), WaPo 러 정유소 화재(06:10)가 모두 원유 정산(03:30) 뒤에 나왔다. 그런데 같은 항목·불릿에 WSJ '유가 상승'이 함께 놓여 있어 인과처럼 읽힌다. top10[2]에는 시각 단서가 있지만 여기에는 없다.
   - 제안: 해당 문장에 "(피격 주장·정유소 화재는 정산 03:30 KST 뒤 보도 — 이날 유가의 원인 아님)"을 덧붙인다.

2. **패트리엇 '판매 승인' → '잠재적(가능) 판매 승인'** — `top10[3].headline_ko`, `essence.headline`, n34 라벨, `by_country.de[1]`·`ru[3]` headline
   - 원문: CNN "approves **potential** $2.1 billion sale", Vedomosti "потенциальную продажу", Meduza "возможную продажу". 의회 통보 단계이지 계약 체결이 아니다. us[2]는 이미 '잠재 승인'으로 썼으니 나머지도 맞춘다.

3. **재원 귀속 분리** — `essence.derivation.decomposition`·`fields.geopolitics.phenomenon`("재원은 … EU 대출(WELT; FAZ)"), `hypothesis_check.support[1]`("…주계약자 록히드 마틴(WELT; FAZ)")
   - 원문: EU 대출(우크라이나 자체 자금)과 록히드 마틴은 WELT(de34)만 썼다. FAZ(de57)는 "Deutschland, Kanada und Norwegen beteiligen sich an den Kosten"뿐이다.
   - 제안: "독·캐·노 분담(WELT·FAZ), EU 대출 재원의 우크라이나 자체 자금과 주계약자 록히드 마틴(WELT)". support[1]의 "전쟁 비용은 동맹이, 매출은 미국 방산이"에는 🔎를 붙인다.

4. **'같은 날' 시점 보정** — 링크 n34→n36 logic, `hypothesis_check.note`("같은 날 어조 완화 요구가 붙어")
   - 원문 시각: 국방부 요구 보도는 CGTN 10-30 14:00·Japan Times 15:51 KST이고, 패트리엇 승인 보도는 10-31 04:19~05:48 KST다. 약 14시간 앞선다.
   - 제안: "하루 사이에(국방부 요구 보도가 약 14시간 먼저)".

5. **올레시키 '순조롭게 완료'는 러시아 측 주장** — `top10[3].why`("Xinhua 관영 '순조롭게 완료'")
   - 원문: Xinhua(cn19) "**俄方称**奥列什基人道主义任务顺利完成". 제안: "Xinhua(관영)가 러시아 측 '순조롭게 완료' 발표를 전재". 완료 여부는 Handelsblatt '완료'·FAZ '거의 끝남'으로 따로 확인된다고 적는다.

6. **i24 '밴스 서한' 보도 인용 표기 통일** — `top10[2].why`("i24는 … 답하지 않았다고 보도했고"), `by_country.il[2].headline_ko`("이란, 밴스 서한 수령 확인·미답신"), `hypothesis_check.against[2]`
   - 원문: i24(il7) 제목 끝이 "- Report"다(타 매체 보도 인용). 제안: why는 "i24가 보도를 인용해 전했다(단일)", il[2] headline은 "이란, 밴스 서한 수령·미답신 보도", against[2]의 해당 항목에는 "단일" 표기를 추가한다.

7. **'핵무기 불가 보장' 귀속** — `top10[2].why`
   - 원문: '핵무기 불가 보장 필요'는 한국경제TV(kr52) 제목에만 있다. 경향(kr95) 제목·요약에는 없다(요약이 잘려 있음). 제안: "…곧 마무리될 것(한국경제TV·경향신문), 핵무기 불가 보장 필요(한국경제TV)".

8. **가설 태그 불일치** — `top10[2].hypothesis`=지지 vs `by_country.kr[1]`=반박 (같은 '트럼프 곧 마무리·카타르' 기사), `top10[3]`=지지 vs `by_country.kr[4]`·`jp[2]`=반박 (같은 '국방부 어조' 기사)
   - hypothesis_check.against[2]는 이 내용을 '분쟁 장기화 균열'로 분류한다. 제안: top10[2]는 지지·반박 근거가 섞여 있다고 why에 적고 태그는 '반박'으로 맞춘다. top10[3]은 판매(지지)와 어조(반박)가 섞였다고 명시한다.

9. **'사상 최대' 단정** — `top10[0].headline_ko`("사상 최대 암호화폐 도난")
   - 원문: AP "**likely** the biggest-ever", BBC "**is believed to be** the largest ever". 제안: "사상 최대로 추정되는 암호화폐 도난".

10. **NTV '1조 엔'** — `top10[0].why`("엔화는 NTV '약 1조 엔'"), `by_country.jp[1].headline_ko`("63억$(약 1조 엔)")
    - 원문: NTV(jp9) "暗号資産**“1兆円影響”**" — 피해 금액이 아니라 '영향' 규모다. 제안: "NTV '1조 엔 영향'". jp[1] 헤드라인의 괄호는 지운다.

11. **G20 단체사진 — Meduza는 Bloomberg 인용** — `top10[4].why`("BBC·Sky·Meduza")
    - 원문: Meduza(ru51) "…пишет Bloomberg". 제안: "BBC·Sky·Meduza(Bloomberg 인용)".

12. **폴란드 — 관영 '상세 보도' 과장, 해석 표시 누락** — `top10[5].why`("TASS·RIA(관영)도 상세 보도 — 러시아 관영의 관심 자체가 메시지")
    - 원문: TASS(ru18)는 TVP Info를 인용한 제목뿐이고, RIA(ru28)도 제목뿐이다(요약 없음). 제안: "TASS·RIA(관영)도 단신 보도 — 🔎 러시아 관영의 관심 자체가 메시지". '3명 체포'에는 "(WELT 단일)"을 붙인다.

13. **SCMP 분석가 전망을 사실처럼 씀** — `top10[7].why`·`fields.forecast.phenomenon`("SCMP: … 강화되겠지만 … 유지될 것")
    - 원문: cn34 "…could bring tougher scrutiny … likely to maintain …, **analysts said**". 제안: "SCMP가 인용한 분석가들은 … 전망".
    - `fields.forecast.cause`의 "선거 결과가 대중 정책보다 재정·관세 감독에 영향을 준다고 보기 때문(SCMP 분석 기준)"은 SCMP 원문(트럼프의 대중 거래에 대한 감독)과 다르다. 원문에 없는 '재정·관세'를 지운다.

14. **forecast 기본 시나리오 근거 없음** — `fields.forecast.scenarios[0].desc`("민주당 하원 탈환·공화당 상원 유지")
    - 원자료에 하원·상원 판세를 정리한 기사는 없다(Spiegel은 '미시간 엘사예드 우세', CNBC는 '알래스카가 상원 다수당을 가를 수도'라고만 썼다). 제안: 🔎를 붙이고 "원자료에 전체 판세 근거 없음"을 적거나, 원자료에 있는 경합(텍사스·미시간·알래스카) 중심으로 고친다.

15. **피쉬본 링크 정합성**
    - n29→n31: logic은 NYT와 닛케이의 시장 해석 대비인데 출발점이 '사전투표'(n29)다. 출발점을 n30(NYT '시장은 중간선거 무관심')으로 바꾼다.
    - n23→n28: DW(de17)가 잇는 것은 '전국 시위→교육 40억 유로 추가 지출 vs 금리 상승'이지 '시위 경로 법정 공방'이 아니다. logic을 "DW는 시위 대응 지출과 금리 부담을 함께 썼다 — 경로 공방 자체와의 연결은 🔎"로 고치거나 링크를 뺀다.
    - n11→n21: "위험자산과 안전자산이 함께 빠진 하루"는 Bloomberg(us50 "investors rushed back to the defensive stocks", us51 "perceived safety" 애플)·Les Echos(fr44 '안전자산 선호로 차입금리 하락')와 맞지 않는다. Handelsblatt도 당일 하락이 아니라 1년래 최저 '수준'을 썼다. 제안: "금·은은 1년래 최저 수준(Handelsblatt) — 같은 날 방어주·애플·채권으로는 피난 수요(Bloomberg·Les Echos)."
    - n15→n44: 바이낸스 해킹과 북한 드론 훈련 공개의 병치는 연결 근거가 없는 억지 연결에 가깝다. 남기려면 "🔎 북한 관련 두 뉴스가 겹쳤을 뿐"으로 낮추고, 아니면 뺀다.

16. **북한 드론 — 북한 관영 공개물 표기** — `by_country.kr[2]`, `essence.derivation.decomposition`("같은 날 북한은 … 자폭 드론을 날렸다")
    - 원문: 동아(kr75) "…훈련 사진을 30일 공개", "조선중앙통신이 30일 보도". 훈련 날짜는 원자료에 없고, 출처는 북한 관영 발표다. 제안: "북한이 조선중앙통신을 통해 … 자폭 드론 훈련 사진을 공개했다([메시지], 동아·SBS·중앙)".

17. **누락된 반박·지지 증거**
    - CBS(us30) "Trump took reporters' questions … on topics ranging from **potential sanctions against Russia** … Standing next to him was Stephen Hubbard, an American recently released from a Russian prison." '어조를 낮춘다'는 해석에 대한 반대 신호(대러 추가 제재 가능성 언급)이자 미·러 수감자 석방이라는 접촉 신호다. `fields.geopolitics.counter` 또는 `hypothesis_check`에 넣는다(제목·요약 수준, 단일).
    - KBS(kr5)·MBC(kr14) '젠슨 황 곁 中 스파이…48억 달러 칩 빼돌렸나' — 가설의 '기술 제재' 포위선과 관련된 지지 쪽 신호인데 브리핑에 없다. 의혹 단계(물음표 제목)로 support에 추가할지 검토한다.

18. **가설 반박 논리의 간접성 표시** — `hypothesis_check.against[0]`·`[1]`
    - 기술주 급락은 'AI 결제의 달러화' 가설을 직접 반증하지 않는다(밸류에이션 조정). 바이낸스(거래소) 해킹도 '달러 스테이블코인 활성화'를 직접 반증하지 않으며, 규제된 달러 스테이블코인 쪽으로 수요가 옮겨 가는 반대 해석도 가능하다. 제안: 각 항목에 "🔎 간접 증거" 한 줄과 그 반대 해석을 붙인다.

19. **배경 사례(precedent) 사실 정밀도**
    - `fields.geopolitics.precedent` "2018년 싱가포르 회담 전 스위스 등 중립국 채널": 당시 주된 중립국 채널은 스웨덴이었다. "스웨덴 등"으로 고치는 것을 권한다.
    - `fields.industry.precedent` "2011년 리비아 내전 때 송유 중단이 유럽 정제 마진을 끌어올린 사례": 당시 두드러진 현상은 경질 원유 공급 차질에 따른 브렌트 상승과 IEA 비축유 방출이었다. 정제 마진 상승으로 단정하기는 어렵다. "브렌트 상승·IEA 비축유 방출"로 바꾼다.

20. **기타 세부**
    - `by_country.de[2]`·`fields.stocks.phenomenon`: 닥스 26,000 붕괴를 쓸 때, 같은 기사(de42)의 "Auf Wochen- und Monatssicht verzeichnet er indes Gewinne"(주간·월간으로는 상승)를 반대 정보로 함께 적는다.
    - `fields.monetary.phenomenon`: Les Echos(WSJ 인용) '10월 차입금리 하락'이 어느 시장 얘기인지 원문에 없다. 프랑스 '사상 최고 차입금리'(Le Monde) 바로 뒤에 두면 모순처럼 읽히므로 "대상 시장 미상(미국 추정, 🔎)"을 적는다.
    - `fields.industry.phenomenon` 비셰이 '약 10억 유로': WELT(de37)는 "Die genaue Summe nannte Vishay nicht. Nach Angaben der CDU-Landtagsfraktion … rund eine Milliarde"라고 썼다. 회사 공식 금액이 아니라고 덧붙인다.
    - 데이터 품질: 매일경제 kr100(07:09)·kr96(08:00)·kr97(07:59)의 published가 수집 시각(06:14)보다 늦다. 타임존 오기로 보이므로, 이 기사들은 시각 근거로 쓰지 않는다(현재 시각 논리에 쓰인 곳은 없음).

---

## 판정

**판정: 수정 필요**

- [필수 수정] **8건**: CENTCOM 부인 오독 / FBI 수사 단일 출처 / 국방부 요구 소식통 / 인텔 '1970년대' 귀속 / '이틀 연속' 전날 자료 / ZIM 10-29 자료 / 금 3,900$ 관영 단일 / 라브로프 '나쁘지 않은' 귀속
- [권고] **20건**
- 총 28건. 필수 1·3은 `essence`와 `hypothesis_check.note`(판정 근거)에 걸려 있다. 이를 고친 뒤에도 판정 '약화'를 유지할 수 있는지 note에서 다시 설명해야 한다. 기술주 급락·바이낸스 해킹·트럼프 종전 발언·카타르 중재·올레시키는 복수 출처로 남으므로 '약화' 유지는 가능해 보이나, 근거 목록에서 소식통 항목은 빼야 한다.

---

## 반영 결과 (임원 최종)

- [필수 수정] 8건 전부 반영: CENTCOM 부인 범위 정정(무인정 주장만), FBI 수사 단일 표기, 국방부 요구를 소식통 보도로 낮추고 판정 근거에서 제외, 인텔 '1970년대' CNBC 귀속, '이틀 연속' 문장 삭제, il[4] ZIM(10-29) → 야이르 네타냐후 발언(Haaretz·JPost)으로 교체, 금 3,900$ 관영 단일 표기, '나쁘지 않은' Interfax 귀속.
- [권고] 20건 반영: 1~16·18~20 반영, 17은 CBS 대러 제재 질문·허버드 동석(counter·against)과 젠슨 황 스파이 의혹(support, 의혹 단계) 추가로 반영. 링크 n15→n44 삭제, n29→n31 출발점 n30으로 변경.
- 판정 '약화' 유지 — note에 소식통 항목을 뺀 뒤의 근거로 다시 설명.
- `python template/verify.py 2026-10-31` 재통과.
