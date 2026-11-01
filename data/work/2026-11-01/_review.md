# 2026-11-01 브리핑 초안 검토 (팀장 → 임원)

- 대상: `briefings/2026-11-01.json` (generated_at 2026-11-01 06:24 KST)
- 대조 기준: `data/raw/2026-11-01/<팀>.json`의 title_original / summary_original / published. 보조로 work 번역본, `_lead.json`, 이전 브리핑(10-26~10-31)
- `python template/verify.py 2026-11-01` 결과: **검증 통과: 선별 뉴스 55건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상** (URL 157개 모두 원자료에서 찾음)
- 누락 점검: `_lead.json` TOP 10 10건, 국가별 45건이 브리핑에 모두 그대로 들어 있음 (누락 없음)
- 시점 확인: 10-31(현지)은 토요일이라 미국 주식·원유 모두 새 거래일이 없음. 원자료에 새 지수·유가 수치 없음 (fields.stocks.phenomenon에 이를 밝힌 것은 적절)

---

## [필수 수정]

### 1. [필수 수정] 이전 날짜 WSJ 유가 기사를 오늘 유가의 원인처럼 씀 (오류 유형 2·7)
- 위치: top10[1].why ("유가: WSJ '미국의 외교 재개 모색에 유가 하락'(제목)"), by_country.us[0].why·sources(WSJ), essence.derivation.decomposition ("유가 하락(WSJ 제목)")
- 문제: 같은 WSJ 기사(URL `…CBMiogFBVV95cUxNTW53UkVQVFpV…`)가 **10-30 브리핑에 이미 출처로 실렸다** ("WTI는 외교 해결 기대감에 102달러로 내렸다(MBC·YTN; WSJ '외교 재개 모색에 유가 하락')"). 오늘 원자료의 published 05:31 KST는 Google News가 날짜를 다시 매긴 것일 뿐이다. 그리고 10-31(토)은 원유 거래가 없는 날이다. 지금 문안은 토요일 루비오의 '외교 선호' 발언 바로 뒤에 놓여 있어서, 그 발언 때문에 유가가 내린 것처럼 읽힌다. 10-31 브리핑은 오히려 '유가 상승(WSJ)'이라고 적었다.
- 원문 근거: WSJ "Oil Prices Ease as U.S. Seeks to Renew Diplomacy With Iran" (요약 없음, 10-30 work/브리핑에 같은 URL 있음)
- 고칠 문안: top10[1].why와 essence.derivation.decomposition에서 유가 문장을 지운다. 남기려면 "(참고: WSJ '외교 재개 모색에 유가 하락'은 10-29 기사의 재노출로 10-30 브리핑에 이미 실림. 토요일은 거래가 없어 오늘의 가격 정보가 아님)"로 바꾼다. by_country.us[0]의 sources와 why에서도 WSJ를 뺀다.

### 2. [필수 수정] RBC 단독 'NPT 탈퇴 검토'에 단일 표기가 없고, 시점을 새 발언처럼 씀 (유형 4·5)
- 위치: top10[1].why ("RBC는 이란 의회에서 … NPT 탈퇴 제안을 검토하겠다는 발언이 나왔다고 전했다"), fields.geopolitics.phenomenon ("이란 의회 'NPT 탈퇴 검토' 발언(RBC)"), hypothesis_check.support[0] ("이란 의회의 NPT 탈퇴 검토 발언(RBC)"), by_country.ru[4].headline
- 문제: 원자료 전체에서 RBC 한 곳만 다룬다. 게다가 원문 동사는 과거형 "заявляли"(그동안 ~라고 말해 왔다)라서 오늘 새로 나온 발언으로 확인되지 않는다. 그런데도 가설 '지지' 근거 목록에 단일 표기 없이 들어가 있다. 같은 RBC 요약의 반대 방향 문장("Тегеран подтвердил попытку властей США наладить переговоры" — 테헤란이 미국의 협상 시도를 확인)은 빠졌다.
- 원문 근거: RBC "В Иране допустили пересмотр ядерной доктрины…" / "Иран остается участником ДНЯО, однако в иранском парламенте заявляли, что рассмотрят предложение о выходе…"
- 고칠 문안: "RBC(단일·미확인)는 이란이 NPT 회원국으로 남아 있지만, 이란 의회에서 전쟁이 재개되면 탈퇴 제안을 검토하겠다는 발언이 있었다고 전했다(발언 시점 불명). 같은 기사는 테헤란이 미국의 협상 시도를 확인했다고도 썼다." support[0]에는 "(RBC 단일·미확인 — 판정 근거 제외)"를 붙인다.

### 3. [필수 수정] 관영 매체만 전한 '키이우 폭발'을 헤드라인·가설 근거에 사실처럼 씀. '같은 날'은 원문에 없음 (유형 3·4·6)
- 위치: top10[9].headline_ko ("같은 날 에너지 시설 피격·키이우 폭발"), top10[9].why ("반대 신호: … 키이우 폭발(TASS·RIA 관영)"), hypothesis_check.support[0] ("키이우 폭발(TASS·RIA 관영)")
- 문제: 키이우 폭발은 TASS·RIA(둘 다 state_media=true)의 제목뿐이고, 비관영 매체의 확인이 원자료에 없다. 관영 보도를 "메시지"로 읽지 않고 헤드라인 사실로 올렸다. Meduza의 정전 기사는 전쟁 1711일째 일일 정리라서 공격이 대피 완료와 '같은 날'인지 확인되지 않는다.
- 원문 근거: TASS "В Киеве произошли взрывы"(요약 없음), RIA "В Киеве вновь прогремели взрывы"(요약 없음), Meduza "Война. 1711-й день. … После российских ударов по энергетике тысячи семей в стране остались без света"
- 고칠 문안: 헤드라인은 "올레시키 대피 완료 — Meduza '2022년 이후 최장 휴전', 러 에너지 공격 뒤 수천 가구 정전(Meduza)"로 고친다. why에는 "[메시지] 러 관영 TASS·RIA는 키이우 폭발을 보도(제목만, 비관영 확인 없음)"로 쓴다. support[0]에서는 키이우 폭발을 빼거나 "(관영 단독·미확인, 판정 근거 제외)"로 표시한다.

### 4. [필수 수정] Le Monde 한 매체의 표현을 두 매체에 귀속하고, 독일 시위를 '유럽 청년층'으로 넓혀 가설 균열의 근거로 씀 (유형 1·5)
- 위치: hypothesis_check.against[2] ("징병 거부·'전쟁 대신 사회 시스템에 돈을'(Le Monde·Le Figaro)"), hypothesis_check.note ("새로 보인 균열은 유럽 청년층의 징병·전쟁 비용 거부(Le Monde·Le Figaro)")
- 문제: 따옴표 문구 "De l'argent pour les systèmes sociaux plutôt que pour la guerre"는 Le Monde 제목에만 있다. Le Figaro는 반대 항목으로 '병역(service militaire)'을 나열할 뿐 '전쟁 비용' 표현은 없고, 동원이 "기대 이하"라고 썼다. 독일 매체 ARD·ZDF·WELT 요약에는 징병 언급이 없다. 프랑스 시위의 요구는 생활비(vie chère)다. '유럽 청년층의 전쟁 비용 거부'는 원자료가 말하는 범위를 넘는다.
- 원문 근거: Le Monde "« De l'argent pour les systèmes sociaux plutôt que pour la guerre » : … manifestants hostiles au service militaire" / Le Figaro "contre la cherté de la vie, le service militaire, les coupes sociales … la mobilisation est néanmoins en deçà des attentes" / ARD "Bessere Bildung, mehr Klimaschutz und bezahlbarer Wohnraum"
- 고칠 문안: against[2]는 "가설 균열(약한 신호) — 독일 청년 시위 요구에 병역 반대 포함(Le Monde·Le Figaro; '전쟁 대신 사회 시스템에 돈을'은 Le Monde 제목). 독일 공영방송(ARD)의 요구 목록은 교육·기후·주거이고, Le Figaro는 동원이 기대 이하라고 함 — 중심 요구는 생활비·교육."로 고친다. note의 "유럽 청년층의 징병·전쟁 비용 거부"는 "독일 청년 시위 일부의 병역 반대"로 좁힌다.

### 5. [필수 수정] 배경 사례의 사실 오류: 2011년 S&P '프랑스 강등' (유형 8)
- 위치: fields.monetary.precedent ("2011년 S&P의 미국·프랑스 등급 강등과 안전자산 이동")
- 문제: S&P의 미국 강등은 2011년 8월이 맞다. 하지만 프랑스의 AAA 박탈은 **2012년 1월**이다(2011년 11월에는 S&P가 강등 메시지를 실수로 내보낸 해프닝만 있었다). 또 2011년 미국 강등 뒤에는 오히려 미 국채로 돈이 몰렸다. 이 사례를 '등급 압박 → 안전자산 이탈'의 선례로 쓰려면 방향을 밝혀야 한다.
- 고칠 문안: "🔎 2011년 8월 S&P의 미국 강등(강등에도 미 국채로 자금 유입), 2012년 1월 S&P의 프랑스 AAA 박탈(이후 프랑스-독일 스프레드 확대)"

### 6. [필수 수정] 배경 사례의 사실 오류: '2018년 중간선거 직후 대중 관세 확대' (유형 8)
- 위치: fields.forecast.precedent
- 문제: 2018년 11월 6일 중간선거 직후에 나온 것은 12월 1일 부에노스아이레스 미·중 정상회담의 **휴전**이다(1월 1일 예정이던 25% 인상을 유예). 관세 인상은 2019년 5월에 실행됐다. 선거 뒤 강경책이 나온다는 시나리오의 근거로 쓰면 사실과 반대다. 1998년 '사막의 여우'(11월 3일 선거, 12월 16~19일 공습)는 맞다.
- 고칠 문안: "🔎 1998년 중간선거 6주 뒤 이라크 '사막의 여우' 공습. 반대 사례: 2018년 중간선거 직후 미·중은 관세 인상을 유예하는 휴전(12월 1일)에 합의했고 인상은 2019년 5월에 실행됨 — 선거 후 결정이 강경으로 간다는 보장은 없다."

### 7. [필수 수정] 배경 사례의 사실 오류: '닷컴 붕괴 때도 메모리·통신 장비 수요는 한동안 유지' (유형 8)
- 위치: fields.industry.precedent (이 선례가 fields.industry.essence "돈은 흔들려도 물건(메모리)은 아직 돈다"를 받치고 있음)
- 문제: 2000~01년에는 DRAM 가격이 2000년 하반기부터 급락했다. 2001년 세계 반도체 매출은 약 3분의 1(약 32%) 줄었고, 통신 장비 주문도 2001년에 무너졌다. 즉 이 선례는 '자금이 식으면 몇 달 뒤 하드웨어 수요가 꺾인다'는 반대 근거다. 지금 문안은 선례를 거꾸로 쓰고 있다.
- 고칠 문안: precedent는 "🔎 2000~01년 닷컴 붕괴: 주가 하락 뒤 수개월 시차로 DRAM 가격·통신 장비 주문이 급감(2001년 세계 반도체 매출 약 3분의 1 감소)"로 고친다. essence 끝에 "— 다만 닷컴기의 시차는 몇 달이었다"를 붙이고, counter에도 이 선례를 넣는다.

### 8. [필수 수정] 본질 헤드라인이 해석("결정은 중간선거 뒤로 밀려 있다")을 사실로 단정 (리뷰 3항 사실/해석 분리)
- 위치: essence.headline 마지막 문장
- 문제: 루비오의 말은 "아직 결정하지 않았다"(CBS·MBC·Haaretz)이지 "선거 뒤로 미뤘다"가 아니다. '중간선거 뒤 공습 위협'은 Reuters·Ynet의 전망 표현이다. 루비오 본인은 "중간선거가 외교 노선에 큰 영향을 주지 않을 것"이라고 했다(Interfax). fields.forecast.essence에는 "(보도 기준)"이 붙어 있는데 헤드라인에는 없다.
- 원문 근거: CBS "no decision has yet been made on whether to renew hostilities" / Reuters "threat looms of US strikes after midterms" / Interfax "Промежуточные выборы … не окажут существенного влияния на внешнеполитический курс"
- 고칠 문안: "… 루비오는 공격 재개를 아직 결정하지 않았다며 외교를 말했다 — Reuters·Ynet은 공습 위협 시점을 중간선거 뒤로 본다(🔎 보도 기준; 루비오는 '선거 영향은 작다')."

---

## [권고]

### 9. [권고] 금 1년 만의 저가·일본 2% '도달'은 10-31 브리핑에 이미 실린 사건 (유형 7)
- 위치: fishbone n15·n17, fields.monetary.phenomenon, top10[2].why (니혼게이자이 금), by_country.jp[2]·jp[3], fields.monetary.counter ("금 저가 … 단일 출처")
- 문제: 10-31 브리핑에 이미 n19 "일본은행 물가 2% '도달'"(마이니치), n21 "금·은 1년래 최저"(Handelsblatt; Xinhua 관영)가 있다. 오늘 자료는 그 후속 해설(닛케이)과 사설(산케이)인데, 새 뉴스처럼 실렸다. counter의 "금 저가는 단일 출처"도 어제 기준으로는 복수 보도라 맞지 않다.
- 고칠 문안: 라벨을 "금 1년 저가 지속(닛케이 해설 — 10-31 기보도)", "산케이 사설 '2% 도달'(10-31 기보도 사건 평가)"로 바꾼다. counter는 "금 저가는 10-31 복수 보도의 연장이고, 오늘 새 정보는 닛케이의 '선거 후 유가 상승 경계'뿐"으로 고친다.

### 10. [권고] 베네수엘라 석유 기사: 'Japan Times 단일'이 아니라 전날 Reuters 기사의 전재이고, 가설 '지지' 표시는 기사 방향과 반대 (유형 5·7)
- 위치: fields.industry.phenomenon·counter, by_country.jp[4] (hypothesis "지지"), hypothesis_check.support[3], fishbone n4
- 문제: 같은 제목 "Trump touted a record Venezuela oil deal. Now reality is setting in"이 10-31 원자료 uk.json에 Reuters 기사로 있다(published 10-31 07:01 KST). 오늘 것은 Japan Times의 전재(10-31 17:13)다. 기사는 무명 업체 몫이 됐다는 '현실 점검' 기사라서 에너지 이익 '지지' 근거가 되기 어렵다. support[3]도 스스로 "오히려 의문 제기 기사"라고 쓰고 있다.
- 고칠 문안: 출처 표기를 "Reuters 기사(Japan Times 전재, 전날 보도)"로 바꾼다. by_country.jp[4].hypothesis는 "무관"으로 하고, support[3]은 against로 옮기거나 지운다.

### 11. [권고] by_country.ru[2]의 Kommersant 출처는 전날 수집분 (유형 7)
- 위치: by_country.ru[2].sources (Kommersant "Эвакуация из херсонских Алешек прошла без инцидентов")
- 문제: published 2026-10-31T06:57 KST로 10-31 원자료에도 있고, 내용도 "30 октября состоялся основной этап"(30일 본 단계)다. 대피 완료는 Meduza·Vedomosti(11-01)로 충분히 뒷받침된다.
- 고칠 문안: 출처에서 빼거나 why에 "Kommersant(10-30 본 단계, 전날 보도)"로 표시한다.

### 12. [권고] 하메네이 발언의 전달 경로 단서(DW 'soll')가 빠짐 (유형 5)
- 위치: top10[1].why, fields.geopolitics.phenomenon, hypothesis_check.support[0], fishbone n28
- 문제: DW는 "공개 석상에 나타나지 않는 최고지도자가 발언했다고 한다(soll gesprochen haben)"며 단서를 달았다. 경향의 로이터 인용은 '공식 텔레그램 계정'을 통한 발표라고 했다. 지금 문안은 '지시했다'로만 단정한다.
- 고칠 문안: "모즈타바 하메네이 최고지도자 명의로(공식 텔레그램 — 경향의 로이터 인용; DW는 '발언했다고 한다') … 반격을 지시했다"

### 13. [권고] links n5→n9의 방향이 시간·인과와 반대
- 위치: fishbone.links[2] (n5 오픈AI 목표 삭감 → n9 Bloomberg 'AI 열기 붕괴')
- 문제: CNBC의 FT 인용 제목은 "slashes funding target … **amid tech rout**"로, 하락장 속에서 목표를 줄였다는 뜻이다. Bloomberg 기사(10-31 22:00 KST)는 CNBC의 FT 인용 기사(11-01 01:08 KST)보다 먼저 나왔다. 화살표가 '삭감 → 열기 붕괴'로 읽힌다.
- 고칠 문안: from n9 → to n5로 뒤집고, logic을 "FT(CNBC 인용)는 오픈AI가 기술주 급락 속에 목표를 줄였다고 썼다 — 시장 냉각이 조달 조건으로 번진 연결"로 고친다.

### 14. [권고] Vedomosti 귀속과 '관영' 표기 범위가 모호 (유형 1·3)
- 위치: essence.derivation.decomposition·top10[4].why·fields.geopolitics.phenomenon·hypothesis_check.against[4]의 "루비오 '우크라이나 해결 임박 아님'(RBC·Vedomosti·Vesti 관영)" 또는 "(RBC; Vedomosti·Vesti 관영)"
- 문제: Vedomosti 원문은 제목 "Рубио уточнил позицию США по возможности скорого достижения сделки по Украине"(입장 명확화)뿐이고 '임박 아님' 내용은 없다. "Vedomosti·Vesti 관영"은 Vedomosti(state_media=false)까지 관영으로 읽힌다.
- 고칠 문안: "(RBC; [관영] Vesti; Vedomosti는 제목만 '입장 명확화')"

### 15. [권고] 칼라스 발언의 '위험(may)'을 단정으로 씀 (유형 5)
- 위치: fields.geopolitics.phenomenon ("칼라스 '푸틴 G20 초청은 전쟁범죄 정상화'(Bloomberg)")
- 원문 근거: Bloomberg "Hosting Putin at G20 **May** Normalize War Crimes" / "would risk regularizing Russia's return"
- 고칠 문안: "칼라스 '푸틴의 G20 참석은 전쟁범죄를 정상화할 위험'(Bloomberg)" (top10[4].why의 문안은 맞음)

### 16. [권고] 대중 포위선 지지 근거에 반대 방향 정보가 섞이고, 같은 기사의 반박 신호가 누락 (리뷰 4항)
- 위치: hypothesis_check.support[1] (쿼드 정상회의 준비), hypothesis_check.against
- 문제: 루비오는 "쿼드는 반중이 아니다"라고 했다. 같은 SCMP 기사는 "몇 주 뒤 트럼프가 선전에서 시진핑과 만날 예정"이라고 썼는데, 이것은 포위선 가설의 반박 신호인데도 어디에도 없다.
- 원문 근거: SCMP "Quad not 'anti-China', says Rubio as first summit in two years set before Trump-Xi talks … just weeks before … meet Chinese leader Xi Jinping in Shenzhen"
- 고칠 문안: support[1]에서 쿼드를 빼거나 "(루비오는 '반중 아냐')"를 앞세운다. against에 "미·중 접촉: 트럼프-시진핑 선전 회담 예정(SCMP 단일)"을 추가한다.

### 17. [권고] 이란 축의 단일 출처 반대·긴장 신호 누락 (리뷰 4항)
- 위치: fields.geopolitics.counter, hypothesis_check.against[1]
- 문제: Handelsblatt 뉴스블로그에는 "Iran: US-Angriff auf Fischerboote nahe Insel Keschm"(이란 측의 '케슘섬 인근 어선 미국 공격' 주장)이 있다. '외교 선호'와 반대 방향인 긴장 신호인데 빠졌다. 반대로 RBC의 "테헤란, 미국의 협상 시도 확인"(2번 항목)은 외교 쪽 신호다. 둘 다 단일 출처지만 반박 점검표에는 '단일'로 표시해 올리는 것이 원칙이다.
- 고칠 문안: counter에 "Handelsblatt(뉴스블로그, 단일)는 이란이 케슘섬 인근 어선에 대한 미국 공격을 주장했다고 전했다"를 추가한다.

### 18. [권고] 가설 태그(hypothesis)의 일관성
- 위치: top10[0] "무관" (그런데 against[2]가 같은 시위를 가설 균열로 씀), by_country.fr[3] 경유 인하 "지지"(근거 설명 없음), by_country.de[4] 후티 억류 유엔 직원 사망 "지지"(분쟁 장기화와의 연결 설명 없음; 원문 n-tv는 "zu Tode gefoltert", Handelsblatt도 "tot" 보도라 단일도 아님), by_country.cn[2] China Daily(관영) 해경 순찰 "지지"(관영 메시지는 사실 판단 유보 대상)
- 고칠 문안: top10[0]은 "반박"(약한 신호)으로 맞춘다. fr[3]·de[4]는 "무관"으로 한다. cn[2]는 "무관"으로 하거나 why에 "[메시지] — 판정 근거 아님"을 명시한다. support[0]의 "후티 억류 유엔 직원 사망(n-tv)"은 "(n-tv·Handelsblatt)"로 고친다.

### 19. [권고] 바이낸스 본질 문장이 원인 문장과 충돌
- 위치: fields.crypto.essence ("이틀 만에 손실 대부분을 메울 만큼 자본이 있다")
- 문제: 같은 분야의 cause는 "보전 재원·방법은 원자료에 없다"고, counter는 "'담보 복구'가 전액 반환과 같은지 미확인"이라고 쓴다. 원문은 "restored backing for 90% of assets affected"(CNBC)뿐이다. '자본이 있다'는 재원을 단정한다.
- 고칠 문안: "🔎 최대 거래소는 해킹 하루 남짓 만에 피해 자산의 90%에 대한 담보를 복구했다고 밝혔다(재원은 미공개) — 위기는 '지급 불능'보다 '보안 신뢰' 쪽으로 좁혀지고 있다(출금 재개 이행이 시험대)."

### 20. [권고] '학생 단체 11월 5일 파업 예고'는 원문과 다름 (유형 5)
- 위치: essence.derivation.decomposition, top10[0].why ("11월 5일 파업을 호소했다"), fields.legislation.phenomenon, fields.forecast.phenomenon, fishbone n27, by_country.fr[0].headline_ko
- 원문 근거: Le Figaro "Elles appellent déjà à bloquer facs et lycées dès mardi, **avant la grève du 5 novembre**" — 학생 단체가 호소한 것은 화요일부터의 대학·고교 봉쇄다. 11월 5일 파업은 이미 잡혀 있는 일정으로 쓰였고, 누가 소집했는지는 원문에 없다.
- 고칠 문안: "학생 단체는 50만 명을 주장하며 11월 5일 파업에 앞서 화요일부터 대학·고교 봉쇄를 호소했다(Le Figaro)". n27은 "프랑스 11월 5일 파업 일정(봉쇄 호소)"으로 바꾼다.

### 21. [권고] 피치 조치의 '계기'는 원문이 시간 순서로만 씀 (유형 6)
- 위치: fields.monetary.cause ("피치 조치의 계기는 예상 밖 3분기 역성장(FT)")
- 원문 근거: FT "Move comes **hours after** data showed an unexpected contraction"
- 고칠 문안: "피치 조치는 예상 밖 3분기 역성장 지표 몇 시간 뒤에 나왔다(FT 단일 — 🔎 계기로 보는 것은 해석)"

### 22. [권고] 배경 사례의 세부 부정확: 중국계 통신사 퇴출 연도
- 위치: fields.business.precedent ("2019~20년 화웨이·차이나텔레콤의 미국 사업 퇴출")
- 문제: 차이나텔레콤 아메리카는 2020년 4월 FCC 소명 명령(Order to Show Cause)을 받았고 2021년 10월 면허가 취소됐다. 차이나유니콤 아메리카는 2022년 1월에 취소됐다. HKT가 받은 '소명 명령'과 같은 절차라서 연도를 바로잡으면 선례가 더 정확해진다.
- 고칠 문안: "🔎 2020년 FCC 소명 명령 → 2021년 10월 차이나텔레콤 아메리카 면허 취소, 2022년 1월 차이나유니콤 아메리카 취소"

### 23. [권고] 배경 사례의 세부 부정확: 닷컴 정점 시점
- 위치: fields.stocks.precedent ("2000년 4월 닷컴 정점 직후")
- 문제: 나스닥 정점은 2000년 3월 10일이다(4월은 급락기).
- 고칠 문안: "🔎 2000년 3월 닷컴 정점 이후 성장주→채권 이동"

### 24. [권고] '테러 경고 공유'를 미·러 접촉 신호로 읽는 것은 같은 브리핑의 선례와 충돌
- 위치: hypothesis_check.against[4] ("주모스크바 미 대사관의 테러 위협 경고를 FSB가 수신 확인 — 접촉 신호")
- 문제: fields.geopolitics.precedent가 든 2024년 크로커스 사례처럼, 미국은 적대 관계에서도 '경고 의무' 관행으로 테러 정보를 공개·전달해 왔다. 원문(Meduza)도 대사관 웹사이트의 공개 경고와 FSB의 수신 확인만 전한다. 거래·접근의 신호로 쓰기에는 약하다.
- 고칠 문안: "(🔎 테러 경고 공유는 2024년 크로커스 때처럼 적대 관계에서도 이뤄지는 관행이라 접근 신호로는 약함)"을 덧붙이거나, 대안 가설 근거에서 뺀다.

### 25. [권고] 판정 연속 횟수 표기
- 위치: hypothesis_check.note ("직전 브리핑 10-31과 같음, 닷새째")
- 문제: 10-26·10-28·10-29·10-30·10-31·11-01 브리핑이 모두 '약화'라서 오늘이 여섯 번째 연속이다.
- 고칠 문안: "(10-26 이후 6회 연속 '약화')"

### 26. [권고] 출처 귀속 세부
- top10[0].why "프랑크푸르트 … 약탈과 경찰관 부상(n-tv·FAZ·WELT·Handelsblatt)": 인용한 WELT(de:35 "Demonstrationen in 34 Städten")에는 프랑크푸르트 언급이 없다. 프랑크푸르트 약탈은 WELT 다른 기사(de:32 "Plünderszenen in Frankfurt")에 있으니 그 기사를 출처에 넣거나 WELT를 뺀다.
- top10[4].why "CNBC·SCMP: … 공동성명 대신 의장 성명": 의장 성명은 CNBC 요약에만 있다(SCMP는 '합의 없이 종료'와 핵심 광물). "합의 없이 종료(CNBC·SCMP), 의장 성명으로 대체(CNBC)"로 나눈다.

---

## 집계
- [필수 수정] 8건 (1 이전 날짜 WSJ 유가, 2 RBC NPT 단일·시점, 3 관영 단독 키이우 폭발, 4 Le Monde 표현 귀속·과장, 5~7 배경 사례 사실 오류 3건, 8 본질 헤드라인 해석 단정)
- [권고] 18건 (9~26)
- 유형별: 1(다매체 귀속) 3건 / 2(장 마감·거래일) 1건 / 3(관영) 2건 / 4(단일 출처) 2건 / 5(과장·반대 읽기) 6건 / 6(원인 추가) 2건 / 7(전날·기보도) 4건 / 8(해석·반박·선례) 9건 (중복 포함)

판정: 수정 필요

---

## 반영 결과 (임원 최종)

- [필수 수정] 8건 전부 반영:
  1. WSJ 유가 기사(10-30 기보도) 제거 — top10[1]·us[0]·분해, 토요일이라 유가 정보 없음을 명시
  2. RBC NPT 발언 '단일·시점 미기재' 표기, 판정 근거에서 제외
  3. 키이우 폭발은 [메시지](관영 제목)로 낮추고 '같은 날' 삭제
  4. '전쟁 대신 사회 시스템에 돈을'은 Le Monde 단일로 귀속, 가설 균열은 '약한 균열·간접 증거'로 낮춤
  5. 2012년 1월 프랑스 AAA 박탈로 정정
  6. 2018년 중간선거 뒤 12월 1일 관세 휴전으로 정정
  7. 2001년 DRAM 폭락(반대 방향 선례)으로 정정
  8. 본질 헤드라인의 '선거 뒤 결정'은 매체 관측으로 표기(루비오 반대 발언 병기)
- [권고] 18건 반영(9~26): 기보도 표기, 베네수엘라 기사 Reuters 전재·태그 무관, Kommersant 제외, DW 단서, 링크 n9→n5로 뒤집음, Vedomosti·관영 범위, 칼라스 '위험', 트럼프-시진핑 회담 예정 반박 추가, 케슘섬 어선 주장 추가, 가설 태그 정리, 바이낸스 본질 문장, 11월 5일 파업 문안, 피치 '계기' 해석 표기, 통신사 퇴출 연도, 닷컴 정점 3월, 테러 경고 공유 단서, 6회 연속, 출처 귀속 세부(WELT de:32 추가·의장 성명 CNBC).
- 판정 '약화' 유지 — note에 소식통·단일 항목을 뺀 근거로 다시 설명.
- `python template/verify.py 2026-11-01` 재통과.
