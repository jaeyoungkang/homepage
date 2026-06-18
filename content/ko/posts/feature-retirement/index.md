---
title: "기능 철회가 쉬워진 사건"
draft: false
date: 2026-06-18
summary: "Light House는 기능을 코드 조각이 아니라 생애주기를 가진 제품 계약으로 다뤘다. 그래서 주요 기능을 몇 시간 안에 철회하면서도 요구사항, 테스트, 분석 이벤트, 릴리스 기록을 함께 움직일 수 있었다."
translationKey: "feature-retirement"
tags: ["경험", "배움"]
---

2026년 6월 18일 Light House 작업은 한 가지 변화를 드러냈다. 기능을 추가하는 속도가 빨라진 것이 아니라, 이미 만든 기능을 철회하는 일이 쉬워졌다. 이 차이는 작지 않다. 제품 개발에서 기능 추가는 화면에 보인다. 새 버튼, 새 패널, 새 API, 새 테스트는 진전처럼 보인다. 반대로 기능 철회는 보통 위험하다. 버튼 하나를 지워도 이벤트가 남고, 이벤트를 지우면 대시보드가 깨지고, 테스트를 지우면 문서가 거짓이 되고, 문서를 지우면 사용자가 기대하던 약속이 설명 없이 사라진다. 그래서 많은 제품은 잘못된 기능을 알면서도 오래 끌고 간다.

예를 들어 보통의 코드베이스에서 PDF 버튼을 없앤다고 하자. 엔지니어가 버튼을 지우면 화면은 깨끗해 보인다. 하지만 분석 대시보드에는 여전히 `pdf_open` 이벤트가 남을 수 있다. QA 테스트는 더 이상 존재하지 않는 PDF 실패 안내를 기대할 수 있다. 도움말이나 릴리스 노트는 여전히 "PDF를 열 수 있다"고 말할 수 있다. 이 상태에서 제품은 기능을 철회한 것이 아니라, 사용자가 찾기 어려운 죽은 약속을 남긴다.

Light House에서 이번에 일어난 일은 달랐다. 떠다니는 봇(floating bot)과 곁에 머무는 존재감(ambient presence), 여러 문서를 한 화면에 펼치는 배치(multi-document layout), 내부 PDF 열기와 PDF 인식(PDF awareness) 같은 주요 기능을 짧은 기간 안에 철회했다. 에이전트는 이 철회를 코드 삭제로만 처리하지 않았다. 제품 요구사항, QA 증거, 분석 추적 계획, 릴리스 노트, PR 리뷰가 함께 움직였다. 제품 운영 언어로 말하면, 기능 폐기(feature deprecation)와 교체 작업이 정상 파이프라인으로 들어왔다.

핵심은 Light House가 기능을 생애주기 단위로 다룬다는 점이다. 여기서 생애주기란 기능이 태어나고, 검증받고, 관측되고, 변경되고, 철회되는 전체 흐름을 말한다. 일반 코드베이스에서는 기능이 컴포넌트, API, 상태, 테스트 몇 개로 흩어진다. Light House에서는 중요한 기능이 하나의 제품 계약 묶음으로 존재한다. 저장소는 제품 장면, 사용자 약속, 인수 조건(acceptance criteria), 구현 표면, 테스트와 증거 장부(evidence ledger), 분석 이벤트(analytics event), 결정 기록(decision log), 출시 게이트(release gate)를 같은 파일 그래프 안에서 연결한다.

<div class="intent-visual" role="img" aria-label="기능 하나가 제품 장면부터 출시 게이트까지 여덟 단계 묶음으로 존재한다">
  <div class="feat-chain">
    <div class="intent-step"><span>01</span><strong>제품 장면</strong><em>사용자가 마주하는 화면</em></div>
    <div class="intent-step"><span>02</span><strong>사용자 약속</strong><em>그 장면이 약속하는 것</em></div>
    <div class="intent-step blue"><span>03</span><strong>인수 조건</strong><em>통과해야 할 조건</em></div>
    <div class="intent-step blue"><span>04</span><strong>구현 표면</strong><em>화면과 런타임 경로</em></div>
    <div class="intent-step hot"><span>05</span><strong>증거 장부</strong><em>약속을 닫는 테스트·검증</em></div>
    <div class="intent-step hot"><span>06</span><strong>분석 이벤트</strong><em>약속을 실제로 밟는지 관측</em></div>
    <div class="intent-step hot"><span>07</span><strong>결정·변경 기록</strong><em>약속을 만든·바꾼 이유</em></div>
    <div class="intent-step green"><span>08</span><strong>출시 게이트</strong><em>내보낼 수 있는 상태인가</em></div>
  </div>
</div>

그래서 기능 하나는 이런 묶음으로 존재한다. 먼저 사용자가 마주하는 제품 장면이 있다. 그 장면에서 제품이 무엇을 약속하는지 요구사항이 이름을 갖는다. 그 요구사항은 어떤 조건을 통과해야 하는지 인수 조건을 갖는다. 구현 표면은 그 약속을 실제 화면과 런타임 경로로 만든다. 증거 장부는 어떤 테스트와 검증이 그 약속을 닫는지 적는다. 분석 이벤트는 사용자가 그 약속을 실제로 밟는지 관측한다. 결정 기록과 변경 기록은 왜 이 약속을 만들거나 바꿨는지 남긴다. 출시 게이트는 이 묶음이 내보낼 수 있는 상태인지 본다.

## 계약의 모양

여러 문서를 한 화면에 펼치던 배치를 철회한 일은 이 묶음의 작동 방식을 보여주는 중간 사례다. 이전 작업 공간(workspace)은 여러 문서를 가로로 펼치고 보기 모드(view mode)를 오가게 했다. 표면상으로는 배치 선택지 하나였지만, 실제로는 지금 활성 문서가 무엇인지, 반응(reaction)이 어느 문서에 속하는지, 넓은 사이드 패널에서도 겹쳐 띄우는 화면 전용 분석 이벤트가 잘못 발생하는지 같은 문제를 만들었다. PR #143은 이 기능을 단순히 접지 않았다. 제품 약속을 하나의 집중된 문서와 문서별 반응 오버레이로 다시 잡았다. 그래서 배치 제거, 오버레이 약속, 관련 증거, 결정 기록, `/about/changes`, 리뷰 스레드가 같은 철회 작업 안에서 함께 움직였다.

내부 PDF 열기 기능이 좋은 사례다. 이 기능은 단순히 `/api/documents/pdf`나 `PdfDocument.tsx`로 존재하지 않았다. Light House는 사용자에게 "PDF를 열면 내부 작업 공간에서 읽을 수 있고, 첫 AI 반응을 받고, 실패하면 안내를 받고, 그림과 표도 해석할 수 있다"는 약속을 했다. 저장소는 이 약속을 `pdf-document-ai-reaction`, `pdf-failure-recovery-reaction`, `pdf-figure-table-interpretation` 같은 요구사항으로 나눠 기록했다. 각 요구사항은 PDF 인식 장부, PDF 시각 자료 해석 장부, 관련 테스트, PDF 열기 분석 이벤트와 연결을 가졌다. 런타임에는 `/api/documents/pdf`, 작업 공간의 `pdf` 문서, PDF 추출 경로가 있었다. 화면에는 검색 결과 카드의 PDF 버튼, PDF 문서 헤더, 그림·표 액션이 있었다.

<div class="intent-visual" role="img" aria-label="내부 PDF 열기 약속 세 개가 장부, 분석 이벤트, API, 화면 표면으로 묶인 계약">
  <div class="feat-fan">
    <div class="fan-promises">
      <span class="intent-label">사용자 약속</span>
      <strong>PDF 첫 반응<br/><code>pdf-document-ai-reaction</code></strong>
      <strong>실패 안내<br/><code>pdf-failure-recovery-reaction</code></strong>
      <strong>그림·표 해석<br/><code>pdf-figure-table-interpretation</code></strong>
    </div>
    <div class="fan-arrow">묶여 있던 표면</div>
    <div class="fan-targets">
      <span>PDF 인식 장부</span>
      <span>시각 자료 해석 장부</span>
      <span><code>product.pdf_open.*</code> 분석</span>
      <span><code>/api/documents/pdf</code></span>
      <span>작업 공간 <code>pdf</code> 문서</span>
      <span>검색 결과 PDF 버튼</span>
      <span>그림·표 액션</span>
    </div>
  </div>
</div>

이 구조 때문에 철회 작업의 질문이 달라졌다. "PDF 버튼을 어떻게 없앨까"가 아니라 "Light House가 아직 내부 PDF 정독을 약속하는가"를 먼저 물을 수 있었다. 이번 판단은 아니었다. Light House는 검색과 탐색 맥락을 유지하고, 정독은 Moonlight로 넘긴다. 따라서 에이전트는 내부 PDF 열기 약속들을 거두고, PDF 인식과 시각 자료 해석 증거를 정리하고, PDF 열기 이벤트를 Moonlight 넘김 이벤트로 바꿔야 했다. 동시에 `delegate-deep-read-to-moonlight` 약속이 새 책임을 받았다. 이 약속은 원래 PDF 문서 안의 후속 링크였지만, 철회 후에는 검색 결과와 인용 계보와 그래프 이웃 카드에서 바로 Moonlight로 넘기는 핵심 약속으로 의미를 바꿨다.

이 차이는 화면에서도 보인다. 이전에는 검색 결과 카드의 제목이나 PDF 버튼을 누르면 Light House가 내부 작업 공간에 `pdf` 문서를 만들었다. 서버는 PDF를 가져오고, 텍스트를 추출하고, 작업 공간은 PDF 문서를 열고, AI 반응은 "논문 소개"를 만들고, 그림·표 액션은 시각 자료 해석으로 이어졌다. 철회 후 같은 동작은 내부 문서를 만들지 않는다. `buildMoonlightFileUrl`이 `https://themoonlight.io/file?url=<encoded>` 형태의 링크를 만들고, 사용자는 Moonlight에서 긴 읽기를 이어간다. Light House는 같은 검색 문서와 탐색 맥락을 그대로 유지한다.

<div class="intent-visual" role="img" aria-label="철회 전에는 Light House가 정독까지 맡고, 철회 후에는 탐색 맥락만 유지하며 정독을 Moonlight로 넘긴다">
  <div class="feat-ba">
    <div class="ba-col before">
      <span class="intent-label">전 — 정독까지 맡음</span>
      <ol>
        <li>검색 결과 PDF 클릭</li>
        <li><code>/api/documents/pdf</code></li>
        <li>작업 공간 <code>pdf</code> 문서 생성</li>
        <li>PDF 인식 반응</li>
        <li>그림·표 해석</li>
      </ol>
    </div>
    <div class="ba-col after">
      <span class="intent-label">후 — 탐색 맥락 유지, 정독은 넘김</span>
      <ol>
        <li>검색 결과 PDF 클릭</li>
        <li><code>buildMoonlightFileUrl(...)</code></li>
        <li><code>themoonlight.io/file?url=…</code></li>
        <li>Moonlight 정독</li>
      </ol>
    </div>
  </div>
</div>

곁에 머무는 존재감을 철회한 일도 같은 구조를 보여준다. 떠다니는 봇은 단순한 화면 장식이 아니었다. 이 기능은 곁에 머무는 존재감 경험, `floating-ambient-bot` 장면, `floating-bot-activity-presence` 약속, `ambient-presence-companion` 측면(aspect), `/admin/intent/support-layer`, 내비게이션, 다국어 키, 테스트와 연결을 가졌다. 그래서 에이전트는 봇 컴포넌트만 지우지 않았다. 봇이 차지하던 제품 약속과 관리 표면을 함께 정리했다. 지원 계층(support-layer) 범위가 비면 관리자 의도 화면에는 죽은 분류가 살아 있는 것처럼 남는다. 이번 철회는 그 빈 범위까지 제거했다. 화면의 봇 하나가 아니라 제품 의미가 놓였던 자리 전체를 철회한 셈이다.

이 사례는 철회의 끝점이 어디인지도 보여준다. 봇이 사라진 뒤에도 `/admin/intent/support-layer`가 남으면 운영자는 아직 지원 계층 제품 영역이 살아 있다고 읽을 수 있다. 내비게이션과 다국어 키가 남으면 화면에는 선택 가능한 빈 분류가 생긴다. 테스트의 import가 남으면 다음 에이전트는 그 표면을 복구해야 하는 대상으로 오해할 수 있다. 그래서 이 철회는 화면 제거가 아니라 관리 표면 제거까지 닫아야 했다.

## 왜 빨랐나

이런 철회가 몇 시간 안에 가능했던 이유는 에이전틱 엔지니어링 하네스가 이 생애주기 묶음을 다룰 수 있었기 때문이다. 첫 번째 축은 제품 계약 구조다. 저장소가 기능을 코드 조각이 아니라 사용자 약속으로 기록했기 때문에, 에이전트는 삭제 대상을 파일 이름으로만 찾지 않았다. 어떤 약속을 끝내는지, 어떤 약속이 살아남는지, 어떤 약속이 새 책임을 받는지를 따라갔다.

두 번째 축은 세부 스킬이다. 여기서 스킬은 사람의 재능이 아니라 에이전트가 작업할 때 읽는 절차 문서다. `mission-control`은 제품 계약 범위를 잡는다. `story-chain-contract-steward`는 요구사항, 인수 조건, 증거 표를 맞춘다. `aspect-steward`는 여러 기능에 걸친 디자인 정책과 공통 제품 규칙을 정리한다. `analytics-event-steward`는 추적 계획과 실제 발생 경로를 맞춘다. `project-knowledge`는 이전 세션의 판단을 다음 작업자에게 넘긴다. `decision-log-draft`와 `branch-review-response`는 기록과 리뷰 루프를 닫는다. 이 스킬들은 에이전트를 더 자유롭게 만들기보다 덜 자유롭게 만든다. 그래서 철회 작업은 삭제 감각이 아니라 계약 전파 작업으로 바뀐다.

세 번째 축은 기계적 보조장치다. 스킬이 에이전트의 역할과 절차를 정한다면, 기계적 보조장치는 그 절차가 실제 코드베이스에서 맞는지 확인한다. `work-start`와 내러티브 회상은 이전 판단을 복원한다. `rg`, `git diff`, `git status`는 어떤 파일과 경로가 아직 남았는지 보여준다. 유닛 테스트는 사용자가 밟는 실행 경로를 고정한다. 린트와 죽은 코드 검사는 철회 후 남은 prop, import, handler를 드러낸다. 중복 검사는 검색 결과 카드, 인용 계보 카드, 그래프 이웃 카드가 서로 다른 방식으로 Moonlight 링크를 만들지 않게 막는다. 타입 검사는 타입 그래프를 확인한다. 스토리 체인 검증기(Story Chain validator)와 출시 상태는 요구사항 그래프와 출시 준비 상태를 본다. 분석 레지스트리는 지금 관측해야 할 이벤트가 무엇인지 보여준다. PR 리뷰 봇은 낡은 설명문, 잘못된 이벤트 발생, 누락된 장부 행을 반복적으로 지적한다.

<div class="intent-visual" role="img" aria-label="검증장치마다 다른 질문을 나눠 맡는다">
  <div class="feat-pairs">
    <span class="intent-label">검증장치가 나눠 맡은 질문</span>
    <div class="pair"><strong>typecheck</strong><em>타입 그래프가 깨졌는가</em></div>
    <div class="pair"><strong>unit tests</strong><em>사용자가 밟는 실행 경로가 새 약속대로 움직이는가</em></div>
    <div class="pair"><strong>lint · dead-code · 중복 검사</strong><em>죽은 prop·import·handler, 복제된 로직이 남았는가</em></div>
    <div class="pair"><strong>Story Chain validator · 출시 상태</strong><em>요구사항 그래프와 출시 준비가 닫혔는가</em></div>
    <div class="pair"><strong>analytics registry</strong><em>실제 내보내는 이벤트가 지금 추적 계획의 의미와 맞는가</em></div>
  </div>
</div>

검증장치의 차이는 작은 코드 흔적에서 드러난다. `onOpenPdf` 같은 prop가 선택적으로 남으면 타입 검사는 통과할 수 있다. 하지만 죽은 코드 검사와 `rg`는 더 이상 쓰지 않는 handler와 import를 드러낸다. 유닛 테스트는 PDF 버튼이 내부 열기 handler를 부르지 않고 Moonlight 링크를 그리는지 고정한다. 중복 검사는 검색 결과 카드와 인용 계보 카드와 그래프 이웃 카드가 제각각 링크를 만들지 않게 막는다. 이 장치들은 제품 판단을 대신하지 않는다. 대신 "끝난 것처럼 보이는 작업"에서 남은 찌꺼기를 드러낸다.

이번 PDF 철회는 이 보조장치들의 역할 차이를 선명하게 보여줬다. 타입 검사와 스토리 체인 검증은 통과했다. 타입 그래프와 기본 요구사항 그래프가 깨지지 않았다는 뜻이다. 그러나 `docs/analytics/events.yaml`과 실제 클릭 handler를 나란히 보자 다른 문제가 보였다. 추적 계획은 `product.moonlight_deep_read.clicked`를 새 정본 이벤트로 두고 있었지만, 실제 `SearchResultItem`은 아직 `product.pdf_open.clicked` 의미를 내보내고 있었다. 이 결함은 타입 오류가 아니다. 문서 형식 오류도 아니다. 제품 관측 의미의 불일치다. 보조장치들이 여러 층으로 나뉘어 있었기 때문에 이런 불일치를 특정할 수 있었다.

<div class="intent-visual" role="img" aria-label="코드는 통과했지만 정본 추적 계획과 실제 클릭 핸들러의 분석 이벤트가 어긋난 상태">
  <div class="feat-clash">
    <div class="clash-side ok">
      <span class="intent-label">정본 추적 계획</span>
      <strong><code>product.moonlight_deep_read.clicked</code></strong>
    </div>
    <div class="clash-vs">≠</div>
    <div class="clash-side warn">
      <span class="intent-label">실제 클릭 핸들러</span>
      <strong><code>product.pdf_open.clicked</code></strong>
    </div>
    <div class="clash-note">코드는 통과했지만 관측 계약은 아직 완전히 닫히지 않았다</div>
  </div>
</div>

이 구조를 종합하면, 에이전틱 엔지니어링의 실질은 "모델이 더 똑똑해졌다"가 아니다. 사람의 제품 판단, 에이전트의 절차 스킬, 기계적 검증장치가 분리돼 있고 서로 보완한다. 사람은 방향과 의미를 정한다. 에이전트는 편집과 연결 추적을 수행한다. 스킬은 에이전트의 행동 범위를 좁힌다. 보조장치는 누락, 모순, 남은 증거를 계속 드러낸다.

기능 철회는 이 하네스를 기능 추가보다 더 강하게 검증한다. 기능 추가는 새 표면이 보이면 진전처럼 느껴질 수 있다. 기능 철회는 기존 연결을 끊고, 남은 연결을 다시 닫아야 한다. 제품 요구사항, QA 증거, 분석 이벤트, 릴리스 안내, 런타임 경로가 함께 움직이지 않으면 기능은 반쯤 살아 있는 상태로 남는다. 이번 Light House 작업은 이 반쯤 살아 있는 상태를 줄이는 능력을 보여줬다.

그래서 이 사건은 단순한 정리가 아니다. 제품이 자기 복잡도를 회수할 수 있게 된 사건이다. 기능을 지울 수 있는 제품은 더 빨리 배운다. 잘못된 약속을 오래 끌고 가지 않고, 지금 배운 것에 맞춰 약속을 다시 정렬할 수 있기 때문이다. Light House는 기능을 더 많이 붙이는 방향만이 아니라, 살아남을 약속만 남기는 방향으로도 진화하고 있다. 에이전틱 엔지니어링의 중요한 성과는 바로 여기에 있다. 더 많은 기능을 더 빨리 만드는 것이 아니라, 잘못된 복잡도를 더 안전하게 되돌릴 수 있게 만든다.
