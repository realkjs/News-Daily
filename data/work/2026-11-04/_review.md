# 2026-11-04 팀장 검토 (임원 초안 `briefings/2026-11-04.json`)

- 검토 기준: `prompts/team-lead.md` 검토 모드, `prompts/analysis-framework.md`, `CLAUDE.md` 원칙
- 대조 자료: `data/work/2026-11-04/tmp/lead/digest.txt`(아래 `팀:인덱스`는 이 파일 기준), `data/raw/2026-11-04/*.json`, 직전 브리핑 11-01·11-02·11-03, `data/raw/2026-11-03/*.json`(11-03 10:50 KST 재수집분 — 11-03 브리핑 06:37 KST 이후 들어온 기사 포함)
- `python template/verify.py 2026-11-04` 결과: `검증 통과: 선별 뉴스 55건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상`
  → URL·구조는 통과했다. 아래 지적은 내용(시점·귀속·판정 논리)에 관한 것이다.

## 요약

| 구분 | 건수 | 핵심 |
|---|---|---|
| [필수 수정] | 5 | ① 케슘섬 공습 '선거 당일' 시점 오류 ② 판정 '유지' 전환 논리 불성립 ③ 다중 출처 반박 증거(AI 데이터센터 반발·나스닥 조정) 누락 ④ 마벨 인수·3자 회담의 발표 시점 오표기 ⑤ 배경 사례(하노이) 사실 오류 |
| [권고] | 12 | 단일 출처 오표기(셰플러·EU-영국), 북극항로·대중 포위 반례 누락, 동맹 축 분류 불일치, 억지 연결 1건, 공격 규모 과장 표현 등 |

---

## [필수 수정]

### 필수 1. 케슘섬 공습을 '선거 당일', '같은 날' 일어난 일로 썼다 (시점 오류)

- **위치**
  - `essence.headline`: "미국 중간선거 당일, 미국은 이란 케슘섬에 '방어적' 공습을 했고…"
  - `fishbone.head`: "선거일, 미국은 적을 때리고 동맹과 거리를 뒀다 — 협상 날짜가 잡히자 공격은 커졌다"
  - `essence.derivation.assumptions`: "오늘 원자료는 선거 당일에 공습(JPost·i24·CBS)과 동맹 원조 중단 발표(NYT 등)가 함께 나오고…"
  - `essence.derivation.rebuild`: "미국은 … 같은 날 보냈다(해석)"
  - `fields[geopolitics].essence`: "미국은 같은 날 적(이란)을 때리고 동맹(이스라엘)과 거리를 뒀다"
  - `fields[monetary].essence`: "공습과 견조한 고용이 같은 날"
  - `top10[0].why` 끝 문장: "11-03 브리핑의 '케슘섬 폭발음'(이란 매체 인용)과 오늘 공습 보도가 같은 사건인지는 원자료로 확인되지 않는다."
- **문제**: 오늘 원자료 가운데 공습 날짜를 적은 기사는 없다. 반면 11-03 원자료(재수집분)에는 미국의 케슘섬 타격이 **선거 전날(미국 시간 11-02 저녁)**에 이미 보도돼 있다. 공습은 선거 당일 사건이 아니다. 같은 사건인지 "확인되지 않는다"는 문장도 원자료와 맞지 않는다.
- **근거**
  - il:4 i24 `US strike on Qeshm island described as a 'defensive act,' in response to Iranian attack on US aircraft` (11-04T00:33) — 날짜 없음, "described as"는 이미 알려진 공습의 성격을 설명하는 표현
  - il:28 JPost `US carries out 'defensive' strikes on Qeshm Island after Iran downs drone, officials tell 'Post'` (11-04T05:14) — 날짜 없음
  - us:26 CBS `…after new U.S. strikes, Tehran called America's response … "not convincing."` — "new"는 시점을 특정하지 않음
  - 11-03 원자료 `data/raw/2026-11-03/us.json` WSJ `Exclusive | U.S. Strikes Iran's Qeshm Island as Trump Talks Down War Risks` (2026-11-03T09:39 KST = 미 동부 11-02 19:39)
  - 11-03 원자료 `il.json` Haaretz `Report: U.S. strikes Iran's Qeshm island, officials say` — 요약: "The strike was part of **a series of limited attacks carried out in recent weeks**, as Trump plays down the prospect of renewed war with Iran, the Wall Street Journal reported, citing U.S. officials" (11-03T10:23)
  - 같은 날 `il.json` JPost `US strikes Iran's Qeshm Island`, `ru.json` Interfax `WSJ сообщила, что США нанесли удар по иранскому острову Кешм`, TASS `NewsNation: США бьют по радарам и ракетным установкам на острове Кешм`, `cn.json` 인민일보 `美媒：美国袭击了伊朗格什姆岛`
  - 11-03 브리핑이 다룬 '폭발음'(Ynet 11-03T06:06, RIA 11-03T06:14)은 WSJ 단독보다 3시간 앞선 보도로, 같은 섬·같은 밤의 일이다.
  - 덧붙여 `fishbone.head`의 "협상 날짜가 잡히자 공격은 커졌다"도 원문이 뒷받침하지 않는다. 위트코프의 날짜 발표는 11-03 08:18 KST(=키이우 11-03 01:18)였다(`data/raw/2026-11-03/ru.json` RBC `Уиткофф назвал дату трехсторонних переговоров в Абу-Даби`). Meduza(ru:50)는 공격이 "С ночи 3 ноября"(3일 밤부터) 이어진다고 썼다. 두 시점이 거의 겹쳐 선후를 가릴 수 없고, Meduza는 "одна из самых масштабных"(최대 규모 **중 하나**)라고만 썼을 뿐 이전보다 "커졌다"는 비교가 없다.
- **수정 제안**
  - `essence.headline` 첫 문장 → "11-03 WSJ 단독(미 당국자)으로 처음 확인된 미국의 이란 케슘섬 타격을, 오늘 JPost(당국자)·i24는 이란의 드론 격추·미 항공기 공격에 대한 '방어적' 대응이라고 설명했고, 이란은 미국의 답변을 '설득력 없다'고 일축했다(CBS)."
  - `fishbone.head` → "미국은 이란에 '방어적' 무력을 쓰고 동맹(이스라엘)엔 원조 종료를 통보했다 — 협상 일정과 대규모 공격이 같은 주에 겹친다"
  - `assumptions`·`rebuild`·`fields[geopolitics].essence`·`fields[monetary].essence`에서 "선거 당일/같은 날 공습"을 지우고, "선거 직전(미국 시간 11-02) 공습, 선거일(11-03) 원조 중단 발표"로 시점을 나눈다.
  - `top10[0].why` 끝 문장 → "🔎 11-03 브리핑의 '케슘섬 폭발음'은 같은 날 오전(브리핑 뒤) WSJ 단독·Haaretz·JPost가 미 당국자를 인용해 미국의 타격으로 보도했다(11-03 원자료). Haaretz는 이를 '최근 몇 주간 이어진 일련의 제한적 공격'의 하나로 썼다. 오늘 보도는 그 공격을 '방어적'이라고 설명한 후속이며, 선거 당일의 별도 공습인지는 원자료로 확인되지 않는다."

### 필수 2. 판정 '유지' 전환의 논리가 서지 않는다 (가설 판정 논리)

- **위치**: `hypothesis_check.verdict`, `hypothesis_check.note`, `hypothesis_check.support[0]`, `hypothesis_check.against[0]`·`[2]`
- **문제**: 11-03의 축별 판정과 같은 기준을 오늘에 적용하면 결론은 '약화'다. '유지'로 올라간 것은 AI 축을 '상쇄'로 다시 분류했기 때문인데, 그 근거가 약하다. 단일 출처 기준도 양쪽에 똑같이 적용되지 않았다.
  1. **축별 비교**
     - 11-03: 이란 '보류', 우크라이나 '지지'(자포리자), AI '반박'(주권형 연산력 반례), 코인 '반박' → '약화'
     - 오늘 초안: 이란 '지지 쪽', 우크라이나 '상쇄', AI '상쇄', 코인 '반박' → '유지'
     - 이란 축이 한 칸 지지 쪽으로 가는 동안 우크라이나 축은 한 칸 반박 쪽으로 왔다(지지→상쇄). 둘이 서로 상쇄되므로 '약화'에서 벗어나는 근거는 AI 축의 재분류 하나뿐이다.
  2. **AI 축 '상쇄'의 근거가 약하다**
     - 지지로 든 것은 ⓐ 마벨-루멘텀 인수, ⓑ 나스닥 하루 반등, ⓒ 구글의 학교 AI 강제다.
     - ⓐ는 11-03에 이미 발표된 거래다(필수 4).
     - ⓑ는 초안 스스로 `fields[stocks].counter`에서 "하루 반등은 의미가 작고"라고 썼다. 같은 날 Handelsblatt(de:45)는 "Nachdem der Nasdaq offiziell in eine Korrektur eingetreten ist"(나스닥이 공식 조정 국면에 들어선 뒤)라고 썼다.
     - ⓒ는 상품 정책이라 "연산력 결제의 달러화"와 연결이 간접적이다.
     - 반대로 11-03의 '약화' 근거(주권형 연산력)는 오늘도 이어진다: de:70 SZ `Digitale Souveränität: Eine neue KI- und Cloud-Plattform für Europa` — 요약 "Bull und Schwarz Digits wollen eine Alternative zu US-Anbietern schaffen". 여기에 다중 출처 반박 증거가 빠졌다(필수 3).
  3. **단일 출처 기준이 비대칭이다**
     - `support[0]`은 제목이 "분쟁 지속 신호(복수)"인데 그 안에 us:26 CBS 단독 "설득력 없다"가 들어 있고, `note`도 "이란이 미국 답변을 일축했다(CBS)"를 판정 근거로 쓴다.
     - jp:26 테레비아사히 단일 제목(`「米と合意程遠い」とイラン高官 中間選挙後の再攻撃防ぐため仲介国の外交努力続く`) 하나가 쪼개져 `support[1]`("합의 아직 멀어")과 `against[0]`("중재국의 재공격 방지 외교") 양쪽에 들어갔다. `note`는 이 단일 제목을 "그래서 '강화'까지는 가지 않는다"의 근거로 쓴다. 11-02·11-03의 원칙("단일 매체 제목은 양쪽 모두 판정 근거에서 뺀다")과 어긋난다.
  4. **같은 협상 과정을 날마다 반대로 센다**: 11-03은 CBS의 이란 '공은 미국에'를 반박(협상)으로 셌다. 오늘은 같은 제안·답변 교환의 다음 단계인 CBS '미국 답변 설득력 없다'를 지지(분쟁 지속)로 센다. 제안과 답변이 오간다는 것 자체가 협상 진행의 증거이므로 양면(중립)으로 두어야 한다.
  5. **공습의 성격**: 11-03 원자료 Haaretz는 이 타격을 "a series of limited attacks carried out in recent weeks"의 하나로 썼다. 오늘 확인된 것은 확전의 전환점이 아니다. '약화' 기간에도 이어지던 저강도 공격이 드러난 것이다. 이란 축을 지지 쪽으로 두는 것은 받아들일 수 있다. 다만 판정을 바꿀 만한 새 국면으로 쓰려면 이 점을 적어야 한다.
- **근거**: us:26, jp:26, de:45, de:70, 11-03 원자료 Haaretz(il.json), 11-03 브리핑 `hypothesis_check.note`("단일 매체 제목 … 양쪽 모두 판정 근거에서 뺀다", 이란 '공은 미국에' 반박 분류)
- **수정 제안**: `verdict` → `약화`. `note`를 아래처럼 바꾼다.
  > "🔎 판정 '약화'(10-26 이후 9회 연속). 초안은 '유지'로 올렸으나 팀장 검토를 받아 되돌렸다. ① 이란 축: 11-03 브리핑이 '폭발음(이란 매체 인용)'으로만 다룬 케슘섬 타격이 미국의 공습으로 확인됐다(11-03 WSJ 단독·Haaretz·JPost, 오늘 JPost 당국자·i24 '방어적'). 그래서 이 축은 지지 쪽으로 한 칸 움직인다. 다만 Haaretz는 이를 '최근 몇 주간의 제한적 공격'의 하나로 보고, 미국은 '방어적'이라고 규정했다. 따라서 확전 전환이 아니라 저강도 무력과 협상의 병행이다. CBS '설득력 없다'는 제안·답변 교환 자체가 협상 진행을 뜻해 중립으로 두고, 테레비아사히(제목)와 함께 단일 출처라 판정 근거에서 뺀다. ② 우크라이나 축: 3자 회담 일정(11-03 위트코프 발표 — 반박)과 대규모 에너지 공격(지지)이 겹쳐 상쇄된다. 11-03의 '지지'에서 반박 쪽으로 한 칸 움직였다. ③ AI 축: 유럽의 미국 대체 AI·클라우드(SZ)와 EU 저작권 제동(Reuters)이 11-03의 주권형 연산력 반례를 잇는다. 미국 주지사 선거의 데이터센터 반발(FT·WaPo·CNBC)과 나스닥 조정 진입(Handelsblatt)도 반박 쪽이다. 나스닥 하루 반등과 11-03에 발표된 마벨 인수로는 상쇄되지 않는다. ④ 코인 축: 스테이블코인 근거는 오늘도 없다. ①과 ②가 서로 상쇄되고 ③·④가 반박이라 11-03과 같은 '약화'다."
  - `support[0]`의 제목 "(복수)"에서 CBS 항목을 빼 `support[1]`(단일)로 옮긴다.
  - `support[1]`의 "테레비아사히 이란 고위 '합의 아직 멀어'(제목)"와 `against[0]`의 "중재국의 재공격 방지 외교(테레비아사히 제목)"는 한 곳에 "테레비아사히(제목, 단일): 합의 멀다 + 중재 외교 지속 — 양면, 판정 근거 아님"으로 합친다.
  - (임원이 '유지'를 고집하려면, 11-03에 없던 새 다중 출처 지지 증거를 AI 또는 코인 축에서 제시해야 한다.)

### 필수 3. 다이제스트에 있던 다중 출처 반박 증거가 가설 점검표에서 빠졌다 (누락)

- **위치**: `hypothesis_check.against[2]`(AI 축), `fields[industry]`·`fields[stocks]`의 `counter`
- **문제**: 미국 안에서 AI 데이터센터에 대한 정치적 반발이 선거 쟁점이 됐다는 보도가 4개 매체에 있다. 이는 "연산력 결제의 달러화" 전제(미국이 연산력을 무제한 늘린다)에 대한 반박 증거다. 그런데 `fields[stocks].phenomenon`에 CNBC 제목 한 줄로만 나오고 가설 점검표에는 없다. 나스닥 조정 진입, 마벨 목표가 하향, 골드만 '현금 비중 확대'도 'AI 반등이 상쇄한다'는 주장과 반대 방향인데 빠졌다.
- **근거**
  - uk:41 FT `Investors watch US state races for signs of backlash against AI boom` — "three dozen gubernatorial races could have significant impact on data centre development across America"
  - us:79 WaPo `Here's where data centers are on the ballot`
  - us:39 CNBC `Texas race results could kick AI trade while it's already down`
  - de:41 Handelsblatt 뉴스블로그 요약 "Texanischer Gouverneur setzt Genehmigungen für Rechenzentren aus"(텍사스 주지사, 데이터센터 인허가 중단 — 블로그 한 줄, 단일)
  - de:45 Handelsblatt "Nasdaq offiziell in eine Korrektur eingetreten"
  - kr:104 한국경제 `마벨 목표가 400→225달러`, kr:105 한국경제 `골드만삭스 "단기 충격 대비해 현금 비중 올려야"`
- **수정 제안**: `against[2]`에 추가한다.
  > "미국 내부의 연산력 반발: 주지사 선거가 데이터센터 개발을 좌우할 수 있다(FT)·데이터센터가 투표 안건에(WaPo)·텍사스 결과가 AI 트레이드에 타격(CNBC) — 복수. 텍사스 주지사의 데이터센터 인허가 중단(Handelsblatt 블로그, 단일). 시장: 나스닥 조정 진입(Handelsblatt), 마벨 목표가 400→225달러(한국경제), 골드만 '현금 비중 확대'(한국경제) — 하루 반등(Reuters·CNBC)은 이 흐름을 뒤집지 못한다."
  - `fields[industry].counter`에 "미국 안에서도 데이터센터가 선거 쟁점이 됐다(FT·WaPo·CNBC)"를 한 줄 붙인다.

### 필수 4. 마벨-루멘텀 인수와 3자 회담 날짜를 오늘 새로 나온 것처럼 썼다 (시점·기보도)

- **위치**
  - `fields[industry].phenomenon`, `top10[7].why`: "(11-03 Les Echos '1,150억 달러 AI 기록적 거래'의 당사자 확인)", "(… 당사자가 확인됨)"
  - `hypothesis_check.against[0]`: "미·우·러 3자 회담 10~11일 아부다비 확정(한겨레·요미우리·[관영] Channel One)"
  - `top10[4]`, `fields[forecast].phenomenon`
- **문제**
  - 마벨-루멘텀: 당사자는 11-03 다이제스트에 이미 이름이 나와 있다. Les Echos 기사의 당사자를 오늘 Bloomberg가 '확인'한 것이 아니다. 11-03에 발표된 거래를 오늘의 지지 증거로 쓰는 것이므로 그렇게 밝혀야 한다.
  - 3자 회담: 날짜는 11-03 아침 위트코프가 발표했다. 오늘 보도는 후속이다. 출처가 셋이지만 장소(아부다비·UAE)를 적은 것은 요약 없이 제목만 있는 요미우리와 관영 Channel One이고, 한겨레는 날짜만 적었다.
- **근거**
  - 마벨: 11-03 다이제스트 us:41 CNBC `Lumentum CEO touts 'enormous' opportunity in massive AI connectivity deal with Marvell`(11-03T06:00), 11-03 원자료 il.json Ynet `Marvell to acquire Lumentum for $115 billion in massive AI infrastructure deal`(11-03T09:24). 오늘 us:48 Bloomberg는 영상 코너 소개(`Bloomberg's Liana Baker joins Dani Burger on "Bloomberg Deals."`)다.
  - 3자 회담: 11-03 원자료 ru.json RBC `Уиткофф назвал дату трехсторонних переговоров в Абу-Даби`(11-03T08:18, "пройдет 10–11 ноября"), us.json Fox `US will mediate upcoming Ukraine-Russia talks in Abu Dhabi, Witkoff says`, uk.json FT `US to hold first talks with Russia and Ukraine since February`, de.json Zeit `Witkoff kündigt neue Gespräche … an`. 오늘: kr:84 한겨레(장소 없음), jp:66 요미우리 `３者協議 ＵＡＥで１０～１１日`(요약 없음), ru:4 Channel One(관영).
- **수정 제안**
  - `fields[industry].phenomenon` → "Bloomberg: 마벨의 1,150억 달러 루멘텀 인수(11-03 발표 — CNBC·Ynet·Les Echos, 오늘은 후속)."
  - `top10[7].why`의 괄호도 같은 내용으로 바꾼다.
  - `against[0]` → "미·우·러 3자 회담 10~11일 아부다비(11-03 위트코프 발표 — FT·Fox·RBC·Zeit, 11-03 브리핑 뒤 수집; 오늘 한겨레·요미우리·[관영] Channel One 후속)". "확정"은 "예정"으로 바꾼다.

### 필수 5. 배경 사례 '2019년 하노이 북미 정상회담 직전 군사 압박'은 사실과 다르다

- **위치**: `fields[forecast].precedent` — "2019년 하노이 북미 정상회담 직전 군사 압박"
- **문제**: 2019년 2월 하노이 회담 직전에는 미국의 대북 군사 압박이 없었다. 2018년 6월 싱가포르 회담 뒤 한미는 대규모 연합훈련(을지프리덤가디언 등)을 유예했고, 회담 직후인 2019년 3월에는 키리졸브·독수리훈련 종료를 발표했다. 압박 국면은 2017년('화염과 분노')이다. 오늘 사례(선거·회담 일정과 무력 병행)의 유사 사례로 쓸 수 없다.
- **근거**: 배경 사례 사실관계. 원자료에는 이 사례를 뒷받침하는 기사가 없다.
- **수정 제안**: "2018년 미 중간선거 민주당 하원 탈환. 협상 전 지렛대 쌓기의 예로는 1972년 북베트남 '라인배커 II' 폭격(파리 협상 재개 직전)"으로 바꾸거나, 두 번째 사례를 지운다.

---

## [권고]

### 권고 1. 셰플러 감원은 '관영 단일'이 아니다
- **위치**: `fishbone.bones[business].items[n6].label` "(관영 단일)", `essence.derivation.decomposition`·`rebuild`, `fields[business].phenomenon`·`counter`, `top10[8].headline_ko`·`why`
- **근거**: cn:11 CGTN `German auto supplier Schaeffler to cut 3,460 jobs, close five sites in Europe`. de:7 ARD Tagesschau 20시 요약에도 "Fränkische Auto- und Industriezulieferer Schaeffler will fast 3.500 Stellen abbauen"이 있다.
- **제안**: "셰플러 약 3,500명 감원(ARD; [관영] CGTN '3,460명·5개 사업장 폐쇄')". `rebuild`의 "핵심 근거로 쓰지 않는" 목록에서 뺀다.

### 권고 2. EU·영국 무역 완화도 '단일'이 아니다
- **위치**: `by_country.de[4]` "단독: EU·영국, 광범위한 무역 완화 임박(단일)"
- **근거**: de:43 Handelsblatt `Exklusiv: EU und Großbritannien stehen vor weitreichenden Handelserleichterungen`, uk:52 Guardian `Andy Burnham to unveil EU trade deals worth billions of pounds`
- **제안**: "EU·영국 광범위한 무역 완화 임박(Handelsblatt 단독 초안; Guardian '버넘, 수십억 파운드 EU 무역협정 발표 예정')"으로 고치고 "(단일)"을 지운다.

### 권고 3. 북극항로 축 증거가 가설 점검표에 없다
- **위치**: `hypothesis_check.support` / `against`
- **근거**: cn:32 SCMP `Greenland ratifies Trump deal despite questions about value` — "Greenland's parliament on Tuesday ratified the Arctic island's security agreement … with US President Donald Trump", ru:61 Vedomosti `МИД РФ потребовал от Норвегии соблюдать Договор о Шпицбергене`(제목만)
- **제안**: `support[1]`(단일)에 "북극: 그린란드 의회, 트럼프와의 안보협정 비준(SCMP 단일), 러 외무부의 노르웨이에 대한 스발바르 조약 준수 요구(Vedomosti 제목) — 북극항로 축의 간접 신호, 판정 근거 아님"을 넣는다. 가설의 '북극항로' 항목은 매일 시험 대상인데, 관련 기사가 있는 날 빠뜨리면 안 된다.

### 권고 4. '중국 고립' 반례가 빠졌다
- **위치**: `hypothesis_check.against`
- **근거**: de:7 ARD 요약 "EU genehmigt Übernahme von MediaMarktSaturn durch chinesischen Konzern JD.com"(단일, 요약 한 줄). 반대 방향으로는 ru:47 Kommersant `Европа опасается «зомби-предприятий» // Перепроизводство в КНР пугает партнеров по торговле, но не Пекин`이 있다.
- **제안**: "대중 포위선 반례(단일): EU의 JD.com 미디어마크트자투른 인수 승인(ARD). 반대로 유럽의 중국 과잉생산 우려(Kommersant)"를 짝으로 적는다.

### 권고 5. 동맹 축의 분류가 note와 against에서 다르다
- **위치**: `hypothesis_check.against[1]` "가설 균열 — 미국의 동맹 이용", `note` ③ "판정에서 중립으로 둔다"
- **문제**: against 목록에는 '가설 균열'로 올려 놓고, note에서는 중립이라고 한다. 독자는 반박 증거로 읽는다.
- **제안**: `against[1]`을 "🔎 양면(판정 중립): …"으로 시작하게 바꾸거나 별도 항목으로 옮긴다. il:27 JPost `Israel's next prime minister faces a growing crisis in US relations`도 함께 적는다.

### 권고 6. 바이낸스는 11-02 사건의 후속이니 판정 근거에서 빼라고 명시
- **위치**: `hypothesis_check.against[3]`, `top10[6].hypothesis` "반박", `by_country.kr[3].hypothesis` "반박"
- **문제**: 같은 해킹 사건이 11-02(인출·FBI 지목)와 11-03(순인출)에 이어 오늘(침투 경위)까지 3일 연속 반박 쪽에 올라 있다. 자포리자 사망자 갱신은 "다시 세지 않는다"고 하면서 바이낸스 후속은 다시 센다. 같은 규칙을 양쪽에 똑같이 적용해야 한다.
- **근거**: us:83 WaPo, uk:46 FT, ru:51 Meduza, kr:16·18 SBS(북한 부인). 11-02·11-03 브리핑 `against` 코인 항목.
- **제안**: `against[3]` → "코인 경로: 오늘도 스테이블코인 헤드라인 없음(판정 근거). 바이낸스 침투 경위(WaPo·FT·Meduza)는 11-02 사건의 후속이라 다시 세지 않는다." 북한 부인(kr:3)의 hypothesis는 '무관'으로 바꾼다.

### 권고 7. 공격 규모를 과장한 표현
- **위치**: `essence.derivation.assumptions` "협상 날짜가 잡힌 주에 최대 규모 에너지 공격이 이어지는 장면(Meduza)"
- **근거**: ru:50 Meduza 요약 "С ночи 3 ноября продолжается **одна из самых масштабных** российских атак на энергетику Украины"
- **제안**: "최대 규모 공격 중 하나(Meduza)"로 고친다. `fishbone.links[n24→n30]`은 이미 맞게 썼다.

### 권고 8. 피쉬본 억지 연결 1건
- **위치**: `fishbone.links` n32(유럽 항공편 폭탄 위협) → n7(일본 개인정보 유출)
- **문제**: logic 스스로 "두 사건을 잇는 배후 정보는 원자료에 없다"고 썼다. 나라도 다르고 수법(허위 신고 대 무단 접근)도 달라 인과가 없다. 검토 기준 2(억지 연결)에 해당한다.
- **제안**: 이 링크를 지운다. 꼭 잇고 싶다면 원자료가 직접 잇는 n12(바이낸스 가짜 면접, 사회공학)와 jp:22 TBS(`サイバー攻撃の背後に北朝鮮系ハッカー`, 다크웹 개인정보 매매)처럼 같은 행위자를 가리키는 연결로 바꾸되, 이것도 단일·제목임을 표기한다.

### 권고 9. 항공편 위협 편수는 매체마다 다르다
- **위치**: `fishbone` n32 라벨 "유럽 항공편 7대 허위 폭탄 위협", `fields[geopolitics].phenomenon` "항공편 7대"
- **근거**: uk:1 BBC·uk:44 FT·uk:13 Sky "seven", jp:60 아사히 `少なくとも4社8便`, fr:1 France 24 `une dizaine de vols`. `top10[5].why`에는 이미 정확히 적혀 있다.
- **제안**: 라벨을 "유럽 항공편 최소 7편 허위 폭탄 위협"으로 바꾼다.

### 권고 10. `cn[0]` 전체를 [메시지]로 묶지 말 것
- **위치**: `by_country.cn[0].headline_ko` "[메시지] 트럼프 '연간 약 40억 달러…' / SCMP '연 38억 달러 폐지'"
- **문제**: SCMP는 관영이 아니다. 원조 중단은 10여 개 매체가 보도한 사실이다. Xinhua 부분만 메시지다.
- **제안**: "트럼프, 연 38억 달러 대이스라엘 군사원조 폐지(SCMP) / [관영] Xinhua '연 약 40억 달러, 올해 말 종료'"

### 권고 11. 배경 사례 연도 정밀화
- **위치**: `fields[industry].precedent` "2016년 EU의 구글 안드로이드 끼워팔기 조사"
- **문제**: EU 집행위는 2015년 4월 조사에 착수했고, 2016년 4월 이의진술서를 냈으며, 2018년 7월 43억 4천만 유로 과징금을 부과했다. '2016년 조사'는 부정확하다.
- **제안**: "2018년 EU의 구글 안드로이드 끼워팔기 과징금(43억 유로, 2015년 조사 착수)"

### 권고 12. GMO 건은 11-03 기보도의 후속이라고 표기, top10 순서 정리
- **위치**: `by_country.jp[0]`, `fields[business].phenomenon`, `top10` 순서
- **근거**: jp:11 NTV `【GMO会見】2か月以上も"侵入"気付かず…（2026年11月3日掲載）`. 11-03 브리핑은 이미 GMO 회장 사과 회견(NTV·TBS)을 다뤘다.
- **제안**: "GMO '2개월 넘게 침입 몰라'(NTV — 11-03 회견 후속; 산케이 사설)"로 고친다. `top10[8]`(importance 3)이 `top10[9]`(importance 4)보다 앞에 있으니 순서를 바꾼다.

---

## 확인했으나 문제없는 항목 (참고)

- 대이스라엘 원조 금액·시점: NYT us:66 "$4 Billion … at End of Year", "part of an agreement reached months ago", Le Monde fr:34 "3,8 milliards", SCMP cn:36 "until 2028", Globes il:42 "$3.8 billion", Handelsblatt de:44 "Finanzministerium ist überrascht" — 귀속이 정확하다. "선거일 발표"도 맞다(Globes 11-03T23:03 KST = 미 동부 11-03 오전).
- NYT 화학무기: us:65 "Some administration officials suggested Prime Minister Benjamin Netanyahu is trying to draw President Trump back into military action" — 원 출처 1건이라는 표기와 판정 제외가 타당하다.
- 법무부 선거 감시관(de:41·de:0·uk:34), 알래스카 수사(us:31·us:25), 하버드 예측(kr:30·kr:54), JOLTS(kr:55·jp:54 "752万件"), 아소뷰 1,580만(jp:38), 세븐일레븐 16만(jp:27), 자포리자 33명(kr:56, 기보도 갱신 표기)도 원문과 맞다.
- 다른 배경 사례(1988 사마귀 작전, 2003 이라크 WMD, 1956 수에즈, 2015 아바고-브로드컴 약 370억 달러, 2023 MOVEit, 2022 로닌 가짜 채용 PDF, 2025 바이비트, 2000 부시-고어, 2020 법무부 부정선거 조사 지시)도 사실관계가 맞다.
- "10-26 이후 8회 연속 '약화'" 집계: 10-26·28·29·30·31·11-01·02·03 = 8회로 맞다(10-27 브리핑 없음).

---

판정: 수정 필요

---

## 반영 결과 (임원 최종)

- **[필수 수정] 5건 모두 반영**
  1. **시점 오류 정정**
     - 근거 확인: 11-03 원자료 재수집분에 WSJ 단독(11-03 09:39 KST), Haaretz, JPost 보도가 있다.
     - 케슘섬 타격을 '선거 전날(미국 시간 11-02 저녁)'로 고쳤다. 오늘 보도는 '방어적'이라는 성격 설명이 담긴 후속으로 처리했다.
     - 고친 곳: essence.headline, 전제(assumptions), 분해(decomposition), 재구성(rebuild), 피쉬본 머리, 지정학·통화 분야 본질, top10[0].
     - "협상 날짜가 잡히자 공격이 커졌다"는 문장을 지웠다. 대신 '같은 주에 겹친다, 선후는 가릴 수 없다'로 썼다.
  2. **판정을 '약화'로 되돌림**(9회 연속)
     - note를 축별로 다시 썼다. 이란 축은 지지 쪽으로 한 칸, 우크라이나 축은 반박 쪽으로 한 칸 움직여 서로 상쇄된다. 동맹 축은 중립으로 두었고, AI·코인 축은 반박이다.
     - CBS '설득력 없다'와 테레비아사히 제목은 단일 출처·양면으로 옮겼다.
  3. **빠진 반박 증거 추가**
     - 미 주지사 선거의 데이터센터 반발(FT·WaPo·CNBC; 텍사스 인허가 중단 — Handelsblatt 블로그, 단일)
     - 나스닥 조정 진입(Handelsblatt), 마벨 목표가 하향, 골드만 '현금 비중 확대'
     - 반영한 곳: against, 산업·증시 분야, 피쉬본 n36과 링크 n36→n9
  4. **기보도 표기**
     - 마벨-루멘텀: 11-03 발표의 후속으로 표기했다.
     - 3자 회담: 11-03 위트코프 발표의 후속으로 표기하고, '확정'을 '예정'으로 바꿨다.
  5. **배경 사례 교체**: 하노이 사례를 1972년 '라인배커 II'로 바꿨다.
- **[권고] 12건 모두 반영**
  - 1: 셰플러는 ARD도 보도해 단일이 아니다. 출처에 de:7을 추가했다.
  - 2: EU·영국 무역 완화에 Guardian을 병기했다.
  - 3: 북극(그린란드 비준·스발바르)을 단일 출처로 support와 지정학 분야에 넣었다.
  - 4: 대중 포위선 반례(JD.com 인수 승인, ARD 단일)를 넣었다.
  - 5: 동맹 축을 '양면(판정 중립)'으로 표기하고 JPost 기사를 추가했다.
  - 6: 바이낸스 후속은 판정에 다시 세지 않는다고 명시했다. top10[6]과 kr[3]의 가설 연관은 '무관'으로 바꿨다.
  - 7: '최대 규모 중 하나'로 고쳤다.
  - 8: n32→n7 링크를 지웠다.
  - 9: '최소 7편'으로 고쳤다.
  - 10: cn[0]에서 SCMP와 [메시지]를 분리했다.
  - 11: 구글 안드로이드 사례를 '2018년 과징금(2015년 조사 착수)'으로 고쳤다.
  - 12: GMO를 11-03 회견 후속으로 표기하고, top10 순서를 중요도 순으로 바꿨다.
- `python template/verify.py 2026-11-04`: 통과(선별 뉴스 55건)
