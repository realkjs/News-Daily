# 2026-11-02 브리핑 초안 검토 (팀장 → 임원)

- 대상: `briefings/2026-11-02.json` (generated_at 2026-11-02 06:24 KST)
- 대조 기준: `data/raw/2026-11-02/<팀>.json`의 title_original / summary_original / published. 보조로 work 번역본, `_lead.json`, 직전 브리핑(10-31, 11-01, 필요한 경우 10-29·10-30)을 함께 봤다.
- `python template/verify.py 2026-11-02` 결과: **검증 통과: 선별 뉴스 53건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상**. URL 추적과 구조는 문제없다. 아래 지적은 모두 라벨·요약·귀속·판정 논리의 문제다.
- 누락 점검: 팀장 TOP 10의 10건은 모두 브리핑 top10에 들어 있다.

---

## [필수 수정]

### 1. Axios 보도를 실제로 담지 않은 매체에 귀속했다 (유형 1)
- 위치: `essence.derivation.decomposition`, `essence.derivation.rebuild`(③), `fishbone.links[0].logic`, `fields[geopolitics].phenomenon`, `top10[1].why`, `hypothesis_check.support[0]`, `hypothesis_check.note`
- 문제: 초안은 "네타냐후가 선거 후 재개를 촉구"했다는 내용을 "Vedomosti·Le Figaro의 Axios 인용", rebuild에서는 "Axios — Vedomosti·Le Figaro·연합뉴스·한국경제TV 인용"으로 썼다. 원문과 대조하면 다르다.
  - Vedomosti(ru#56): «Axios: Нетаньяху призвал Трампа возобновить войну против Ирана после выборов» → 네타냐후 촉구 + Axios 출처. 이 매체만 맞다.
  - Le Figaro(fr#49): «Trump aurait échangé avec Netanyahou… Selon Axios, le président américain a dit vouloir privilégier la voie diplomatique» → 네타냐후의 '선거 후 재개 촉구'는 원문에 없다. Le Figaro가 Axios를 인용한 내용은 '트럼프는 외교 우선'뿐이다.
  - 연합뉴스(kr#43)·한국경제TV(kr#51): '선거 직후 타격 압박…트럼프 유보적'이라는 내용만 있고, 원문 요약(잘림)과 제목 어디에도 Axios가 없다.
- 수정안: "네타냐후의 '선거 직후 타격' 압박(Vedomosti의 Axios 인용; 연합뉴스·한국경제TV — 출처 원문 미기재)", "Le Figaro(Axios 인용): 트럼프는 외교 경로를 우선하고 싶다고 말했다" 두 문장으로 나눈다. rebuild ③은 "(Vedomosti의 Axios 인용, 연합뉴스·한국경제TV 보도 — 원 출처는 사실상 Axios 1건일 수 있음)"으로 고친다.

### 2. Spiegel 단독 인용문을 FAZ에도 귀속했다 (유형 1)
- 위치: `essence.derivation.decomposition` "'한두 곳 더… 10분이면 끝낼 수 있다'(Spiegel; FAZ)", `fields[geopolitics].phenomenon` "'한두 곳 더… 10분이면'(Spiegel; FAZ)"
- 원문: Spiegel(de#48) «Wir müssen uns noch um ein oder zwei Anlagen kümmern, aber das können wir in zehn Minuten erledigen». FAZ(de#56)는 제목 «Trump bringt Angriffe auf weitere Ziele in Iran ins Spiel»뿐이고 인용문이 없다.
- 수정안: "'한두 곳 더… 10분이면'(Spiegel), 추가 목표 공격 거론(FAZ 제목)". top10[1].why는 이미 이렇게 구분해 썼으니 그 문안에 맞춘다.

### 3. FBI의 북한 지목을 "동아일보 단일"로 썼으나 SCMP도 보도했다. 거래소 인출 급증과 비트코인 급락도 빠졌다 (유형 4·5·6)
- 위치: `essence.derivation.decomposition`·`rebuild`, `fields[crypto]` 전 항목(phenomenon·cause·essence·counter), `fields[business].cause` "북한 지목(동아 단일)", `top10[7].why`, `by_country.kr[0].why`, `fishbone` n11 라벨, `hypothesis_check.against[4]`
- 원문:
  - SCMP(cn#30, 11-02 04:53): «Binance customers pulled US$3.64 billion, or 2.1 per cent of its assets, as the world's biggest cryptocurrency exchange went back online on Sunday after hackers **the FBI links to North Korea** stole billions… covered 95 per cent of…» → FBI의 북한 연계 판단은 2개 매체(동아·SCMP)가 보도했다. 출금 재개 뒤 인출 36.4억 달러(자산의 2.1%), 손실 95% 보전도 함께 나온다.
  - Kommersant(ru#42): «Взлом биржи Binance… обрушили курс биткойна до $76 тыс.» → 비트코인이 7.6만 달러로 급락했다. 코인은 주말에도 거래되므로 시점 문제는 없다.
  - 동아(kr#73) 원문은 "8조 원대"라고만 쓰고 날짜가 없다. 초안 crypto.phenomenon의 "지난달 29일"은 원자료에 없다(번역본이 덧붙인 것). "29일에 지목했다"로도 읽혀 오해를 부른다.
- 문제: "단일"이라는 전제가 틀리면서 crypto.counter의 "출금 재개(CNN)로 시장 영향은 이미 줄었을 수 있다"가 SCMP의 인출 급증·Kommersant의 비트코인 급락 보도와 정면으로 어긋난다.
- 수정안:
  - "FBI가 바이낸스 해킹(약 63억 달러 — SCMP; 동아 '8조 원대')의 배후로 북한을 지목(동아 '공식 지목'; SCMP 'FBI links to North Korea'). 트럼프 '확인되면 북한과 대화'는 동아 단일."
  - phenomenon에 "SCMP: 일요일 거래 재개 후 36.4억 달러(자산 2.1%) 인출, 바이낸스는 '안정 중'·95% 보전 주장. Kommersant: 해킹 여파로 비트코인 7.6만 달러까지 하락(단일)"을 추가한다.
  - counter는 "인출 급증(SCMP)과 비트코인 하락(Kommersant)은 시장 충격이 진행 중임을 보여 준다. 반대로 바이낸스는 인출이 안정되고 있다고 주장한다(SCMP)"로 바꾼다. "지난달 29일"은 삭제한다.

### 4. 일본은행 '동결·2% 도달 판단 전망'은 이미 지난 회의의 사전 예측 기사다 (유형 7)
- 위치: `fields[monetary].phenomenon`·`essence`·`scenarios[기본].signal`("일본은행 회의 결과"), `fishbone` n15 "일본은행 동결·'2% 도달' 판단 전망", `by_country.jp[1]`
- 원문: TV도쿄(jp#44, published 11-01 19:07) «日銀 政策金利据え置きへ 2％の物価目標は到達と判断の公算大»는 '~할 전망'이라는 회의 전 예측 제목이다.
- 기보도: 10-30 브리핑은 "일본은행은 금융정책 발표를 앞두고 '물가 2% 도달' 언급이 주목된다(아사히)"라고 썼고, 10-31 브리핑은 "일본은행: 13년 만에 물가 2%에 '도달'(마이니치)"를 이미 결과로 실었다. 회의는 끝났고, 이 기사는 늦게 올라온 영상 업로드로 보인다.
- 수정안: n15와 by_country.jp[1]을 빼거나 "12월 금리 인상 중간 점검(TV도쿄 jp#45, 제목)"으로 바꾼다. monetary.phenomenon에서 "동결 전망"은 지우고 "(10-30 결정 — 10-31 브리핑 기보도)"로 바꾼다. 기본 시나리오의 신호는 "12월 회의 전 인상 시사 발언"으로 고친다.

### 5. '김종양 인터폴 총재 선출'은 과거 기사가 다시 올라온 것으로 보인다 (유형 7)
- 위치: `by_country.kr[4].headline_ko`·`why`
- 원문: KBS(kr#1, kr#2) «김종양 전 경기청장, 인터폴 총재 선출… 한국인 최초». google_news 경유이고, 두 건이 같은 시각(11-02 03:28:50)에 요약 없이 들어왔다.
- 문제(🔎 검토자 배경지식이며 원자료로는 확인할 수 없음): 김종양의 인터폴 총재 선출은 2018년 11월 일이다. '전 경기청장'이라는 직함도 당시 직함이다. 원자료에는 이를 뒷받침할 다른 매체 보도가 없다. kr 팀원 notes도 같은 성격의 'JTBC AZ 백신' 기사에 대해 게재 시점 확인이 필요하다고 적어 두었다.
- 수정안: 이 건을 뺀다. 에르도안 2건만 남기거나, 대체로 "루비오 '북미회담 일정 없지만 대화 준비'(동아 kr#75 — 11-01 브리핑 기보도의 후속)"를 고려한다.

### 6. WSJ '유가 선물 상승'을 top10에서 시점 단서 없이 썼다 (유형 2)
- 위치: `top10[1].why` 끝 "WSJ '중동 확전 우려에 유가 선물 상승'(제목)"
- 원문: WSJ(us#72) «Oil Futures Rise on Fears of Middle East Escalation», 제목만 있고 published는 11-02 06:01 KST다. 미국은 11월 1일(일)에 서머타임이 끝났으므로 이 시각은 미 동부 11-01 16:01(EST)이다. CME 원유 선물은 일요일 18:00 ET에 개장하므로 이 기사의 '상승'은 일요일 거래를 반영할 수 없다. 직전 거래일 움직임이거나 시점을 알 수 없는 기사다. 11-01 브리핑도 "토요일이라 원유 거래·가격 정보 없음"이라고 적었다.
- 수정안: stocks.phenomenon처럼 "(제목만 — 발행 시각이 일요일 선물 개장 전이라 거래 시점 미확인)"을 붙이거나 top10에서 뺀다. 가격 수치는 쓰지 않는다.

### 7. 관영 RIA를 표기 없이 헤드라인 수치 출처로 썼다 (유형 3)
- 위치: `by_country.ru[4].headline_ko` "출구조사 58.2%(RIA)·52.5%(Vedomosti)"
- 원문: RIA Novosti(ru#31)는 state_media=true다. 같은 날 다른 매체 수치는 WELT(de#38) «51 Prozent», Vedomosti 52.5%, Libération 52.5~59%로 RIA가 가장 높다.
- 수정안: "불가리아 대선 요토바 선두 — 출구조사 51~59%(WELT 51%·Vedomosti 52.5%·[관영] RIA 58.2%)". top10[3].why와 decomposition의 수치 나열에도 WELT 51%를 넣는다.

### 8. 단일 출처 항목이 '복수' 판정 근거에 섞여 있고, 반박 쪽 단일 항목은 단일 표기가 빠졌다 (유형 4)
- 위치: `hypothesis_check.support[0]`("분쟁 장기화·재개 신호(복수)"), `hypothesis_check.against[0]`, `hypothesis_check.note`
- 문제:
  - support[0]의 "이스라엘 공동 타격 준비(JPost 소식통)"는 JPost(il#25) 1건이고 익명 소식통이다. 그런데도 '복수' 묶음에 들어가 판정 근거로 쓰였다. note는 "판정 근거는 복수 출처 항목만"이라고 해 놓고 이를 어긴다.
  - against[0]의 "이란 외무 '카타르 중재 진전'(MBC 제목)"과 "란트라토바 '정기 인도주의 미션 합의'(RBC)"도 각각 단일이다. 란트라토바 건은 러시아 당국자의 주장이다. 양쪽 기준이 달라 보인다.
- 수정안: JPost 건은 support[1](단일·관영) 묶음으로 옮긴다. against[0]에는 "(MBC 제목 단일)", "(RBC 단일 — 러 당국자 주장)"을 붙인다. note는 두 항목이 판정 근거에서 빠짐을 반영해 다시 쓴다.

### 9. 도네츠크 정전의 원인이 원문에 없는데 '양측 전력망 피해·공방'으로 썼다 (유형 6)
- 위치: `essence.derivation.rebuild` ⑥ "양측 전력망 피해", `fishbone.links[6].logic` "휴전 종료와 전력망 공방이 같은 날", `hypothesis_check.support[0]`·`note` "양측 전력망 피해(BBC·Reuters·Interfax)"
- 원문: Interfax(ru#35)는 "도네츠크 약 28만 가입자 정전, 1890개 변전소 차단(시장 쿨렘진 발표)"이라고만 썼다. Vesti(관영, ru#11)는 제목만 있다. 원인(우크라이나 공격 여부)은 어디에도 없다. BBC·Reuters의 정전은 우크라이나 측 정전(러 공습)이다.
- 수정안: "러 공습에 우크라이나 정전(BBC·Reuters), 러 점령 도네츠크 약 28만 가구 정전(Interfax — 원인 미기재; [관영] Vesti)". '공방'·'양측 피해'는 지우거나 🔎 해석으로 표시한다.

### 10. 가설 판정을 '약화'에서 '유지'로 바꾼 논리가 성립하지 않는다 (유형 8)
- 위치: `hypothesis_check.verdict`, `hypothesis_check.note`, `hypothesis_check.support[0]`
- 문제:
  1. **같은 사건을 날마다 반대 방향으로 셌다.** 11-01 브리핑은 "올레시키 국지 휴전 완료(복수)"를 반박 근거로 셌다. 오늘은 계획대로 끝난 같은 휴전의 "종료"를 지지 근거로 센다. 오늘 원자료는 오히려 반박 쪽 사실을 더 담고 있는데 빠져 있다. Kommersant(ru#46)는 «Локальное перемирие, достигнутое при посредничестве первой леди США Мелании Трамп, стало самой продолжительной и… самой успешной»라고 썼고(미국 중재로 성사된 최장·최고 성공 휴전), FAZ(de#58)는 «Präsident dankt den USA für Vermittlung der Waffenruhe», RBC(ru#67)는 정기 인도주의 미션 합의를 전했다. 미국이 휴전을 중재한 사실은 '분쟁 장기화로 달러 권력 공고화' 가설에 대한 반박이다.
  2. **'새로 늘었다'는 지지 근거의 상당수는 기보도의 연장이다.** 11-01 지지 근거에 이미 "중간선거 후 미국 공습 위협(Reuters)·이스라엘의 교전 재개 대비(Ynet)"가 있었다. 오늘의 '네타냐후 선거 후 재개 압박'은 같은 흐름이고, 원 출처는 사실상 Axios 1건이다(1번 참조). 이스라엘 공동 타격 준비는 JPost 단일이다(8번 참조).
  3. **지지 쪽 신호도 빠졌다.** FAZ(de#56) «Irans Außenminister: Keine Pläne für Gespräche mit den USA +++ Iran meldet Verletzten nach US-Angriff auf Fischerboote»는 MBC의 '카타르 중재 진전'과 엇갈리는 내용이고 분쟁 지속 쪽 신호인데 가설 점검표에 없다. 다만 '회담 계획 없음'은 11-01 브리핑의 아락치 발언(MBC·Xinhua)과 같은 발언일 수 있고, 어선 공격 주장은 11-01의 Handelsblatt '케슘섬 어선' 주장과 같은 사건일 수 있다.
  4. **가설의 다른 축은 여전히 약화 쪽이다.** 6회 연속 '약화'의 근거였던 AI(연산력) 축은 오늘도 반박 증거(CNBC 'AI 붕괴 우려', TV도쿄 '코어위브 쇼크', FT 정크본드)가 이어지고, 스테이블코인 근거는 없다. 오늘은 바이낸스 인출 급증·비트코인 급락(3번 참조)이 더해졌다. 이란 한 사건에서 지지와 반박이 '균형'을 이뤘다는 이유만으로 가설 전체 판정을 올릴 수는 없다.
- 수정안: 판정을 **'약화'로 유지**하고, note에 "이란 축에서는 선거 후 재개 압박 보도(Axios 계열)와 협상 진전 발언이 맞서 판단 보류, 우크라이나 국지 휴전은 미국 중재 성공 사례(Kommersant·FAZ)로 반박 쪽, AI·코인 축은 반박 지속 → 7회 연속 약화"라고 쓴다. 굳이 '유지'로 둔다면, 위 1~4를 반영하고도 남는 복수 출처 지지 근거를 note에 명시해야 한다. support[0]에서 "올레시키 휴전 종료"를 빼고, against에 "미국 중재 휴전(Kommersant·FAZ)"을, support에 "이란 외무 '미국과 회담 계획 없음'(FAZ 라이브블로그 단일)"을 추가한다.

### 11. The Economist 제목을 반대로 읽었다 (유형 5)
- 위치: `top10[0].why` "알래스카 사태가 민주당의 상원 장악을 무너뜨릴 수 있다", `by_country.uk[3].headline_ko` "Economist '알래스카 재앙이 민주당 상원 장악 무너뜨릴 수도'"
- 원문: Economist(uk#80) «An unfolding disaster in Alaska could cost Democrats the Senate». 민주당이 지금 상원을 장악하고 있다는 뜻이 아니다. 상원 다수당을 차지할 기회를 잃을 수 있다는 뜻이다.
- 수정안: "Economist: 알래스카에서 벌어지는 사태가 민주당의 상원 다수당 확보를 좌절시킬 수 있다(제목)".

### 12. 이전 브리핑에 실린 사실을 오늘 뉴스처럼 썼다 (유형 7)
- 위치와 근거:
  - `top10[0].why`, `fields[legislation].phenomenon`, `by_country.uk[3]`: "Sky: 동명 후보에 대한 연방 형사 수사". Sky(uk#12)의 published는 11-01 17:16이다. 10-31 브리핑에 이미 피쉬본 n26 "알래스카 '방해 후보' 형사 수사"가 있다. 오늘 새로운 내용은 Handelsblatt(de#40)의 «Ermittlungen zu Senatswahl in Alaska bestätigt»(수사 확인) 정도다.
  - `top10[0].why`, `fields[forecast].phenomenon`, `by_country.jp[2]`: "사전투표 5천만 명 이상(테레비아사히)"는 11-01 브리핑 forecast에 "사전투표 5천만 명 돌파(한국경제TV 제목, 단일)"로 이미 있다.
  - `top10[7].why`: "중앙일보: 미국은 '중국 서해 강압'을 밝혔다"는 11-01 브리핑 hypothesis_check에 "미국의 중국 '서해 강압' 제기(SBS 단일)"로 이미 있다. 오늘 중앙일보가 나오면서 2개 매체가 됐다는 점만 새롭다.
  - `top10[2].why`: "동아일보는 독일 34개 도시 시위가 생활비 부담 완화·교육 재정 확대를 요구했다고 정리"는 10-31(현지) 시위 내용이다. 11-01 브리핑의 "독일 'Gen Z' 시위(30여 개 도시 수만 명)"와 같다.
- 수정안: 각 문장 끝에 "(10-31 브리핑 기보도)" 또는 "(11-01 브리핑 기보도 — 오늘은 ○○ 추가)"를 붙인다. Dong-A의 인텔 기사에 이미 붙인 방식과 같다. 서해 건은 "(11-01 SBS 단일 → 오늘 중앙일보로 2개 매체)"로 쓴다.

### 13. '완전 회복 예상'을 5개 매체에 귀속했다 (유형 1)
- 위치: `top10[0].why` "크리스 머피 상원의원은 뇌졸중으로 입원했고 완전 회복이 예상된다(CNN·AP·NYT·WaPo·ABC)"
- 원문: '완전 회복 예상'은 CNN(us#3) 제목에만 있다(«expected to make full recovery, his team says»). AP·WaPo·ABC는 입원 사실만, NYT는 «'Awake and Alert'»만 담고 있다.
- 수정안: "크리스 머피 상원의원이 뇌졸중으로 입원(CNN·AP·NYT·WaPo·ABC). 측근은 완전 회복을 예상(CNN), '의식 있고 또렷'(NYT)".

---

## [권고]

### R1. IRGC 유조선 주장의 '단일' 표기와 반복 여부
- 위치: `top10[1].why`, `by_country.uk[1].why`, `essence.derivation.decomposition`·`rebuild`, `hypothesis_check.support[1]`
- 원문: Reuters(uk#37) 제목 외에 RBC(ru#65)도 «Два нефтяных танкера подорвались на морской мине при движении по «несанкционированному маршруту»»라고 보도했다. 전달 매체는 2곳이고 원 출처는 IRGC 1곳이다. '비인가 항로'라는 IRGC의 프레임도 '메시지'로 읽을 만하다.
- 10-31 브리핑에 "이란 '유조선 3척 기뢰 피격'(AP)·IRGC '4척 화재'(Reuters)", 11-01 브리핑에 Haaretz의 '유조선 기뢰 피격 주장'이 있었다. 새 사건인지 같은 주장이 반복된 것인지는 원자료로 알 수 없다.
- 문안: "IRGC 해군 '비인가 항로의 유조선 2척 기뢰 폭발' 주장(Reuters·RBC 전달 — IRGC 단일 출처, 독립 확인 없음; 10-31·11-01에도 유사 주장)".

### R2. 이란 외무 발언의 상충을 함께 적기
- 위치: `fields[geopolitics].phenomenon`, `fishbone.links[2].logic`(n29→n26), `by_country.kr[2]`
- 원문: MBC(kr#15) '카타르 중재 협의 진전'(제목) vs FAZ(de#56) «Irans Außenminister: Keine Pläne für Gespräche mit den USA». FAZ의 "이집트, 새 확전의 막대한 결과 경고"도 걸프 우려 항목에 보탤 수 있다.
- 문안: link 2 logic에 "같은 날 FAZ 라이브블로그는 이란 외무장관이 '미국과 회담 계획 없다'고 했다고 전해 MBC 제목과 엇갈린다(둘 다 제목·요약 수준)"를 추가한다.

### R3. 불가리아 '친러 대통령 승리'의 무게를 낮추는 원문 정보 반영
- 위치: `top10[3].why`, `fields[geopolitics].counter`, `hypothesis_check.against[2]`
- 원문: WELT(de#38) 투표율 «nur bei 29 Prozent», Spiegel «Wählerbeteiligung war niedrig», SCMP(cn#31) «the largely ceremonial post», «acting president», n-tv «Bulgaren bestätigen Präsidentin im Amt»(현직 유지).
- 문안: counter에 "현직(권한대행) 유지라 새 균열이라기보다 연속이고, 투표율 29%(WELT), 대통령직은 주로 의례적(SCMP)"을 추가한다. 헤드라인의 '현직'은 "대통령 권한대행(SCMP·Interfax)" 표현과 맞춘다.

### R4. 스파이웨어 '사용 확인'은 ARD 표현임을 헤드라인에 표시
- 위치: `top10[5].headline_ko`
- 원문: ARD(de#3) «bestätigte… den Einsatz von Spyware». 다른 매체는 Spiegel «bestätigt den Hinweis», FAZ «bestätigt Hinweise auf möglicherweise kompromittierte Geräte», WELT «Bedrohungsbenachrichtigung für iPhones von Apple»이다. 다른 매체 기준으로는 '애플 위협 알림·감염 가능성 경고 확인'이다.
- 문안: "디지털장관, 애플 경고 확인(Spiegel·FAZ·WELT) — ARD는 '스파이웨어 사용 확인'으로 보도".

### R5. 억지 연결 교체: links n35→n32
- 위치: `fishbone.links[7]`
- 문제: FSB의 테러 용의자 구금(러시아)과 불가리아 대선은 나라도 행위자도 다르다. logic 스스로 "접근 신호로는 약하다"고 인정한다.
- 문안: n33(올레시키 휴전 — 미국 중재, Kommersant·FAZ)과 n35(미국 제보·FSB 감사, CNN·산케이·Handelsblatt)를 잇는다. "미·러 사이에 휴전 중재와 테러 정보 공유라는 실무 채널이 같은 주에 작동(🔎 해석; 2024 크로커스 선례상 정보 공유 자체는 관행)".

### R6. 본질 헤드라인의 단정 표현과 연속성 표시
- 위치: `essence.headline`, `fishbone.head`
- 문제: "두 결정이 같은 날짜에 묶였다"는 해석인데 사실처럼 단정했다. 트럼프 '유보적'(연합)·'외교 우선'(Le Figaro의 Axios 인용)과도 긴장이 있다. '선거 뒤 결정' 구도는 11-01 본질에도 이미 있다("미국의 결정이 중간선거 뒤로 밀려 있다고 본다"). 한국 독자에게 "국내에선"은 한국으로 읽힌다.
- 문안: "…이란 재공격 결정이 선거 뒤로 미뤄져 있다는 보도가 이어졌다(11-01부터) — …", "국내에선" → "미국 안에선".

### R7. SMIC 인상의 '원인'을 제목에서 추론하지 말 것
- 위치: `fields[monetary].cause` "SMIC 인상 전망은 사회적 긴장(Les Echos 제목)"
- 원문: Les Echos(fr#44) «Semaine sociale à haut risque pour le gouvernement, coup de pouce significatif en vue sur le SMIC». 두 사실을 나란히 적었을 뿐 인과는 쓰지 않았다.
- 문안: "Les Echos 제목은 '고위험 사회 주간'과 SMIC 인상 전망을 나란히 적었다. 🔎 시위 대응용 인상으로 보는 것은 해석".

### R8. 시점 표기 정리 (일요일·주간 누적)
- 위치: `fields[stocks].phenomenon`, `top10[6].why`
- 문제:
  - "오늘(일요일)은 주식 거래일이 아니다"에서 브리핑 날짜(11-02 월, KST)와 원자료 구간(현지 11-01 일)이 섞여 있다. "원자료 구간(현지 11월 1일 일요일)은 주식·채권 거래가 없다"로 바꾼다.
  - FT 정크본드(uk#46, 11-01 23:54 일요일 발행)는 그 전 거래일까지 누적된 매도세 기사다.
  - TV도쿄 '코어위브 쇼크'(jp#46, 11-01 18:31)는 평일 프로그램(모닝새틀라이트)을 일요일에 업로드한 것이라 쇼크 시점을 알 수 없다. "(방송 시점 미확인)"을 붙인다.

### R9. 도브린트 발언 전체 반영
- 위치: `top10[2].why`, `fields[legislation].phenomenon`, `by_country.de[0]`
- 원문: WELT(de#32) «dass linke Gruppen und „migrantische Chaoten" … verantwortlich sind», The Times(uk#65)·MBC(kr#12) '극좌 세력·이주민 배경 말썽꾼'. 초안은 '이주민'만 적어 발언을 좁혔다.
- 문안: "도브린트가 소요를 좌파 그룹과 '이주민 난동꾼' 탓으로 돌리자(WELT·The Times·MBC; ZDF·n-tv는 이주민 부분)…".

### R10. 배경 사례 표현 정밀화
- 위치: `fields[business].precedent` "2023년 애플의 국가 지원 공격 경고 알림"
- 🔎 검토자 배경지식: 애플의 위협 알림은 2021년에 시작됐다. 2023년(10월)은 인도 야당 정치인들에게 대량 발송된 사례다. 문안: "2021년 도입된 애플의 국가 배후 공격 경고(2023년 인도 야당 정치인 대량 수신)". 나머지 precedent(로닌 2022·바이비트 2025 FBI 지목, 1998 사막의 여우 = 중간선거 약 6주 뒤, 2016 라데프, 2019 반폭도법, 2023년 8월 리펀딩 뒤 장기금리 상승, 2024 크로커스 경고)는 사실관계상 문제를 찾지 못했다.

### R11. 관련 없는 내용 섞임
- 위치: `top10[6].why` 끝 "Fox(호퍼 인용): 높은 항공유 가격에 연말 항공료 10년 만에 최고"
- 문제: AI·신용 경고 항목에 항공료가 들어가 논지가 흐려진다. industry 분야(n1)에 이미 있으니 top10[6]에서는 뺀다.

---

## 잘 된 점 (유지)
- 국영매체 표기는 7번(by_country.ru[4] 헤드라인) 한 곳을 빼면 모두 붙어 있다(TASS·Vesti·RIA·Xinhua·인민일보·China Daily).
- 단일 출처 표기(France 24 '연장 거부', FT 정크본드, 산케이 방위비, DW 가스, Fox 항공료, SBS 공군)와 판정 근거 제외 원칙을 대체로 지켰다.
- 동아일보 인텔 기사의 10-31 기보도 표기, forecast의 '지난 브리핑 보도' 표기, 피쉬본 links의 "직접 인과를 잇는 원문은 없음" 단서 같은 처리는 좋다. 같은 방식을 12번 지적에도 적용하면 된다.

---

## 집계
- [필수 수정]: 13건 (1 Axios 귀속, 2 Spiegel 인용 귀속, 3 FBI 단일 오표기·바이낸스 시장 충격 누락, 4 일본은행 구기사, 5 인터폴 구기사, 6 WSJ 유가 시점, 7 RIA 관영 미표기, 8 단일 출처의 판정 근거 혼입, 9 도네츠크 원인 추가, 10 판정 '유지' 논리, 11 Economist 오독, 12 기보도 미표기, 13 머피 귀속)
- [권고]: 11건 (R1–R11)

판정: 수정 필요

---

## 반영 결과 (임원 최종)

- [필수 수정] 13건 전부 반영: Axios 귀속을 Vedomosti로 한정(연합·한국경제TV는 원 출처 미기재, Le Figaro는 '외교 우선'만), Spiegel 인용 단독 표기, FBI 지목 동아·SCMP 2개 매체로 정정하고 SCMP 36.4억$ 인출·Kommersant 비트코인 하락 추가('지난달 29일' 삭제), 일본은행 '동결 전망' 제외, 인터폴 구기사 제외(루비오 동아 기사로 교체), WSJ 유가 시점 미확인 표기, RIA 관영 표기·WELT 51% 추가, JPost 소식통을 단일 묶음으로 이동, 도네츠크 원인 미기재·'양측 공방' 삭제, 판정 '약화'로 되돌림(7회 연속), Economist 제목 정정, 기보도 표기(Sky 수사·사전투표·서해·독일 34개 도시), 머피 '완전 회복' CNN 귀속.
- [권고] 11건 반영: IRGC 유조선 단일 출처·RBC 추가, FAZ '회담 계획 없음' 병기, 불가리아 투표율 29%·의례적 직위·권한대행, 스파이웨어 표현 구분, 링크 n35→n32를 n33→n35로 교체(+n11→n12 추가), 본질 헤드라인 단정 완화·'미국 안에선', SMIC 인과 해석 표기, 일요일 시점 표기, 도브린트 '좌파 그룹' 포함, 애플 경고 선례 정정, top10[6]에서 항공료 제거.
- `python template/verify.py 2026-11-02` 재통과.
