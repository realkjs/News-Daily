# 2026-10-30 임원 초안 검토 (팀장, 검토 모드)

검토 대상: `briefings/2026-10-30.json` (generated_at 2026-10-30 06:27 KST)
대조 자료: `data/work/2026-10-30/_lead.json`, `data/work/2026-10-30/<국가>.json`(9개), `data/raw/2026-10-30/<국가>.json`(9개, title_original/summary_original 기준).
시각 표기: 원자료 `published`(KST) 기준. 미 동부(EDT)는 KST−13시간. NYMEX 원유 정산은 14:30 EDT, 즉 03:30 KST다.

## 0. verify.py 결과

```
$ python3 template/verify.py 2026-10-30
검증 통과: 선별 뉴스 55건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상
```

- URL 존재 여부와 피쉬본 구조는 통과했다(노드 41개, 8개 분야 모두 있음). verify.py는 문장 속 괄호 매체명이 그 매체 기사 내용과 맞는지는 보지 않는다. 아래 지적은 대부분 그 부분이다.
- `top10`과 `by_country`는 `_lead.json`과 필드 단위로 같다(10건 모두 포함, 누락 없음). 아래에서 top10/by_country를 짚은 곳은 팀장 작성분의 오류다. 임원 문장과 같은 오류가 반복된 곳이라 함께 고친다.

**지난 이틀 반복 오류 유형 점검**

| 유형 | 오늘 |
|---|---|
| 매체 귀속 부풀리기 | 반복(1-2, 1-3, 1-4). 다만 건수와 정도는 줄었다 |
| 시점·나라가 맞지 않는 인과 | 반복(2-1 유가와 유조선 피격 주장의 선후) |
| 원자료에 없는 원인 추가 | 반복(1-5 'AI가 메모리를 빨아들여', 2-2 다크 탱커를 대러 제재 완화로 읽음) |
| 단일 출처를 판정 근거로 사용 | 일부 반복(1-3: 슈타인마이어 비판을 '복수 출처 지지'로 셈) |
| 원문을 거꾸로 읽음 | 반복(3-1 알래스카 수사를 '양당 대상'으로 씀) |
| 관영 '메시지' 표기 | 누락 없음. 비관영 매체에 [메시지]를 잘못 붙인 곳도 없다. 세부 권고만 있다(R-9, R-10, R-15) |

**수치 대조 결과(원자료와 맞음)**
- 알파벳: 약 13%·5천억 달러(CNBC), 12% 넘게·약 반조 달러(Sky), 12.6%(MBC), 5천억 달러(Handelsblatt)
- 나스닥100 1.4%(FT), 아마존 잉여현금흐름 -424억 달러(CNBC), AWS 39%(연합뉴스·한국경제)
- 아마존 주가 6%(Le Figaro)·7%(한국경제), 매출 2,019억 달러·12%(Le Figaro; YTN도 12%)
- 인텔 16%(CNBC)·17%(FT)
- 유조선 4척(CBS)·3척(AP), WTI 102달러(MBC·YTN)
- 4,260만 배럴·2.30유로(Libération). '11개국'은 기사 제목 기준이다(URL에는 'douze'가 있음)
- 이스라엘: 53·48·19석, 리쿠드 27석, 샤스 6석(Globes), 570만 명 이상 투표(Haaretz)
- 사전투표 4,300만 표(BBC), 미 3분기 GDP 3.4%(NYT·요미우리), PCE 3.6%·예상 3.7%(매일경제), ECB 예금금리 2.50%(매일경제)
- 라가르드 '2월 7일'(Bloomberg 단독. 1-2 참조)
- 드론 194대(Interfax), 우크라이나 철도역 14명 사망(TBS·Japan Times·Channel 4), ZIM 화물선 컨테이너 421개(Globes)
- MS 250억 달러 채권(Bloomberg), 아우디 '10%'(WELT 소식통), 280억 파운드(Guardian)
- 한국: 46.4%·14가구(조선일보), 7만6700가구(경향신문), 26.7조(한겨레)·19조(한국경제), 7만 명(franceinfo)

---

## 1. 출처 추적 (매체 귀속·수치·내용)

### [필수 수정] 1-1. 세 종목의 급락을 모두 'AI 설비투자 비용'으로 묶음. 원자료가 밝힌 다른 원인을 뺐다
- 경로: `essence.headline`, `top10[0].headline_ko`, `top10[0].why`(마지막 문장 "연산력(기술)과 돈(현금흐름·차입)이 정면으로 부딪힌 하루"), `by_country.uk[0].headline_ko`, `fishbone.links[0].logic`(🔎 문장)
- 원자료가 각 하락의 원인으로 쓴 것은 이렇다.
  - **인텔**: CNBC "chipmaker blames PC slowdown for weak guidance". CNBC는 "AI 수혜주였지만 PC 시장 부진에 눌렸다"고 썼고, FT는 "weaker chip sales forecast", Handelsblatt는 "높은 메모리 가격에 PC 구매 감소"라고 썼다. AI 설비투자 비용과는 다른 원인이다.
  - **알파벳**: Reuters 제목은 "Alphabet **revenue miss** revives AI capex jitters"다. 초안은 이 기사를 'AI 설비투자 불안 재점화'로만 인용하고 '매출 미달'을 뺐다. CNBC 실시간 기사는 "disappointing third quarter", CNBC 본기사는 '예상보다 큰 마이너스 잉여현금흐름'을 원인으로 들었다. FT는 오히려 '예상보다 낮은 설비투자'라고 썼다.
  - **아마존**: Reuters는 "fourth quarter sales below estimates", FT는 "lower Christmas sales forecast … disappointing sales and guidance despite booming cloud unit"이라고 썼다. 연합뉴스("기대치 밑돈 실적")와 YTN("시장 전망치 밑돌아")도 매출과 전망을 원인으로 들었다. 'AI 투자에 현금흐름 악화'를 원인으로 쓴 것은 한국경제뿐이다(NYT는 '현금 소진에 월가 불안'을 배경으로 썼다).
- 이렇게 고친다.
  - `essence.headline`: "빅테크 실적에 시장이 거세게 반응했다(알파벳 사상 최악의 하루 — 매출 미달·마이너스 잉여현금흐름·AI 지출 우려, 아마존 6~7% 하락 — 매출 전망 하회·현금흐름, 인텔 16~17% 급락 — PC 부진). 이란 전선에서는 공격 옵션 보고와 외교 재개 모색이 같은 날 나왔고, 유가는 외교 기대에 내렸다. 이스라엘은 개표가 끝나고도 과반 정부가 없다." 'AI 비용 청구서'라는 묶음은 `essence.derivation.rebuild`의 (해석) 문장에만 남긴다.
  - `top10[0].headline_ko`: "빅테크 실적 충격: 알파벳 사상 최악의 하루(약 12~13%↓·시총 5천억$ 증발), 아마존 잉여현금흐름 -424억$·매출 전망 하회, 인텔 16~17%↓(PC 부진)"
  - `top10[0].why`·`essence.derivation.decomposition`·`fields[2].phenomenon`의 Reuters 인용: "Reuters는 '매출 미달이 AI 설비투자 불안을 되살렸다'"
  - `top10[0].why` 마지막 문장 앞에 "🔎 해석:"을 붙인다.
  - `by_country.uk[0].headline_ko`: "알파벳 사상 최악의 하루 — 매출 미달에 AI 설비투자 불안 재점화(Reuters)"
  - `fishbone.links[0].logic`의 🔎 문장: "🔎 한국경제는 AI 투자의 현금 소모를 원인으로 봤지만, Reuters·FT·연합뉴스·YTN은 매출·4분기 전망 하회를 원인으로 들었다."

### [필수 수정] 1-2. 라가르드 '2월 7일'을 닛케이·한국경제TV에도 귀속함
- 경로: `essence.derivation.decomposition`("라가르드 2월 7일 조기 사임(Bloomberg·닛케이·한국경제TV)")
- 날짜 '2월 7일'은 Bloomberg에만 있다("resign on February 7, before the end of her term next October"). 닛케이 제목은 「金融政策以外に関与」 仏大統領選前の退任を決断이고 날짜가 없다. 한국경제TV는 "내년 2월 사임"이라고만 썼다. Japan Times도 사임을 보도했다.
- 이렇게 고친다: "라가르드 조기 사임(Bloomberg '2월 7일'; 한국경제TV '내년 2월'; 닛케이·Japan Times)". `fields[4].phenomenon`과 `top10[5].why`는 이미 바르게 귀속했다.

### [필수 수정] 1-3. 슈타인마이어 '직설 비판'을 DW·ARD 복수 출처로 쓰고, 가설 판정의 '복수 출처 지지'로 셈
- 경로: `hypothesis_check.support[3]`("슈타인마이어의 대중 직설 비판(DW·ARD)"), `hypothesis_check.note`("지지 쪽 복수 출처는 … 슈타인마이어의 대중 비판 정도"), `fields[7].phenomenon`("(DW·ARD)"), `top10[6].why`, `by_country.de[1].why`
- 비판 내용은 DW 기사 두 건(같은 매체)에만 있다. "Steinmeier wird in China überraschend deutlich", 그리고 "Mit Größe und Macht kommt große Verantwortung"이 그것이다. ARD 원자료는 제목 "Rede von Bundespräsident Steinmeier bei Besuch in China"(요약 없음)와 tagesschau 요약("Grundsatzrede zu den europäisch-chinesischen Beziehungen")뿐이다. 연설을 했다는 사실만 확인될 뿐 '직설 비판'은 없다. 따라서 이 비판은 단일 매체 보도다.
- 독일 대통령의 연설이 '미국의' 대중 포위선 가설을 지지하는지도 별도 논증이 필요하다.
- 이렇게 고친다.
  - 출처 표기: "슈타인마이어의 대중 직설 비판(DW 단일 매체; ARD는 연설 사실만)"
  - `hypothesis_check.note`: "지지 쪽 복수 출처는 분쟁 지속 요소(이란 측 유조선 피격 주장, 철도역 공격, ZIM 화물선 침몰)뿐이고, 슈타인마이어 비판(DW)·AI 회사채 기록(Bloomberg)·FCC 규제(SCMP)·EU 비축유 방출(Libération)은 단일 출처라 판정 근거에서 뺀다."
  - `support[3]` 안의 슈타인마이어 항목에 "(독일의 입장 — 미국의 포위선과 직접 관련 없음)"을 붙인다.

### [필수 수정] 1-4. 알래스카 '새 소환장'을 CNN·CBS에도 귀속함
- 경로: `fields[5].phenomenon`("새 소환장을 냈고(ABC·AP·CNN·CBS)"), `top10[8].why`(같은 귀속)
- 새 소환장은 ABC("DOJ issues new wave of subpoenas")와 AP("issues new subpoenas … AP source says")에만 있다. 둘 다 소식통 인용이다. CNN은 "Dan Sullivan criminal probe accelerates"라고 썼고 소환장은 언급하지 않았다. CBS는 "What to know about Alaska's Senate race as ballot fight heats up"이라는 배경 기사다.
- 이렇게 고친다: "법무부는 알래스카 상원 선거 '스포일러 후보' 의혹 수사에서 새 소환장을 냈다(ABC·AP, 소식통). CNN은 수사가 빨라지고 있다고 전했다."

### [필수 수정] 1-5. 인텔 해설에 Handelsblatt에 없는 원인('AI 데이터센터가 메모리를 빨아들여')을 붙임
- 경로: `fields[0].cause`("AI 데이터센터가 메모리를 빨아들이면서 PC 같은 기존 수요는 비싼 부품 가격에 눌린다(Handelsblatt)"), `fields[0].essence`("AI가 부품을 독식하고")
- Handelsblatt 원문은 "hohe Speicherpreise dafür sorgen, dass weniger Computer gekauft werden"까지다. 높은 메모리 가격이 PC 구매를 줄였다는 내용뿐이고, 메모리 가격이 높은 원인(AI 데이터센터 수요)은 오늘 원자료 어디에도 없다. 굳이 연결하자면 TV도쿄의 'SK하이닉스 호실적·키옥시아 급등' 정도인데, 이 기사도 메모리 가격의 원인은 말하지 않는다.
- 이렇게 고친다.
  - `cause`: "높은 메모리 가격이 PC 구매를 줄였다(Handelsblatt). 🔎 해석: 메모리 가격 강세가 AI 수요 때문이라면 AI가 기존 완제품 수요를 밀어내는 구도이지만, 그 원인은 원자료에 없다."
  - `essence`: "🔎 비싼 부품, 관세로 끌어오는 공장, 비축유로 막는 에너지 비용 — 제조 비용 압박이 여러 경로로 나타나는 국면(메모리 가격의 AI 원인설은 미확인)."

## 2. 연결 타당성 (시점·나라·원인)

### [필수 수정] 2-1. 유가가 '유조선 피격 주장보다 외교 기대에 더 반응했다' — 시점이 맞지 않음
- 경로: `fields[2].cause`("유가는 공급 위험 주장(이란의 유조선 피격 주장)보다 외교 기대에 더 반응했다"), `essence.derivation.rebuild`("확전 준비와 협상 기대가 동시에 가격에 반영되고 있다")
- 원자료 시각을 순서대로 놓으면 이렇다.
  - 유가 하락: WSJ 04:53 KST, MBC 05:29, YTN 05:40. 모두 29일 장 마감(정산 03:30 KST) 이후의 결산 기사다.
  - 유조선 기뢰 피격 주장: AP 04:58, CBS 06:12. CBS 요약에는 "on Thursday night"이 있다.
  - 공격 옵션 보고는 WSJ 05:30, '공습 수주'는 WaPo 06:01이다.
- 피격 주장과 확전 신호는 정산 이후에 나왔을 가능성이 크다. 그렇다면 유가가 피격 주장을 '무시했다'고도, 확전 준비가 '가격에 반영됐다'고도 말할 수 없다. 원자료가 직접 잇는 것은 '외교 기대 → 유가 하락'(WSJ·MBC·YTN)뿐이다.
- 이렇게 고친다.
  - `fields[2].cause`: "유가는 외교 재개 기대에 내렸다(WSJ·MBC·YTN). 이란의 유조선 피격 주장과 공격 옵션 보고는 원자료 시각상 장 마감 뒤에 나와 오늘 유가에 반영됐는지 알 수 없다."
  - `essence.derivation.rebuild`: "에너지·군사 축에서는 확전 준비와 협상 모색이 같은 날 나란히 보도됐다(가격은 아직 외교 기대만 반영)."
  - `watch[0]`에 "다음 거래일 유가가 유조선 피격 주장에 반응하는지"를 더한다.

### [필수 수정] 2-2. DW '다크 탱커 합법화'를 '대러 에너지 제재의 선택적 완화'로 읽고, 세 번째 독립 증거로 셈
- 경로: `fishbone.links[6].logic`, `essence.derivation.rebuild`("러시아 경유의 미국 반입·다크 탱커 합법화 보도는 같은 방향(대러 에너지 제재의 선택적 완화)"), `hypothesis_check.against[1]`("세 매체가 같은 방향을 따로 보도"), `top10[2].why`
- DW 원문은 "Die USA sollen Medienberichten zufolge erwägen, sogenannte 'Dark Tankers' in legale Schiffe umzuwandeln, um ihnen den Transport von Rohöl zu ermöglichen, **das nicht den Sanktionen unterliegt**"다. 원문에는 러시아가 언급되지 않는다. 운송 대상도 '제재 대상이 **아닌** 원유'다. 제재를 푼다는 뜻이 아니라, 선박을 합법 지위로 바꿔 제재 밖 원유만 나르게 한다는 뜻으로도 읽힌다. 기사 제목도 "EU가 미국 없이 그림자 선단과 어떻게 싸울 수 있나"다. 이것을 대러 제재 완화와 '같은 방향'으로 세면 원문을 넘어선다.
- 경유 건은 Handelsblatt('미국 예외')와 FT(뉴저지행 러시아산 경유 카고)가 서로 독립적으로 확인한 **두 매체**다. 따라서 '세 매체'는 '두 매체'로 고쳐야 한다.
- 이렇게 고친다.
  - `links[6].logic`: "🔎 병치(단일 출처, 재인용): DW는 언론 보도를 인용해 미국이 '다크 탱커'를 합법 선박으로 전환해 제재 대상이 아닌 원유를 운송하게 하는 방안을 검토한다고 썼다. 러시아 언급도, 제재 완화 여부도 원자료에 없어 경유 '미국 예외'(Handelsblatt)와 같은 방향인지는 알 수 없다." 이 링크를 지우는 것도 가능하다.
  - `against[1]`: "… Handelsblatt와 FT가 러시아 경유의 미국행을 따로 보도(두 매체, 거래 규모·조건 미상). DW의 다크 탱커 보도는 방향이 불분명해 참고로만."
  - `essence.derivation.rebuild`와 `top10[2].why`에서 "다크 탱커 합법화"를 '같은 방향' 근거 목록에서 뺀다.

## 3. 사실/해석 분리·원문 오독

### [필수 수정] 3-1. 알래스카 수사를 '양당 모두를 대상'으로 씀 — 원문과 반대
- 경로: `fields[5].counter`("선거 수사는 양당 모두를 대상으로 한 개별 사건들이다(알래스카는 공화당도 펠톨라 캠프 조사)")
- 원자료상 수사 대상은 모두 민주당 쪽이다.
  - ABC: 법무부 수사는 "alleged efforts by **Democrats** to recruit a candidate with the same name as the GOP incumbent"
  - WaPo: "**Republicans** launch investigations into **Peltola** campaign". 공화당이 민주당 펠톨라 캠프를 조사한다는 뜻이다.
  - Guardian: 알래스카 주지사의 펠톨라 캠프 조사 명령, 트럼프의 펠톨라 기소 촉구
  - NYT(캘리포니아): "unsubstantiated claims about large numbers of illegal voters"
- 초안의 "공화당도 … 조사"는 '공화당이 조사받는다'로 읽히고, '양당 대상'이라는 결론으로 이어졌다. 원문을 거꾸로 읽은 것이다.
- 이렇게 고친다: "이 해석이 틀렸다면: FCC 결정은 SCMP 단일 보도이고 정상회담 협상용 카드일 수 있다. 알래스카 건은 민주당 측의 동명이인 후보 영입 의혹이라는 구체적 사안에 대한 수사이고(ABC), 선거 절차 전반을 겨냥한 것이라는 근거는 아직 없다. 캘리포니아 수사는 NYT 단일 보도다."

### [필수 수정] 3-2. 알파벳 반론에 전날 원자료를 쓰고, 오늘 원자료의 같은 근거는 뺐다
- 경로: `fields[2].counter`("검색·광고 같은 본업 문제와 겹쳤을 수 있고(전날 WSJ '검색 매출 둔화')")
- 오늘 원자료에 같은 방향의 근거가 있다.
  - Reuters "Alphabet **revenue miss**"
  - CNBC 실시간 "Alphabet reported a disappointing third quarter"
  - 한국경제 "'구글링 시대 끝나나'…AI가 구글의 검색사업 흔든다"
  - CNBC(Reddit) "as Google search traffic shrinks"
- 이렇게 고친다: "알파벳 하락은 매출 미달(Reuters)·검색 사업 약화 우려(한국경제; CNBC는 Reddit 실적 기사에서 '구글 검색 트래픽 감소')와 겹쳤을 수 있고, …". '전날 WSJ'는 지운다.

## 4. 반박 증거 누락

### [필수 수정] 4-1. 대중 포위선 가설의 반박 뉴스가 `hypothesis_check.against`에서 빠짐
- 경로: `hypothesis_check.against`
- work 파일에 태그가 붙어 있는데 점검표에 없는 반박 뉴스는 이렇다.
  - **SCMP**(cn) "In Michigan Senate race, **Trump's softer China tone** gives candidates room to look elsewhere". 미국 대통령의 대중 어조가 누그러졌다는 보도로, 포위선 가설의 직접 반박이다.
  - **毎日新聞**(jp) 「中国製自動車席巻で理念曲げるEU 日本も『不利を被る可能性』」. 동맹 EU가 중국차에 맞춰 원칙을 굽힌다는 보도로, 중국 고립의 반대 방향이다.
  - **경향신문**(kr) '미 정부 규제에도 특허절벽에 중국서 신약 찾는 미국 빅파마'. `top10[6].why`에는 '반대 흐름'으로 들어가 있지만 점검표에는 없다.
  - (참고) **SCMP** '중국, 잠수함 탑재 가능한 AI 시험'. 기술 제재 속에서도 중국 AI 응용이 진척됐다는 보도다(SCMP 단일·중국 측 시연).
- 이렇게 고친다. `against`에 다음 항목을 추가한다: "가설 균열 — 대중 포위선: 트럼프의 대중 어조 완화로 미시간 상원 후보들이 대중 강경론을 접음(SCMP), EU가 중국차 확산에 원칙을 굽힘(마이니치), 미 빅파마의 중국 신약 후보 탐색(경향신문). 각각 단일 매체." 같은 날 FCC 규제(SCMP)와 나란히 놓아 '규제는 쌓이지만 대통령 어조와 동맹·기업 행동은 반대로 간다'는 균열을 `note`에 한 줄 적는다.

---

## 권고

### [권고] R-1. 아마존 '주가 6~7% 하락'은 시간외일 가능성
- 경로: `essence.headline`, `essence.derivation.decomposition`, `fields[2].phenomenon`, `top10[0].why`, `by_country.fr[3]`
- CNBC는 "Amazon reported third-quarter earnings on Thursday **after the bell**"이라고 썼다. 실적이 장 마감 뒤에 나왔으므로 6~7%는 시간외 낙폭일 가능성이 크다. Le Figaro는 "à la clôture"라고 썼지만, 실적 발표 시점과 맞지 않는다.
- "주가 6~7% 하락(시간외 추정; Le Figaro 6%·한국경제 7%)"으로 표기한다.

### [권고] R-2. '사상 최악의 하루' 출처에 MBC를 넣음
- 경로: `hypothesis_check.against[0]`("알파벳 사상 최악의 하루(CNBC·Sky·MBC·Handelsblatt)")
- MBC 제목은 '알파벳 12.6%↓'뿐이다. "알파벳 사상 최악의 하루(CNBC·Sky·Handelsblatt; MBC '12.6%↓')"로 고친다.

### [권고] R-3. 폴리마켓 '영국 당국 회부'는 CNBC에만 있음
- 경로: `fields[3].phenomenon`
- NBC는 거래 1시간 중단과 '이용자 자금 도난 보도'까지만 썼다. "이용자 자금이 도난당했고(NBC·CNBC; Le Figaro '수백만 달러 도난 가능성') 영국 당국에 회부했다(CNBC)"로 고친다.

### [권고] R-4. 캐나다 '대미 의존 축소' 해석과 엔비디아 참여가 충돌하고, 라벨 인용부호가 원문과 다름
- 경로: `fishbone.links[8].logic`, `top10[7].why`(마지막 🔎 문장), `fishbone.bones[geopolitics].items[n37].label`
- 코히어 투자 라운드에는 미국 기업 엔비디아가 참여했다(Handelsblatt). 해석 문장에 "다만 미국 기업 엔비디아도 투자에 참여해 'AI 탈미국'으로 보기는 이르다"를 붙인다.
- n37 라벨 "카니·EU '준회원·반트럼프 연대'"는 인용부호 안의 표현이 원문과 다르다. AP 원문은 "wider alliance against Trump threats"다. 라벨을 "카니·EU, 준회원·'트럼프 위협 맞선 동맹' 추진"으로 바꾼다. `fields[7].phenomenon`의 '반트럼프 연대'도 같이 고친다.

### [권고] R-5. `top10[2].why`(팀장 작성): '구체적 물동량'은 원자료에 없고, 전날 자료를 근거로 씀
- 첫 문장 "미·러 거래가 구체적 물동량으로 나타났다"의 '물동량'은 원자료에 없다. 같은 글의 "거래의 규모·조건은 원자료에 없다"와도 모순된다. "러시아산 경유 카고의 미국 동부 항구 반입이 거론됐다(FT)"로 고친다.
- "어제의 RDIF 제재 해제 논의(크렘린 언급)"는 오늘 원자료에 없는 10-29 자료다. `hypothesis_check.note`의 같은 문구와 함께 "(10-29 원자료, 오늘 재확인 없음)"을 붙인다.

### [권고] R-6. Kommersant에 없는 '고금리'
- 경로: `fields[1].cause`, `by_country.ru[3].why`
- Kommersant 원문의 원인은 "снижению продаж и ухудшению условий по кредитам", 즉 판매 감소와 대출 조건 악화다. `cause`의 "고금리·대출 조건 악화"는 "판매 감소·대출 조건 악화(Kommersant)"로 고친다. by_country의 "긴축·고금리의 실물 전이"에는 "🔎 해석"을 붙인다.

### [권고] R-7. 단일 기사 하나를 '시장 판단'으로 일반화
- 경로: `fields[6].cause`("… 대통령에게 남아 있다는 시장 판단이다")
- 근거는 한국경제TV 기사 하나다. "🔎 해석: 한국경제TV가 전한 전망(단일)처럼, 선거가 의회를 바꿔도 관세·군사 결정권은 대통령에게 남는다는 관측이 있다"로 고친다.

### [권고] R-8. 통화 분야의 본질·원인이 매일경제 단일 속보에 기대고, 그 기사의 시각이 맞지 않음
- 경로: `fields[4].cause`, `fields[4].essence`
- ECB 2.50% 동결과 PCE 3.6%는 매일경제 단일 속보다. 게다가 원자료 published가 각각 07:20·06:54 KST로, 원자료 수집 시각(06:15)과 초안 작성 시각(06:27)보다 늦다. 피드의 시각 오류로 보이지만 시점을 확인할 수 없다.
- `cause`의 "물가(PCE 3.6%)" 뒤에 "(매일경제 단일)"을 붙인다.
- `essence`의 근거로는 복수·독립 근거를 쓴다. Japan Times('이란발 유가 충격·국채 금리 급등'), 닛케이 「欧州国債概況」('ECB利上げ観測' — ECB 인상 관측), Bloomberg('연준 이번 주 동결')를 명시한다.

### [권고] R-9. '달러 지수 하루 하락'을 비달러 결제망의 반박 증거로 씀
- 경로: `hypothesis_check.against[4]`
- Xinhua의 "美元指数29日下跌"는 하루치 시세 기사다. 결제망 구조와는 관계가 없다. 이 항목에서 지우고, 중·칠레 통화스와프 갱신(인민일보 관영, 규모 미기재)만 남긴다. `fields[4].phenomenon`의 해당 문장도 시세 단신이라 지워도 된다.

### [권고] R-10. 카타르에너지 기사를 'CGTN 단독'이라 씀
- 경로: `top10[1].why`("CGTN 관영 단독"), `by_country.cn[3].why`("CGTN 단독(관영)")
- 원문 제목 앞의 "EXCLUSIVE-"는 통신사 속보를 그대로 옮겨 실은 형식이다. CGTN의 단독 취재라는 근거는 없다. "CGTN(관영, 'EXCLUSIVE' 통신 속보 전재 — 원 출처 미표기)"로 고친다. [메시지] 표기는 그대로 둔다.

### [권고] R-11. 푸틴 발언의 '준비돼 있다' 부분과 위협 해석이 빠지고, Interfax 인용 귀속이 모호함
- 경로: `essence.derivation.rebuild`(④), `hypothesis_check.against[2]`, `fields[7].phenomenon`·`top10[4].why`("Meduza·동아일보의 Interfax 인용")
- 반박 증거로 쓰려면 반대 독해도 함께 적어야 한다. Independent는 "'ready for war' with Europe in chilling threat", Handelsblatt는 '발트해 긴장 고조 경고'로 보도했다. ④를 "푸틴의 '전쟁 준비는 돼 있지만 유럽과 전쟁은 원치 않는다' 발언(Independent는 '위협'으로 보도)"으로 고친다.
- Meduza 원자료에는 Interfax 인용 표기가 없다. "Meduza; 동아일보(Interfax 인용)"로 나눠 쓴다.

### [권고] R-12. 철도역 공격 기사의 '휴전' 맥락이 빠짐
- 경로: `hypothesis_check.support[1]`, `fields[7].phenomenon`
- Channel 4 제목은 "Russian train strike kills 14 **despite Melania Trump's negotiated ceasefire** in Ukraine"이다. 휴전이 존재한다는 점은 분쟁 장기화 가설의 반박이고, 그 휴전이 깨졌다는 점은 지지다. 양면을 적는다: "멜라니아 트럼프가 중재한 휴전에도(Channel 4) 철도역 공격 14명 사망".

### [권고] R-13. EU 비축유 방출 기사에서 반대 문장을 뺌
- 경로: `hypothesis_check.support[2]`, `fields[0].phenomenon`
- Libération 원문은 "Sans que Bruxelles redoute de problème d'approvisionnement"로 끝난다. 브뤼셀은 공급 문제를 우려하지 않는다는 문장이다. "(단, EU 집행위는 공급 차질을 우려하지 않는다고 함)"을 덧붙인다. 유럽 경유 가격이 '대중' 에너지 봉쇄 가설과 어떻게 연결되는지도 불분명하므로, '에너지 압박(유럽 내부 비용)'으로 범위를 좁힌다.

### [권고] R-14. `by_country.kr[4]`(팀장 작성): 외국인 매매 방향 오해 소지
- 제목이 '외국인 9월 순매도'와 '코스피 1%대 하락'을 한 줄에 붙여 놓았다. 그러나 조선일보 원문은 "외국인도 3거래일 연속 순매수를 이어갔지만, 삼성전자가 주주 환원 실망감에 4% 넘게 떨어지면서" 하락했다고 썼다.
- why에 "29일에는 외국인 3거래일 연속 순매수 — 하락 원인은 삼성전자(조선일보)"를 추가한다.

### [권고] R-15. `by_country.ru[2]`: 관영 Vesti를 사실 확인 출처처럼 나열
- "Interfax(194대·공항), Vesti(관영)"를 "Interfax(194대·공항); Vesti(관영)도 공항 중단 보도"로 고친다. 관영 보도는 사실 확인의 근거가 아니라 같은 내용을 보도했다는 뜻으로만 쓴다. 공항 중단은 Interfax로 이미 확인된다.

### [권고] R-16. `top10[8].headline_ko`: 단일 출처 내용을 제목에 표시 없이 씀
- "트럼프는 본디 법무장관 경질"은 WaPo 단일 보도다. why에만 표시돼 있으므로 제목도 "트럼프, 본디 법무장관 경질(WaPo 단일)"로 고친다.

### [권고] R-17. `top10[9].why`: 산케이 원문에 없는 설명을 덧붙임
- '일·영·이'는 원자료에 없는 배경 설명이다. 원제는 「＜主張＞日独首脳会談 GCAP遅れは許されぬ」다. "산케이 사설(일독 정상회담)은 차세대 전투기 GCAP 지연은 용납 안 된다고 주장"으로 고친다.

### [권고] R-18. `fields[0].phenomenon`: 아우디 관세 인하를 확정 사실로 씀
- "미국은 … 관세를 낮춰 주기로 했다"는 확정 표현이다. WELT 원문은 "sollen … zugesagt haben – Insider"(약속했다고 함 — 소식통)이고, Handelsblatt는 '아직 구두 약속'이라고 썼다.
- "미국이 아우디에 … 관세 인하를 약속했다고 소식통이 전했다(WELT '10%'; Handelsblatt '구두 약속 단계')"로 고친다.

### [권고] R-19. 젠슨 황 지인 스파이 판단 보도를 '기술 포위선' 지지로 분류함
- 경로: `hypothesis_check.support[3]`
- 이 보도는 미 정보기관의 방첩 판단이다(요미우리 등 3매체). 제재·수출통제 같은 기술 포위 조치가 아니다. "(방첩 보도 — 기술 제재 조치는 아님)"을 붙인다. 아니면 지지 근거에서 빼고 `top10[6]`에만 둔다.

### [권고] R-20. `fields[7].cause`: '동맹국(캐나다·독일·한국) 거리 조정'에서 독일 근거가 없음
- 오늘 독일 관련 원자료는 이렇다. 슈타인마이어의 대중 비판(DW), 메르츠의 캐나다 준회원 구상 제동(Spiegel), 한·독 전략적 동반자 관계(JTBC), 아우디의 대미 관세 합의 기대(WELT·Handelsblatt). 모두 미국과 거리를 둔다는 근거가 아니다. 아우디 건은 오히려 대미 순응이다.
- '독일'을 빼거나, 대미 거리 조정의 근거 기사를 명시한다.

---

## 5. 누락 점검

- `_lead.json`의 top10 10건은 브리핑 `top10`에 모두 있고, 순서와 내용도 같다. by_country 9개국도 같다. **누락 없음.**
- 피쉬본 노드는 41개이고 8개 분야가 모두 있다. crypto 3개 노드는 원자료(NBC·CNBC·WSJ·Ynet·Bloomberg·Le Figaro)와 맞는다. 스테이블코인 헤드라인이 없다는 점도 `fields[3]`에 명시돼 있다.
- 관영 매체 표기: state_media=true 기사(Xinhua·CGTN·CCTV·인민일보·China Daily·TASS·RIA·Vesti)가 쓰인 곳은 모두 '관영' 또는 [메시지]로 표기됐다. 비관영 매체(SCMP·Meduza·Interfax·Kommersant 등)에 [메시지]를 붙인 곳은 없다.

---

## 요약

- [필수 수정] 10건
  - 1-1: 세 종목 급락을 AI 비용으로 묶고, Reuters '매출 미달'·인텔 PC 부진을 누락
  - 1-2: 라가르드 '2월 7일' 귀속
  - 1-3: 슈타인마이어 비판을 DW·ARD 복수 출처로 쓰고 판정 근거로 사용
  - 1-4: 알래스카 새 소환장 CNN·CBS 귀속
  - 1-5: 인텔 해설에 출처에 없는 원인 추가
  - 2-1: 유가와 유조선 피격 주장의 시점 역전
  - 2-2: 다크 탱커를 대러 제재 완화로 읽고 세 번째 증거로 셈
  - 3-1: 알래스카 수사를 '양당 대상'으로 거꾸로 읽음
  - 3-2: 전날 WSJ를 반론 근거로 사용
  - 4-1: 대중 포위선 반박 뉴스(SCMP·마이니치·경향) 누락
- [권고] 20건: R-1 ~ R-20
- 매체 귀속 부풀리기는 어제보다 줄었지만 남아 있다. 오늘 새로 두드러진 것은 원인 서술의 선택적 인용(1-1·1-5·2-2)과 원문 반대 독해(3-1)다. 필수 수정을 반영한 뒤 verify.py를 다시 통과해야 하며, 반영 여부를 재검토한다.

판정: 수정 필요
