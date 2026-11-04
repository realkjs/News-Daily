# 2026-11-05 임원 초안 검토 (팀장 검토 모드)

- 대상: `briefings/2026-11-05.json` (generated_at 2026-11-05 06:25 KST)
- 대조 자료: `data/work/2026-11-05/tmp/lead/digest.txt`(ORIG 원제·원요약), `data/raw/2026-11-04/`(브리핑 뒤 09:13 KST 재수집분, 아래 "11-04 raw 팀:인덱스"), `briefings/2026-11-02~04.json`
- 근거 표기: `팀:인덱스`는 digest 기준이다. 11-04 재수집분은 "11-04 raw 팀:인덱스"로 적는다.
- 주의: 팀장 선별 `_lead.json`의 top10을 초안이 그대로 옮겼다. 아래 F2·F3·F5·F6의 오류는 팀장 선별 단계에서 생긴 것이다. 팀장도 `_lead.json`을 같은 내용으로 함께 고친다.

## 0. 출처 추적 — `python template/verify.py 2026-11-05`

```
검증 통과: 선별 뉴스 55건의 출처가 모두 원자료에 있음, 피쉬본 구조 정상
```

- URL은 모두 원자료에 있다. 아래 지적은 **라벨·요약이 원문과 맞는지**에 관한 것이다.
- FT 요약 뒤바뀜(uk:41·uk:42) 확인 결과: 초안은 두 FT 기사를 **제목으로만** 인용한다(uk:41 = 밴스, uk:42 = 유가 100달러 아래). 뒤바뀐 요약을 다른 기사에 붙인 귀속 오류는 없다.

---

## [필수 수정]

### F1. 단일 출처 수치 '유가 8% 넘게'를 본질 문장과 헤드라인에 사실로 씀 — 점검 항목 2·3
- **위치**
  - `essence.headline`: "유가를 8% 넘게 끌어내리고(중앙일보·FT '100달러 아래')"
  - `top10[2].headline_ko`: "국제유가 8% 넘게 급락"
  - `fishbone.bones[monetary].items[n13].label`: "유가 8% 넘게 급락·100달러 아래"
  - `hypothesis_check.against[0]`: "유가 100달러 아래·8% 넘게 급락(FT·중앙일보·Telegraph)"
  - `hypothesis_check.note` ①: "유가를 100달러 아래로 끌어내렸다(FT·중앙일보·Telegraph)"
- **문제**
  - '8%'는 중앙일보 속보 제목 하나뿐이다. 05:09 KST 장중 수치라 종가인지도 확인되지 않는다.
  - '100달러 아래'는 FT 제목 하나뿐이다. 중앙일보·Telegraph는 이 수치를 쓰지 않았다.
  - 그런데 note와 against는 두 수치를 세 매체의 공동 근거처럼 묶었다.
  - `fields.monetary.counter`는 "8%는 단일"이라고 스스로 적었다. 본질 문장·헤드라인·판정 근거와 서로 모순된다.
  - 원칙 위반: 단일 출처 수치는 핵심 근거로 쓰지 않는다.
- **근거**
  - kr:64 중앙일보 "[속보] 美 민주당 압승에 국제유가 8% 넘게 급락" (제목만, 11-05T05:09)
  - uk:42 FT "Oil tumbles below $100 on post-election peace hopes" (제목)
  - uk:56 Telegraph "Oil prices plunge after Republicans suffer midterms defeat" (수치 없음)
- **고칠 문장**
  - 방향(급락)만 복수 출처로 쓴다. 예: "시장은 선거 결과를 평화 쪽으로 읽어 유가를 급락시켰다(FT·Telegraph·중앙일보; 수치는 FT '100달러 아래'·중앙일보 '8% 넘게' 모두 단일·장중)."
  - n13 라벨: "유가 급락(FT '100달러 아래', 단일 수치)"
  - top10[2] 헤드라인: "국제유가 급락(8%는 단일 속보)"
  - note ①: "(FT 제목 '100달러 아래'; Telegraph·중앙일보는 급락)"

### F2. 미시시피 '재검표 가능성'을 ABC·CNN에 귀속한 것 — ABC 원문은 반대 내용 — 점검 항목 1·2
- **위치**
  - `top10[0].why`: "미시시피 상원은 수십 표 차 초접전·재검표 가능성(CNN·ABC·YTN)"
  - `essence.derivation.decomposition`: "미시시피 상원 초접전·재검표 가능성(CNN·ABC·YTN)"
  - `fields.forecast.phenomenon`: "미시시피 상원 수십 표 차 초접전·재검표(CNN·ABC·YTN)"
  - `fields.forecast.scenarios[기본].signal`: "미시시피 재검표 결과"
  - `watch[0]`: "미시시피·알래스카 상원 확정과 재검표"
- **문제**
  - ABC 요약은 "미시시피 선거법에는 자동 재검표나 요청 재검표 규정이 없다"고 썼다. 원문을 반대로 읽었다.
  - CNN은 "어떻게 뜻밖의 격전지가 됐나"라는 제목뿐이다. 표차나 재검표 내용이 없다.
  - '수십 표 차'는 YTN 제목 하나뿐이다.
  - Fox는 표 다툼이 소송전(법률팀)으로 가고 있다고 썼다.
- **근거**
  - us:30 ABC "What to know about recounts in Mississippi with razor-thin margin in Senate race || … Mississippi election law does not provide for automatic or requested recounts."
  - us:1 CNN "How Mississippi became an unlikely Senate battleground" (제목만)
  - kr:28 YTN "공화 텃밭 미시시피 상원 수십표차 초접전...알래스카도 아직"
  - us:15 Fox "… Marc Elias' law firm prepares for a legal fight as the Mississippi Senate race remains uncalled."
  - uk:49 Guardian "Senate contests in Mississippi and Alaska are still too close to call"
- **고칠 문장**
  - "미시시피 상원은 초박빙으로 미확정(ABC·Guardian; '수십 표 차'는 YTN 제목 단일). ABC는 미시시피 법에 자동·요청 재검표 규정이 없다고 했고, 양측은 법정 다툼을 준비한다(Fox). 알래스카도 미확정(YTN·Guardian)."
  - signal·watch의 '재검표'는 "미시시피 개표 확정·소송 여부"로 바꾼다.

### F3. 같은 기사 묶음 안의 '지지' 증거를 '반박'으로 태깅, 정책 고수 보도 누락 — 점검 항목 6
- **위치**
  - `by_country.de[2]`: n-tv "이란은 다시 공격할 것" → `hypothesis: "반박"`
  - `by_country.fr[4]`: France 24 "그만한 가치 있었다" + 슈머 → "반박"
  - `by_country.ru[0]`: Vesti "언제든 끝낼 준비" + Interfax "모두 옳았다" → "반박"
  - `top10[1]`·`by_country.us[1]`: 밴스 비판 + 트럼프 '전쟁 옹호' → "반박"
  - `hypothesis_check.support[0]`
- **문제**
  - '다시 공격할 것', '그만한 가치', '모두 옳았다'는 초안 자신이 `support[0]`에 지지 증거로 올린 발언이다. 같은 발언이 담긴 국가별 항목이 '반박'으로 태깅돼 있다.
  - 정책을 고수한다는 보도가 복수 매체에서 나왔는데 support에 빠졌다(Die Zeit·ZDF·WELT, Interfax 요약의 직접 인용). 그래서 지지 쪽이 'France 24 제목' 같은 약한 근거로만 보인다.
- **근거**
  - de:30 n-tv "Trump gibt JD Vance "weitgehend" recht - würde Iran aber wieder angreifen"
  - de:72~74 Die Zeit "Donald Trump will trotz Vance' Kritik an Iranpolitik festhalten || … Pete Hegseth soll im Amt bleiben."
  - de:10 ZDF 요약 "Trump verteidigt den Krieg trotz der Niederlage."
  - de:32 WELT 요약 "Vance … legt nahe, dass dieser es nicht wert gewesen sei. Trump reagierte ungehalten."
  - ru:39 Interfax 요약 "«Я бы ничего не стал менять» — сказал Трамп журналистам в Белом доме"
  - fr:4 France 24 "la guerre en Iran "valait la peine" malgré la défaite électorale, juge Donald Trump"
- **고칠 문장**
  - de[2]의 `hypothesis`는 "지지"로 바꾼다.
  - fr[4]·ru[0]·top10[1]·us[1]은 항목을 나눈다. 정책 고수 = 지지, 정치적 비용 인정·슈머 = 반박. 스키마상 나누기 어려우면 "무관"으로 두고 why에 "양면"을 적는다.
  - `support[0]` 끝에 덧붙인다: "트럼프는 밴스의 비판에도 이란 정책을 고수(Die Zeit)·전쟁 옹호(ZDF·ABC)·'아무것도 바꾸지 않겠다'(Interfax 요약), WELT '밴스 발언에 불쾌한 반응' — 정책 고수는 복수 출처."

### F4. 단일 출처 기준을 지지·반박에 비대칭으로 적용 — 점검 항목 3·6
- **위치**
  - `hypothesis_check.against[0]`: "상원 민주당 대표 '이란 전쟁은 끝나야'(franceinfo)", "트럼프 '언제든 끝낼 준비'([관영] Vesti)"가 "(복수)" 판정 근거 묶음 안에 있다.
  - `hypothesis_check.support[1]`: 후티 주장(관영)·Reuters 제재(제목)·한국경제TV 이란 안보수장(제목)을 "판정 근거는 복수 출처 항목만"이라며 뺐다.
- **문제**
  - 11-03 브리핑 원칙은 "단일 매체 제목은 양쪽 모두 판정 근거에서 뺀다"였다.
  - 지지 쪽에서는 Reuters 단일 제목(대이란 제재)을 뺐다. 반박 쪽에서는 franceinfo 단일 제목(슈머)과 관영 단일(Vesti)을 판정 근거로 넣었다.
  - Vesti는 관영 매체다. 다른 매체가 확인하지 않은 트럼프 발언 전달이므로 "메시지"로 읽어야 한다.
- **근거**
  - fr:13 franceinfo (슈머 발언, 다른 매체에 없음). de:44 Handelsblatt의 슈머 언급은 '다수당 원내대표 선출 기대'뿐이고 이란 발언이 아니다.
  - ru:11 Vesti[관영] "Трамп заявил о готовности завершить войну с Ираном в любой момент" (단일)
  - uk:39 Reuters 제재 (제목 단일)
- **고칠 문장**
  - against[0]에서 슈머·Vesti를 떼어 "단일·관영·제목(판정 근거 제외): 슈머 '이란 전쟁은 끝나야'(franceinfo 단일), 트럼프 '언제든 끝낼 준비'([관영] Vesti 단일 — 메시지)" 항목으로 옮긴다.
  - note 끝의 제외 목록에도 두 건을 더한다.

### F5. 기보도 사건을 지지 증거로 다시 셈 — BBC '이중 폭격'·키이우 정전 — 점검 항목 4·6
- **위치**
  - `hypothesis_check.support[0]`: "키이우 정전 지속(Vesti 관영·RBC), BBC 러시아 이중 폭격" ("분쟁 지속 신호(복수)" 묶음)
  - `top10[5].why`: "BBC: 우크라이나 '보디캠 영상이 러시아의 치명적 이중 폭격 보여줘'"
  - `fields.geopolitics.phenomenon`
  - `by_country.ru[4]`: 키이우 정전, "지지"
- **문제 1 — BBC 이중 폭격**
  - BBC 기사는 '월요일(11-02)' 공격을 다룬다. 이는 11-03 브리핑이 지지로 센 자포리자 구호품 배급소 폭격(26명, 같은 날 BBC '3,000kg급 폭탄 9발')과 같은 사건으로 보인다.
  - 11-04 브리핑은 "자포리자 사망자 갱신(33명)은 다시 세지 않는다"고 정했다.
  - 오늘 BBC 기사는 사망자를 40명으로 갱신하고 영상을 공개한 후속 보도다. 사망자 수 추이도 26 → 33 → 40으로 이어진다.
- **문제 2 — 키이우 정전**
  - 11-04 브리핑이 지지로 센 '최대 규모급 에너지 공격 — 키이우 정전·단수'의 여파다.
- **근거**
  - uk:1 BBC "Ukraine says bodycam video shows deadly Russian double-tap bombing || At least 40 people were killed and another 30 may still be under the rubble after Monday's attack on a Ukrainian village"
  - 11-04 raw fr:34 Le Monde "au moins 33 morts au lendemain d'une attaque russe contre un centre de distribution d'aide humanitaire dans la région de Zaporijia"
  - 11-04 raw uk:37 Reuters "Russia bombards Ukraine power grid before Abu Dhabi talks"
  - ru:10 Vesti[관영], ru:65 RBC (도로 봉쇄)
  - 11-04 브리핑 note ②
- **고칠 문장**
  - support[0]에서 두 건을 빼고 따로 적는다: "기보도 후속(다시 세지 않음): 11-02 자포리자 구호소 폭격 사망자 40명으로 갱신·보디캠 공개(BBC), 11-04 에너지 공격 여파 키이우 정전·도로 봉쇄([관영] Vesti·RBC)."
  - top10[5]의 BBC 문장 뒤에 "(11-03 기보도 사건의 후속, 사망자 40명으로 갱신)"을 붙인다.

### F6. 올레시키를 다시 '반박'으로 셈, DW 원문의 반대 평가 누락 — 점검 항목 2·4·6
- **위치**
  - `hypothesis_check.against[0]`: "우크라이나: 올레시키 모델 확대(Le Monde·DW)·워싱턴 인도주의 회동(Meduza)·크렘린 '평화 노력 계속하길'"
  - `hypothesis_check.note` ②
  - `top10[5].hypothesis = "반박"`, `by_country.fr[3]`·`ru[2]` = "반박"
  - `fields.geopolitics.scenarios[기본]`
- **문제 1 — 같은 사건을 다시 셈**
  - 올레시키 휴전·대피는 11-01·11-02에 '미국 중재 성공'으로 이미 반박에 셌다.
  - 11-03은 "종료를 따로 세지 않는다"는 원칙을 세웠다.
  - 오늘 새로 나온 것은 ⓐ 우크라이나의 '다른 곳에도 재현' 의향(Le Monde)과 ⓑ 워싱턴 회동 예정(Meduza의 페스코프 발언 전달)뿐이다. 둘 다 계획 단계다.
- **문제 2 — DW를 한쪽만 인용**
  - DW 요약은 "러시아가 휴전을 군사적 위치 강화에 썼다는 경고"를 함께 적었다. 초안은 DW를 '평화로 가는 첫걸음?'(제목)으로만 인용해 반박 근거로 썼다.
- **문제 3 — 크렘린 발언의 성격**
  - 크렘린의 '평화 노력 계속하길'은 상대국 정부의 메시지다. 평화의 사실 증거가 아니다.
- **근거**
  - de:16 DW "Oleschky-Mission als erster Schritt zum Frieden? || … Manche Beobachter sprechen von einer erfolgreichen humanitären Mission, andere warnen, Russland habe die Waffenruhe genutzt, um seine militärische Position zu stärken."
  - fr:35 Le Monde "L'Ukraine veut répliquer ailleurs …"
  - ru:50 Meduza "… Об этом заявил пресс-секретарь Владимира Путина Дмитрий Песков"
  - ru:55 Meduza (크렘린)
  - 11-02 note ②, 11-03 note ②
- **고칠 문장**
  - against[0]의 우크라이나 부분을 다음으로 바꾼다: "🔎 양면(판정 중립): 올레시키 모델을 다른 곳에 재현하려는 의향(Le Monde)·워싱턴 인도주의 회동 예정(Meduza, 페스코프 발언) — 11-01·11-02에 반박으로 센 사건의 후속이라 새로 세지 않는다. DW는 '러시아가 휴전을 군사적 위치 강화에 썼다'는 경고를 함께 전했다. 크렘린 '평화 노력 계속하길'은 [메시지]."
  - 이에 맞춰 top10[5]·fr[3]·ru[2]의 hypothesis를 "무관"으로 바꾼다.

### F7. 시점 오류 — 선거 전에 이미 있던 '공습 계획 없음'·유가 하락을 선거 효과로 계산 — 점검 항목 4·6 (11-04 재수집분)
- **위치**
  - `hypothesis_check.note` ①: "반박 쪽으로 크게 움직였다 … 미국 유권자가 처음으로 반대 증거를 냈다"
  - `fields.monetary.essence`: "선거가 그 프리미엄을 하루 만에 깎았다"
  - `fields.monetary.cause`
  - `essence.headline`: "시장은 이를 평화 쪽으로 읽어"
- **문제 1 — 선거 전 신호**
  - 11-04 브리핑 뒤 재수집된 원자료에 따르면 트럼프는 투표 마감 몇 시간 전에 이미 FT에 "당장 이란을 칠 계획이 없다"고 했다. RIA는 "새 공습 계획 없다", "농축 우라늄 협상 계속"을 전했다.
  - 유가도 선거 전에 미·이란 협상 기대로 이틀 연속 떨어지고 있었다(Bloomberg·닛케이).
  - 11-03 브리핑은 그날의 유가 급락(7%대)을 이미 반박으로 셌다.
  - 따라서 '평화 기대'와 유가 하락은 선거가 처음 만든 신호가 아니다. 선거 전 협상 국면의 연장선 위에 선거가 더해진 것이다.
  - Vesti '언제든 끝낼 준비'도 같은 선거 전 입장의 연장으로 봐야 한다.
- **문제 2 — 11-04 축별 판정과의 일관성**
  - 11-04는 케슘섬 타격으로 이란 축을 '지지 쪽 한 칸' 옮겼다.
  - 오늘은 정치적 비용 인정만으로 '크게 반박'이라 했다. 하지만 정책은 바뀌지 않았고(F3), 유권자의 정치적 비용 인정은 11-02~11-04의 축 판정 기준(무력 신호 vs 협상 신호)에 없던 새 범주다.
- **문제 3 — 11-04 감시 항목을 닫지 않음**
  - 11-04 watch에 '이르면 수요일 공습' 보도의 사실 여부가 있었다. 오늘 원자료에는 미국의 대이란 공습 보도가 없다. 초안은 이 항목을 닫지 않았다.
- **근거**
  - 11-04 raw uk:41 FT "US has no immediate plan to strike Iran, Trump tells FT || President says position with Tehran is 'brilliant' in interview just hours before midterm polls close" (11-04T08:34 KST)
  - 11-04 raw ru:31 RIA[관영] "Трамп заявил об отсутствии планов наносить новые удары по Ирану"
  - 11-04 raw ru:28 RIA[관영] "США продолжают переговоры с Ираном по обогащенному урану"
  - 11-04 raw us:50 Bloomberg "Oil fluctuated after a two-day decline as traders weighed conflicting signals on the trajectory of US-Iran peace talks."
  - 11-04 raw jp:55 닛케이 "NY商品、原油続落 米イランの交渉が進展するとの見方"
  - 11-04 raw il:35 Ynet "US prepared to strike Iran as early as Wednesday …"
  - 11-04 raw ru:33 Interfax(NYT 인용)
  - digest 전체에 미국의 대이란 공습 보도 없음
- **고칠 문장**
  - note ①: "① 이란 축: 반박 쪽으로 한 칸. 대통령·부통령이 전쟁의 선거 비용을 인정했지만(복수), 트럼프는 정책 고수·재공격 가능성을 말했다(Die Zeit·ZDF·n-tv·Interfax). 선거 전부터 트럼프는 '당장 공습 계획 없음'(11-04 FT·[관영] RIA)이라 했고, 유가도 협상 기대로 이미 내려가고 있었다(11-04 Bloomberg·닛케이; 11-03 반영분). 오늘의 유가 급락은 그 흐름이 선거로 가속된 것이지 새 전환점은 아니다. 11-04에 보도된 '이르면 수요일 공습'은 오늘 원자료에 실행 보도가 없다."
  - monetary.essence: "선거가 그 프리미엄을 하루 만에 깎았다" → "선거 전부터 이어진 협상 기대에 선거 결과가 더해져 프리미엄이 더 깎였다(해석)"

### F8. 메타 유로화 채권의 '달러 밖 조달' 해석 — 11-04 재수집분에 반대 증거가 있음 — 점검 항목 4·6
- **위치**
  - `hypothesis_check.against[1]`: "단일: 메타의 첫 유로화 채권으로 AI 자금 조달(KBS 제목) — 연산력 자금이 달러 밖에서도 조달된다는 신호"
  - `fields.business.cause`: "AI 자금 조달은 달러 밖(유로화 채권) 시장으로도 넓어진다"
  - `top10[3].why` 끝 문장
- **문제**
  - 11-04 재수집분에 따르면 메타는 같은 주에 미국 달러 채권 150억 달러(5개 트랜치)를 먼저 발행했다.
  - 유로화 채권은 달러 조달을 보완한 것이다. 이를 '달러 밖으로 넓어진다'는 가설 균열 신호로 쓰면 증거를 반대로 읽게 된다.
  - 유로화 채권 기사도 KBS 제목 하나뿐이다.
- **근거**
  - 11-04 raw uk:33 Reuters "Meta raises $15 billion in five-part US bond sale" (11-04T07:55 KST)
  - kr:0 KBS "메타, 인공지능 투자금 마련 집중…첫 유로화 채권 13.6조 원 발행" (제목만)
- **고칠 문장**
  - against[1] 끝: "메타는 같은 주 달러 채권 150억 달러를 먼저 발행했고(11-04 Reuters), 첫 유로화 채권(KBS 제목, 단일)은 그 보완이다. 연산력 자금의 달러 시장 의존을 보여 주는 쪽(지지)에 가까워 균열 근거에서 뺀다."
  - business.cause의 해당 문장은 "AI 자금 조달은 달러 채권을 중심으로 통화를 다변화한다(해석)"로 바꾼다.

### F9. 본질 문장 '두 엔진에 브레이크'의 반박 증거 누락 — '대외 권한은 그대로'라는 복수 보도 — 점검 항목 6·7
- **위치**
  - `fishbone.head`, `essence.derivation.assumptions`(통념 3 "의회가 바뀌어도 대통령의 전쟁 권한은 그대로다"), `essence.derivation.rebuild`, `fields.geopolitics.counter`
- **문제**
  - 초안은 통념 3을 의심할 가정으로 내걸었다. 그러나 오늘 원자료의 여러 매체는 오히려 통념 3을 지지한다. 국내 권한은 줄지만 대외·전쟁 정책은 대통령 손에 남고, 더 공격적으로 될 수 있다는 것이다.
  - 이 반론이 rebuild·head에 없다. 그래서 '전쟁 엔진에 브레이크'가 사실처럼 읽힌다.
  - 원칙 위반: 반박 증거는 반드시 표기한다.
- **근거**
  - uk:7 BBC Bowen "Trump's loss limits powers at home, but it will likely be different abroad || … will want to show he can still shake the world"
  - uk:0 BBC Mason "… does defeat at home make it more likely that President Trump gets angrier abroad?"
  - de:21 DW "Doch in der Außenpolitik bleibt Donald Trump ein Machtfaktor."
  - de:53 Spiegel "»Donald Trump kann jetzt gefährlich werden«"
  - kr:52 한국경제TV "트럼프, 대외정책서 폭주하나…이란공격·추가관세 우려"
  - cn:13 CGTN[관영] 프랑스 재무장관 "on international issues, President Trump will remain in charge"
  - de:63 FAZ "Trumps Macht schwindet, seine Zölle bleiben"
- **고칠 문장**
  - rebuild 끝에 덧붙인다: "반론(복수): 국내 권한은 줄지만 대외 정책은 여전히 대통령 손에 있고(BBC Bowen·DW·[관영] CGTN의 프랑스 재무장관), 국내 패배가 대외 강경으로 이어질 수 있다(BBC Mason·Spiegel·한국경제TV). 브레이크는 '국내 엔진'에 걸렸을 뿐 '전쟁 엔진'에 걸렸는지는 아직 확인되지 않았다."
  - fishbone.head: "…유권자가 브레이크를 걸었다 — 대통령은 비용을 인정했지만 대외 권한과 전쟁 정책은 그대로다"

---

## [권고]

### R1. 헤그세스 거취의 비중 — 트럼프 본인의 직접 발언이 '경질 검토' 보도보다 무겁다
- **위치**: `top10[6].why`, `fields.legislation.phenomenon/cause/counter/precedent`, `by_country.il[2]`
- **근거**
  - '경질 의사 없다' 쪽(직접 발언·복수)
    - ru:37 Interfax 요약 "Трамп заявил, что доволен работой … Хегсета и не рассматривает вопрос о его отставке" — 기자들에게 한 직접 발언이다.
    - de:72 Die Zeit "Pete Hegseth soll im Amt bleiben"
    - us:8 Fox "… but Trump isn't budging yet"
  - '경질 검토' 쪽은 모두 "report" 인용이다: il:30 JPost, il:2 i24, uk:74 Independent, ru:61 Vedomosti '~할 수도'.
- **제안**
  - "트럼프는 기자들에게 헤그세스에 만족하며 경질을 검토하지 않는다고 했다(Interfax 요약; Die Zeit·Fox도 유임으로 전함). 경질 검토는 익명 보도 인용(JPost·i24·Independent)."
  - legislation.cause의 럼스펠드 유비에는 "다만 트럼프는 직접 부인"을 앞세운다.

### R2. 밴스 불출마 언급을 '단일'로 잘못 표기, 트럼프 반응의 결
- **위치**: `fields.forecast.counter`("밴스의 대선 불출마 언급은 Vedomosti 제목 단일이다"), `essence.headline`
- **근거**
  - de:32 WELT "Mit einem einzigen Satz setzt Trump ein großes Fragezeichen hinter Vances politische Zukunft || … legt nahe, dass dieser es nicht wert gewesen sei. Trump reagierte ungehalten."
  - ru:57 Vedomosti
- **제안**
  - counter: "밴스의 정치적 미래에 대한 트럼프의 의문 제기는 Vedomosti·WELT 2건"
  - essence.headline의 "그러면서도 트럼프는 '그만한 가치'" 앞에 "밴스가 전쟁이 '그럴 가치가 없었다'는 뜻을 비치자(WELT)"를 넣는다. 그러면 '그만한 가치'가 밴스에 대한 반박이라는 점이 드러난다.

### R3. 적대국 정부 발언에 [메시지] 표기
- **위치**: `by_country.us[4]`(이란 지도부, AP, "반박"), `top10[4]`·`by_country.ru[1]`·`kr[3]`(크렘린)
- **근거**: us:55 AP(이란 지도부 발언 보도, 단일), ru:55 Meduza(페스코프)
- **제안**
  - us[4] 헤드라인에 "[메시지]"를 붙이고 hypothesis를 "무관"으로 바꾼다.
  - 크렘린 항목에도 "[메시지] — 러시아 정부가 원하는 미국 중재의 지속"을 붙인다.
  - 요미우리(jp:66)의 "중·러는 트럼프 외교 '유지'에 기대"와 짝지으면 해석이 선명해진다.

### R4. '동맹 축 균열' 분류
- **위치**: `hypothesis_check.against[2]`
- **문제**
  - 게이단렌 회장의 '관세에 일정한 제동이 걸리길'(jp:64)은 미국 정책이 수정되기를 바라는 것이다. 미국에서 이탈한다는 신호가 아니다.
  - 캐나다 발언은 SCMP 단일(cn:32)이다. FT 'Cartwheels'(uk:44)는 반응 기사이고 '의존 축소' 근거가 아니다.
- **제안**: "동맹 축(단일): 캐나다 '대미 의존 축소 계속'(SCMP 단일). 게이단렌은 이탈이 아니라 관세 수정 기대(요미우리)라 판정 근거에서 뺀다."

### R5. AI 축 — 반대 증거 보강, '처음으로' 삭제
- **위치**
  - `fields.stocks.essence`: "처음으로 정치 변수로 할인"
  - `fishbone.head`·`essence.derivation.rebuild`: "처음으로 … 브레이크"
  - `fields.industry.counter`, `hypothesis_check.against[1]`
- **근거 — '처음으로'가 맞지 않는 이유**
  - 정치 변수는 11-04 브리핑에서 이미 다뤘다: 11-04 raw uk:43 FT "Investors watch US state races for signs of backlash against AI boom", 11-04 브리핑의 CNBC '텍사스 결과가 AI 트레이드에 타격'.
- **근거 — 빠진 반대 증거**
  - uk:45 FT 요약 "Midterm results could affect 45 per cent of planned expansion, but there is a silver lining for investors" — 45%는 단일 수치이고, 투자자에게 좋은 면도 있다고 했다.
  - us:43 CNBC "a bubble deflating gradually is better than a pop"
  - 11-04 raw us:47 CNBC "AMD stock jumps 8% … data center revenue nearly doubles"
  - 11-04 raw uk:39 Reuters "Nasdaq ends higher as AI heavyweights rebound"
- **단일 표기 누락**
  - 'AI주 하락'은 Handelsblatt(de:41) 단독, '데이터센터주 급락'은 Reuters(uk:35) 단독이다.
  - SCMP AI 분석(cn:39)도 단일이다. 그런데 셋 다 against[1]의 "(복수)" 묶음 안에 있다.
- **제안**
  - '처음으로'를 삭제한다.
  - counter에 FT '45%·투자자에게 좋은 면'과 AMD 데이터센터 매출 급증을 넣는다.
  - 주가·SCMP 항목에는 "각 단일"을 표기한다.

### R6. 후티 '킹칼리드·리야드 국제공항'은 같은 공항일 가능성
- **위치**: `top10[8]`, `hypothesis_check.support[1]`, `fields.geopolitics.phenomenon`, `by_country.cn[0]`
- **근거**: cn:7 CCTV "哈立德国王国际机场"(킹칼리드 국제공항), cn:22 Xinhua "利雅得国际机场"(리야드 국제공항)
- **문제**: 킹칼리드 국제공항은 리야드의 공항이다. 두 관영 매체가 같은 후티 주장을 전한 것인데, "킹칼리드·리야드 국제공항 등"이라고 쓰면 공항 두 곳으로 읽힌다.
- **제안**: "후티 '사우디 킹칼리드(리야드) 국제공항 등 타격' 주장 — 중국 관영 2건이 같은 후티 발표를 전달(원 출처 1)"

### R7. 김여정 담화는 '후속'이 아니라 재보도
- **위치**: `fields.crypto.phenomenon`, "TV도쿄: 김여정 '황당무계한 유언비어' — 바이낸스 부정 접속(11-04 기보도의 후속)"
- **근거**
  - jp:43 TV도쿄(11-05T00:26)는 11-04 브리핑이 이미 반영한 '황당무계' 담화와 같은 내용이다.
  - 11-04 raw kr:16 SBS "김여정, 바이낸스 사태에…"(11-04T08:54), 11-04 raw uk:34 Reuters "North Korea denies Binance accusation"
- **제안**: "(11-04 기보도 담화의 일본 매체 재보도 — 새 사실 없음)"이라고 쓰거나 삭제한다.

### R8. 억지 연결 삭제 — 피쉬본 링크 n33→n34
- **위치**: `fishbone.links[11]` (후티 사우디 공항 → 미국 이란 지원 기업 제재)
- **문제**: logic 문장이 스스로 "두 사건을 잇는 원문은 없다"고 적었다. 관영 주장과 Reuters 제목을 병치한 것이다.
- **제안**: 링크를 삭제한다. 대신 원자료가 직접 잇는 연결 하나로 바꾼다(R9 참조).

### R9. 놓친 연결 — 프랑스 혈액은행 공격은 유럽 슈퍼마켓 냉장고 해킹과 같은 수법
- **위치**: `fields.business`, `top10[7]`
- **근거**
  - jp:18 TBS "血液バンクも標的に…冷蔵室の温度が引き上げられる"(혈액은행도 표적, 냉장실 온도가 올라감)
  - fr:23 TF1 "Santé, supermarchés... des pirates sans limite"
  - 11-04 raw kr:47 연합뉴스 "英·獨도 냉장고 온도 50도로…유럽 11개국 번진 마트 해킹"
  - 11-03 브리핑 watch '유럽 슈퍼마켓 사이버 공격의 배후'
- **제안**
  - "혈액은행 공격은 냉장실 온도를 올리는 수법으로, 10월 프랑스 슈퍼마켓에서 시작해 유럽 11개국으로 번진 냉장고 해킹(11-04 연합뉴스)이 의료 인프라로 옮겨 간 것으로 보인다(TBS·TF1)."
  - 피쉬본 링크 n6(아르케아)와 사이버 항목의 연결로 쓴다.

### R10. 기타 누락 뉴스
- **지지 쪽**
  - 11-04 raw us:67 NYT "More Iranians Call for Nuclear Weapons After War With U.S." — 11-04 브리핑 뒤 재수집분이다. 전쟁 이후 이란에서 핵무장론이 커진다는 보도로, 분쟁 장기화 쪽 근거다.
- **기술**
  - uk:84 Economist "With an eye on America, China is beefing up its AI-controlled labs" — SCMP의 '미국 AI 둔화가 중국에 유리'와 짝을 이루는 근거다.
- **대중 포위선 반례**
  - kr:63 조선일보 "'대체 조달처 없다' 삼성전자, 중국 LCD 가격 인상에 TV 적자 장기화 우려" — 중국이 공급망을 지렛대로 쓴다는 신호다.
- **유럽 '총이냐 버터냐'**
  - kr:60·61 조선일보, kr:27 YTN: 덴마크 학생 시위, '국방비 증액으로 교육 예산 삭감'
  - 프랑스 11월 5일 총동원(생활비)과 독일 Z세대 시위와 함께 묶을 수 있다.

### R11. 표기 — '라트라토바'는 '란트라토바'
- **위치**: `top10[5]`, `by_country.ru[2]`, geopolitics
- **근거**: ru:50 "Яна Лантратова"(얀나 란트라토바). 11-02 브리핑도 "란트라토바"로 적었다.

### R12. 라인메탈 '올해 무산'은 과장
- **위치**: `by_country.de[1].headline_ko` "연방군 전차 대형 수주 올해 무산"
- **근거**: de:43 Handelsblatt 요약 "Rheinmetall rechnet in diesem Jahr nicht mehr mit einem Panzer-Großauftrag der Bundeswehr. Auch eine Marschflugkörper-Kooperation liegt hinter den Zielen zurück. Der Aktienkurs reagiert deutlich."
- **제안**: "연방군 전차 대형 수주를 올해는 더 기대하지 않음, 순항미사일 협력도 목표 미달, 주가 급반응(Handelsblatt 단일)"

### R13. 출처 귀속 — 엘사예드 '무기 판매 중단' 항목의 i24
- **위치**: `by_country.il[4].sources`
- **근거**: il:1 i24는 '엘사예드 승리가 미국 유대인에게 갖는 의미' 분석 기사다. 무기 판매 중단 촉구는 il:38 Ynet에만 있다.
- **제안**: why를 "Ynet(단일); i24는 관련 분석"으로 고친다.

### R14. 콜린스 패배 보도의 확인 수준
- **위치**: `top10[0].why`, `essence.derivation.decomposition`
- **근거**
  - cn:15 CGTN[관영](CNN 예측 인용)이 유일한 결과 보도다.
  - cn:36 SCMP "Who won in China? … Susan Collins and the local firefighters"는 메인주 차이나(China) 타운의 지역 결과를 다룬 기사로 읽힌다. 주 전체 결과와 혼동하지 않도록 쓰지 않는다.
  - 11-04 raw us:6 CNN "Former Susan Collins supporters explain votes for Troy Jackson"은 유권자 인터뷰다. 결과를 확인하지 않는다.
- **제안**: 지금처럼 '단일 전달'로 둔다. watch에 "메인주 상원 결과 확인"을 넣는다.

### R15. 배경 사례 — 2018년 탄핵 조사의 시점
- **위치**: `fields.legislation.precedent` "2018년 민주당 하원 탈환 뒤 트럼프 탄핵 조사"
- **문제**
  - 탄핵 조사는 2019년 9월 우크라이나 통화 건으로 시작됐다. 선거 직후의 '조사 의제'와는 시점과 계기가 다르다.
  - 오늘의 '가족 조사' 의제와 바로 비교하려면 "2019년 하원의 소환장·청문회 공세"가 더 정확하다.
- **나머지 사례 점검**: 오류를 찾지 못했다.
  - 2006년 럼스펠드 사임(선거 다음 날)
  - 1991년 1월 공습 개시 뒤 유가 폭락
  - 1968년 구정 공세 → 존슨 불출마·파리 협상
  - 2016년 방글라데시 8,100만 달러
  - 2021년 콜로니얼 파이프라인
  - 2011년 신용등급 강등

### R16. 형식
- **위치**: `essence.headline`
- **문제**: 스키마는 "오늘의 본질 한 문장"인데 다섯 문장이다.
- **제안**
  - 본질 문장: "미국 유권자가 전쟁 비용과 데이터센터 비용을 함께 거부해 민주당에 양원을 넘겼지만, 대통령은 비용을 인정하면서도 이란 정책을 바꾸지 않았다(복수)."
  - 시장 반응 문장은 derivation으로 내린다.

---

## 요약

- **[필수 수정] 9건**
  - F1 유가 8%(단일)를 본질·헤드라인에 사용
  - F2 미시시피 재검표 오귀속(ABC 원문은 반대 내용)
  - F3 지지 증거를 '반박'으로 태깅, 정책 고수 보도 누락
  - F4 단일 기준 비대칭
  - F5 자포리자·키이우 정전 재계산
  - F6 올레시키 재계산, DW 경고 누락
  - F7 선거 전 '공습 계획 없음'·유가 하락을 선거 효과로 계산(11-04 재수집 FT·Bloomberg)
  - F8 메타 유로채 해석(11-04 재수집 Reuters 150억 달러 채권)
  - F9 '대외 권한은 그대로'라는 복수 반론 누락
- **[권고] 16건** (R1~R16)
- **판정 '약화' 자체에 대한 의견**: AI·코인 축만으로도 유지할 수 있다. 다만 이란 축은 "크게 반박"이 아니라 "반박 쪽 한 칸"으로 고친다(F3·F4·F7). 우크라이나 축은 지지(F5)와 반박(F6) 양쪽에서 재계산을 빼면 "상쇄·보류"가 된다.

판정: 수정 필요

---

## 반영 결과 (임원 최종)

[필수 수정] 9건 모두 반영했다. 팀장 선별 `_lead.json`도 함께 고쳤다.

1. **F1 유가 수치:** 본질 문장·top10[2]·n13·판정 근거에서 수치를 '각 단일'로 표기했다. 방향(급락)만 복수 출처로 썼다.
2. **F2 미시시피 재검표:** ABC 원문대로 '재검표 규정 없음', Fox의 '법정 다툼 준비'로 고쳤다. YTN은 단일로 표기했다. signal과 watch의 '재검표'는 '개표 확정·소송 여부'로 바꿨다.
3. **F3 정책 고수 보도:** Die Zeit·ZDF·WELT·Interfax의 정책 고수 보도를 support[0]·top10[1]·분해·재구성에 넣었다.
   - de[2]는 '지지'로 바꿨다.
   - top10[1]·us[1]·fr[4]·ru[0]는 '무관(양면)'으로 바꿨다.
4. **F4 단일 출처:** 슈머(franceinfo)와 Vesti(관영) 발언을 '단일·관영·제목(판정 근거 제외)' 항목으로 옮겼다. 이란 지도부 발언에는 [메시지]를 붙였다.
5. **F5 기보도 사건:** BBC 이중 폭격(사망자 40명으로 갱신)과 키이우 정전을 '기보도 후속(다시 세지 않음)'으로 분리했다. ru[4]는 '무관'으로 바꿨다.
6. **F6 올레시키:** '양면(판정 중립)'으로 바꾸고 DW의 경고를 넣었다. top10[5]·fr[3]·ru[2]는 '무관'으로 바꿨다.
7. **F7 선거 전 신호:** 11-04 재수집분의 FT '당장 공습 계획 없음'과 Bloomberg·닛케이 '이틀 연속 하락'을 넣었다.
   - 이란 축은 '반박 쪽 한 칸'으로, 통화 분야 본질은 '기존 흐름의 가속'으로 고쳤다.
   - '이르면 수요일 공습'은 실행 보도가 없다고 명시했다.
8. **F8 메타 채권:** 달러 채권 150억 달러를 먼저 발행했다고 명시했다. 유로화 채권은 반박 근거에서 빼고 지지 쪽 간접 근거로 옮겼다.
9. **F9 대외 권한 반론:** BBC Bowen·Mason, DW, Spiegel, 한국경제TV, [관영] CGTN의 반론을 재구성·지정학 분야 반론·피쉬본 머리·n36(링크 n36→n26)에 넣었다.

[권고] 16건 중 15건을 반영했다.

- **R1:** 헤그세스 거취는 트럼프의 직접 부인을 앞에 두었다.
- **R2:** 밴스 건은 WELT를 병기했다.
- **R3:** 크렘린·이란 발언에 [메시지]를 붙였다.
- **R4:** 동맹 축은 단일 출처로 정리하고, 게이단렌 발언은 판정 근거에서 뺐다.
- **R5:** '처음으로'를 삭제했다. FT 45%(단일)와 CNBC의 반대 측면, 주가·SCMP 항목의 '각 단일' 표기를 넣었다.
- **R6:** 킹칼리드(리야드) 국제공항은 원 출처 1건임을 밝혔다.
- **R7:** 김여정 담화는 재보도로 표기했다.
- **R8:** n33→n34 링크를 지웠다.
- **R9:** 혈액은행 냉장실 공격과 마트 해킹 수법을 연결했다(n7→n6, 사이버 항목).
- **R11:** 란트라토바 표기를 고쳤다.
- **R12:** 라인메탈 표현을 바로잡았다.
- **R13:** 엘사예드 건의 출처 귀속을 고쳤다.
- **R14:** watch에 메인주 상원 확인을 추가했다.
- **R15:** 배경 사례를 2019년 하원의 소환장·청문회 공세로 바꿨다.
- **R16:** 본질 문장을 한 문장(대시로 이은 두 절)으로 줄였다.
- **R10(부분만 반영):** 핵무장론 기사(11-04 재수집)는 오늘 원자료에 없어 출처로 쓸 수 없다. 덴마크 학생 시위·삼성 LCD 기사는 중요도가 중간이라 넣지 않았다.

`python template/verify.py 2026-11-05`: 통과(선별 뉴스 55건)
