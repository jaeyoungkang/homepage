---
title: "의도 전파 — 시각화 샘플"
draft: true
date: 2026-04-28
summary: "intent-to-code-propagation 본 글에서 부족했던 핵심 개념들을 더 풍부하게 시각화한 샘플 모음. 본 글 통합 전 검토용."
translationKey: "intent-propagation-visuals"
tags: ["draft"]
build:
  list: never
  render: always
---

본 글 `거친 의도가 코드가 될 때`는 텍스트로는 8단계 모델, 종단×횡단, 4개 신호, 권한 분리까지 다루는데 시각화는 평면 박스 그리드에 머물렀다. 아래는 그 격차를 메우는 다섯 개의 샘플이다. 검토 후 마음에 드는 것을 본 글에 흡수한다.

---

## 샘플 1 — 빈칸 채우기 문제

`gap-fill`. 거친 말 한 줄이 다섯 개의 정해지지 않은 빈칸으로 분해되고, AI가 그 빈칸을 자기 방식으로 채워 어긋난 결과를 만든다. 도입부에 두면 "AI가 느려서가 아니라 너무 빨리 빈칸을 채우는 게 문제"라는 메시지가 한 장에 들어온다.

<div class="intent-visual gap-fill" role="img" aria-label="거친 말이 다섯 개의 빈칸으로 분해되고 AI가 임의로 채워 어긋난 결과가 만들어지는 흐름">
  <div class="gap-source">
    <span class="gap-tag">제작자의 거친 말</span>
    <strong>"AI 코멘트가 너무 짧다.<br/>좀 더 풍부한 설명을 줘야 한다."</strong>
    <em>구체적 약속 0개 · 검증 가능 조건 0개</em>
  </div>
  <div class="gap-blanks">
    <span class="gap-tag">정해지지 않은 빈칸</span>
    <ol class="gap-list">
      <li><b>?</b><span>"풍부하다"가 무엇인가</span></li>
      <li><b>?</b><span>어느 화면에서 드러나야 하는가</span></li>
      <li><b>?</b><span>사용자가 무엇을 얻어야 하는가</span></li>
      <li><b>?</b><span>실패했을 때 무엇을 막아야 하는가</span></li>
      <li><b>?</b><span>어느 코드 표면이 책임지는가</span></li>
    </ol>
    <em class="gap-arrow">↓ AI가 자기 방식으로 채운다</em>
  </div>
  <div class="gap-result">
    <span class="gap-tag warn">그럴듯한 출력</span>
    <strong>형식은 맞지만 의도와 어긋난 코멘트</strong>
    <em>돌아간다 ≠ 작동한다</em>
  </div>
</div>

> 노트: 빈칸 5개가 본문 단락 "어느 화면에서 드러나야 하는지 정해지지 않았다…" 리스트와 1:1 대응. 텍스트와 시각화가 서로를 강화한다.

---

## 샘플 2 — 방법론 스택 7층

`method-stack`. 좌측 세로 게이지가 의도→코드 진행을 표시하고, 우측에 7개 방법이 각각 어떤 산물과 어떤 실패를 막는지 카드로 쌓인다. 본 글의 "신뢰도를 만든 방법론 스택" 섹션이 표 한 칸으로만 처리되어 있던 것을 입체화한다.

<div class="intent-visual method-stack" role="img" aria-label="User Story부터 Quality Gate까지 7단계 방법론 스택과 각 단계가 막는 실패">
  <div class="stack-axis">
    <span class="stack-axis-top">의도</span>
    <span class="stack-axis-bar"></span>
    <span class="stack-axis-bot">코드 / 출시</span>
  </div>
  <ol class="stack-list">
    <li class="stack-step s1">
      <span class="stack-no">01</span>
      <strong>User Story</strong>
      <em>거친 의도를 사용자 약속 단위로 자른다</em>
      <b>막는 실패</b><i>구현 가능 단위 부재</i>
    </li>
    <li class="stack-step s2">
      <span class="stack-no">02</span>
      <strong>Acceptance Criteria · CIQ</strong>
      <em>약속을 검사 조건과 판단 질문으로 쪼갠다</em>
      <b>막는 실패</b><i>"풍부하다" 같은 모호한 완료</i>
    </li>
    <li class="stack-step s3">
      <span class="stack-no">03</span>
      <strong>SpecDown</strong>
      <em>문서를 실행 가능한 스펙으로 만든다</em>
      <b>막는 실패</b><i>읽기만 하는 죽은 문서</i>
    </li>
    <li class="stack-step s4">
      <span class="stack-no">04</span>
      <strong>Traceability</strong>
      <em>약속·조건·스펙·테스트·코드가 서로를 가리킨다</em>
      <b>막는 실패</b><i>중간 연결 누락</i>
    </li>
    <li class="stack-step s5">
      <span class="stack-no">05</span>
      <strong>Aspect-Oriented 구조</strong>
      <em>여러 기능을 가로지르는 공통 규칙을 따로 관리</em>
      <b>막는 실패</b><i>공통 규칙이 한 기능에 숨음</i>
    </li>
    <li class="stack-step s6">
      <span class="stack-no">06</span>
      <strong>Judge · Validator · Contract Test</strong>
      <em>구조적 성공과 의미적 성공을 나눠 검증한다</em>
      <b>막는 실패</b><i>형식만 맞춘 그럴듯한 출력</i>
    </li>
    <li class="stack-step s7">
      <span class="stack-no">07</span>
      <strong>Quality Gate · CI</strong>
      <em>실패 상태가 commit / push / release로 못 넘어간다</em>
      <b>막는 실패</b><i>말로만 있는 규칙</i>
    </li>
  </ol>
</div>

> 노트: 단계 색이 위에서 아래로 노란→주황→파란→녹색 그라데이션을 그려 "의도가 코드로 내려간다"는 운동감을 만든다.

---

## 샘플 3 — 종단 × 횡단 매트릭스

`cross-grid`. 본 글에서 가장 누락이 큰 부분. 세로축은 사용자 약속(종단), 가로축은 기능 모듈, 그 위로 두 개의 공통 규칙(횡단)이 가로로 가로지른다. 종단과 횡단이 한 격자 안에 동시에 보여야 "한 점수로 뭉개지 않는다"는 메시지가 산다.

<div class="intent-visual cross-grid" role="img" aria-label="종단(사용자 약속)과 횡단(공통 규칙)이 한 격자에서 만나는 매트릭스">
  <div class="grid-corner">
    <span>축</span>
    <strong>종단 × 횡단</strong>
  </div>
  <div class="grid-col-head"><span>기능</span><strong>검색</strong></div>
  <div class="grid-col-head"><span>기능</span><strong>PDF</strong></div>
  <div class="grid-col-head"><span>기능</span><strong>워크스페이스</strong></div>
  <div class="grid-col-head"><span>기능</span><strong>리포트</strong></div>

  <div class="grid-row-head longi"><span>약속 1</span><strong>판단 근거 표시</strong></div>
  <div class="grid-cell longi has"><b>✓</b><span>US-A1</span></div>
  <div class="grid-cell"><b>·</b></div>
  <div class="grid-cell longi has"><b>✓</b><span>US-C1</span></div>
  <div class="grid-cell"><b>·</b></div>

  <div class="grid-row-head longi"><span>약속 2</span><strong>다음 행동 제안</strong></div>
  <div class="grid-cell"><b>·</b></div>
  <div class="grid-cell longi has"><b>✓</b><span>US-B2</span></div>
  <div class="grid-cell longi has"><b>✓</b><span>US-C2</span></div>
  <div class="grid-cell longi miss"><b>!</b><span>missing</span></div>

  <div class="grid-row-head longi"><span>약속 3</span><strong>근거 부족 표기</strong></div>
  <div class="grid-cell"><b>·</b></div>
  <div class="grid-cell"><b>·</b></div>
  <div class="grid-cell"><b>·</b></div>
  <div class="grid-cell longi has"><b>✓</b><span>US-D3</span></div>

  <div class="grid-row-head cross"><span>공통 규칙 α</span><strong>근거 없는 단정 금지</strong></div>
  <div class="grid-cell cross"><b>woven</b></div>
  <div class="grid-cell cross"><b>woven</b></div>
  <div class="grid-cell cross miss"><b>not woven</b></div>
  <div class="grid-cell cross"><b>woven</b></div>

  <div class="grid-row-head cross"><span>공통 규칙 β</span><strong>한국어 품질</strong></div>
  <div class="grid-cell cross"><b>woven</b></div>
  <div class="grid-cell cross"><b>woven</b></div>
  <div class="grid-cell cross"><b>woven</b></div>
  <div class="grid-cell cross"><b>woven</b></div>

  <div class="grid-legend">
    <span><i class="dot longi"></i>종단 — 약속이 기능에 닫혔는가</span>
    <span><i class="dot cross"></i>횡단 — 공통 규칙이 기능에 weave됐는가</span>
    <span><i class="dot miss"></i>한 칸이라도 누락 → release blocked</span>
  </div>
</div>

> 노트: PDF×약속1, 검색×약속2처럼 비어있는 칸은 의도하지 않은 누락이 아니라 적용 대상이 아닌 칸. 누락(`!`)은 명시적으로 다른 색.

---

## 샘플 4 — 권한 분리

`authority-split`. Human / Agent / Evaluator / System 네 역할이 각자 무엇을 할 수 있고 무엇을 할 수 **없는지** 함께 보여준다. 권한 칸과 금지 칸을 같은 카드 안에 위아래로 나눠 "이 분리가 무너지면 AI가 자기 통과시킨다"는 위험을 시각적으로 못박는다.

<div class="intent-visual authority-split" role="img" aria-label="Human, Agent, Evaluator, System 네 역할의 권한과 금지 분리">
  <div class="auth-col human">
    <span class="auth-role">Human</span>
    <strong>약속을 선언한다</strong>
    <ul class="auth-can"><li>의도 정의</li><li>약속 형식 확정</li><li>철회 결정</li></ul>
    <ul class="auth-cannot"><li>판정 통과 못함</li><li>gate 우회 못함</li></ul>
  </div>
  <div class="auth-col agent">
    <span class="auth-role">Agent (AI)</span>
    <strong>약속을 아래로 전파한다</strong>
    <ul class="auth-can"><li>문서 / 스펙 생성</li><li>테스트 / 코드 작성</li><li>표면 태그 부착</li></ul>
    <ul class="auth-cannot"><li>met 판정 못함</li><li>gate 통과 결정 못함</li></ul>
  </div>
  <div class="auth-col eval">
    <span class="auth-role">Evaluator</span>
    <strong>충족 여부를 판단한다</strong>
    <ul class="auth-can"><li>met / not-met / unknown</li><li>Sufficiency Review 기록</li></ul>
    <ul class="auth-cannot"><li>코드 변경 못함</li><li>약속 자체 수정 못함</li></ul>
  </div>
  <div class="auth-col system">
    <span class="auth-role">System</span>
    <strong>실패 상태를 막는다</strong>
    <ul class="auth-can"><li>commit / push / CI gate</li><li>release verdict 차단</li></ul>
    <ul class="auth-cannot"><li>의도 해석 못함</li><li>판정 자체 못함</li></ul>
  </div>
  <div class="auth-warning">
    <span>⚠ 분리가 무너지면</span>
    <strong>AI가 빈칸을 채우고 → AI가 스스로 통과시킨다 → 의도가 코드까지 도달했는지 알 수 없다</strong>
  </div>
</div>

> 노트: "권한 있는 것"과 "권한 없는 것"을 한 카드에 같이 넣은 게 핵심. 보통 시각화는 권한만 그리지만, 라이트하우스의 핵심은 *무엇을 못 하게 했는가*다.

---

## 샘플 5 — 4개의 신호등

`signal-lights`. 본 글의 `release-verdict`는 종단축/횡단축을 학술적으로 보여줬다면, 이 샘플은 운영실 대시보드처럼 4개 lamp가 모두 켜진 상태와 하나가 꺼진 상태를 위아래로 비교해 "한 개라도 꺼지면 blocked"라는 메시지를 직관적으로 만든다.

<div class="intent-visual signal-lights" role="img" aria-label="네 개의 신호등이 모두 켜져야 release ready, 하나라도 꺼지면 blocked">
  <div class="lights-header">
    <span>출시 판정</span>
    <strong>네 개의 불이 모두 켜져야 한다</strong>
  </div>

  <div class="lights-row">
    <div class="lamp on">
      <b class="lamp-no">01</b>
      <span class="lamp-axis longi">종단</span>
      <strong>의도</strong>
      <em>약속이 충족됐는가</em>
      <i class="lamp-state">green</i>
    </div>
    <div class="lamp on">
      <b class="lamp-no">02</b>
      <span class="lamp-axis longi">종단</span>
      <strong>조건</strong>
      <em>스펙·테스트까지 이어졌는가</em>
      <i class="lamp-state">green</i>
    </div>
    <div class="lamp on">
      <b class="lamp-no">03</b>
      <span class="lamp-axis longi">종단</span>
      <strong>코드</strong>
      <em>실제 코드 표면까지 닫혔는가</em>
      <i class="lamp-state">green</i>
    </div>
    <div class="lamp on">
      <b class="lamp-no">04</b>
      <span class="lamp-axis cross">횡단</span>
      <strong>공통 규칙</strong>
      <em>aspect가 모든 사이트에 weave됐는가</em>
      <i class="lamp-state">green</i>
    </div>
  </div>
  <div class="lights-result ok">
    <span>모두 green</span>
    <strong>release ready</strong>
  </div>

  <div class="lights-row dim">
    <div class="lamp on"><b class="lamp-no">01</b><strong>의도</strong><i class="lamp-state">green</i></div>
    <div class="lamp on"><b class="lamp-no">02</b><strong>조건</strong><i class="lamp-state">green</i></div>
    <div class="lamp off"><b class="lamp-no">03</b><strong>코드</strong><i class="lamp-state">missing</i></div>
    <div class="lamp on"><b class="lamp-no">04</b><strong>공통 규칙</strong><i class="lamp-state">green</i></div>
  </div>
  <div class="lights-result blocked">
    <span>한 개라도 꺼짐</span>
    <strong>release blocked</strong>
  </div>
</div>

> 노트: 두 줄을 위아래로 두는 게 메시지의 핵심. "어떤 종류의 불완전함인지 드러난다"는 본문 문장이 한 장에 살아난다.

---

## 정리

다섯 개 모두 본 글의 빈 자리에 대응한다.

- 샘플 1 — 도입부 "거친 말이 너무 빨리 코드가 된다" 단락
- 샘플 2 — 신뢰도 만든 방법론 스택 섹션
- 샘플 3 — 종단·횡단 두 섹션을 한 장으로
- 샘플 4 — 권한 분리 섹션 (현재 본 글에 없음)
- 샘플 5 — 출시 판정 4개의 불 (현재 release-verdict와 교체 후보)

본 글에 흡수할 후보를 골라주면, 흡수 PR은 본 글 단락 위치까지 정해서 한 번에 정리한다.
