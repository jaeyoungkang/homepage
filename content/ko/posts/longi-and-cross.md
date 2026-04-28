---
title: "한 점수로 뭉개지 않는다 — 종단과 횡단"
date: 2026-04-28
summary: "출시 판정은 점수 하나가 아니다. 약속이 코드까지 내려갔는지(종단)와 공통 규칙이 모든 기능에 박혔는지(횡단)를 동시에 본다."
translationKey: "longi-and-cross"
tags: ["생각", "경험"]
---

출시 판정이 한 줄로 끝날 때가 있다. 통과 또는 미통과. 점수 하나로 압축된 결과는 깔끔해 보이지만, 정작 무엇이 비었는지를 알려주지 않는다.

문제가 의도 자체였는지, 조건이 스펙까지 내려가지 못한 것인지, 코드 표면이 비어 있는 것인지, 아니면 공통 규칙이 일부 기능에서만 적용된 것인지. 한 점수로 합쳐버리면 다음에 무엇을 고쳐야 하는지가 흐려진다.

라이트하우스에서 이 문제를 풀 때 쓴 생각 도구가 두 축이다. 종단과 횡단.

## 종단 — 하나의 약속이 아래로 내려가는 길

종단은 사용자 약속 하나가 위에서 아래로 내려가는 세로 경로다. 사람이 선언한 약속이 검사 조건이 되고, 조건이 스펙으로, 스펙이 테스트와 코드로, 코드가 화면까지 이어진다.

종단이 본다는 것은 이 한 줄이 어디서 끊겼는지 찾는 일에 가깝다. 약속은 있는데 조건이 없을 수 있다. 조건은 있는데 스펙으로 내려가지 않았을 수 있다. 테스트는 있는데 코드 표면과 연결되지 않았을 수 있다.

라이트하우스 문서 표현을 빌리면 종단은 "이 기능 하나가 약속대로 닫혔는가"를 본다.

## 횡단 — 여러 기능을 가로지르는 공통 규칙

횡단은 다르다. 한 기능이 아니라 여러 기능을 가로지르는 공통 규칙을 본다.

근거 없이 단정하지 않는다. 사용자에게 보여지는 문장은 한국어 품질을 지킨다. 상태 변화는 추적 가능해야 한다. 이런 규칙은 검색 기능에만 속하지 않고 PDF, 워크스페이스, 리포트에도 동시에 걸린다.

이 사고는 Aspect-Oriented Programming의 시선과 닮아 있다. AOP에서는 로깅이나 보안처럼 여러 기능에 흩어지는 공통 관심사를 aspect로 분리한다. 라이트하우스에서는 AI 응답 포맷이나 한국어 품질 같은 제품 규칙을 같은 방식으로 떼어낸다. Pointcut으로 적용 대상을 정하고, Advice로 주입할 규칙을 정하고, Weaving으로 그 규칙이 각 기능의 약속 안에 박혀 있는지를 본다.

핵심은 공통 규칙이 한 기능 안에 숨어버리지 않게 하는 일이다. 어떤 기능에서는 잘 지키고 다른 기능에서는 슬쩍 빠져 있다면, 그 규칙은 사실상 운영되지 않는 것에 가깝다.

횡단은 그래서 이렇게 묻는다. "이 공통 원칙이 관련 기능 전체에 실제로 스며들었는가."

종단 한 줄과 횡단 한 띠가 한 그림에서 만나는 모습은 이렇다. 종단은 위에서 아래로, 횡단은 그 줄들을 가로질러 들어간다.

<div class="intent-visual weave-chain" role="img" aria-label="종단 5단계 chain이 4개 기능에 나란히 내려가고, 두 개의 횡단 advice가 그 chain들을 가로지르는 모습">
  <div class="wc-corner"><span>축</span><strong>종단 × 횡단</strong></div>
  <div class="wc-col-head"><span>기능</span><strong>검색</strong></div>
  <div class="wc-col-head"><span>기능</span><strong>PDF</strong></div>
  <div class="wc-col-head"><span>기능</span><strong>워크스페이스</strong></div>
  <div class="wc-col-head"><span>기능</span><strong>리포트</strong></div>

  <div class="wc-step-head"><span>step 1</span><strong>약속</strong></div>
  <div class="wc-cell s-promise"><strong>US-A1</strong><em>판단 근거 표시</em></div>
  <div class="wc-cell s-promise"><strong>US-B2</strong><em>다음 행동 제안</em></div>
  <div class="wc-cell s-promise"><strong>US-C1</strong><em>판단 근거 표시</em></div>
  <div class="wc-cell s-promise"><strong>US-D3</strong><em>근거 부족 표기</em></div>

  <div class="wc-step-head"><span>step 2</span><strong>조건</strong></div>
  <div class="wc-cell s-cond"><strong>AC + CIQ</strong></div>
  <div class="wc-cell s-cond"><strong>AC + CIQ</strong></div>
  <div class="wc-cell s-cond"><strong>AC + CIQ</strong></div>
  <div class="wc-cell s-cond"><strong>AC + CIQ</strong></div>

  <div class="wc-cross">
    <span class="wc-cross-label">횡단 advice α</span>
    <strong class="wc-cross-name">근거 없이 단정 금지 — 4기능 모두에 weave</strong>
    <span class="wc-cross-tag">aspect</span>
  </div>

  <div class="wc-step-head"><span>step 3</span><strong>스펙</strong></div>
  <div class="wc-cell s-spec"><strong>spec.md</strong></div>
  <div class="wc-cell s-spec"><strong>spec.md</strong></div>
  <div class="wc-cell s-spec"><strong>spec.md</strong></div>
  <div class="wc-cell s-spec"><strong>spec.md</strong></div>

  <div class="wc-cross">
    <span class="wc-cross-label">횡단 advice β</span>
    <strong class="wc-cross-name">한국어 품질 — 사용자 가시 출력 전체에 weave</strong>
    <span class="wc-cross-tag">aspect</span>
  </div>

  <div class="wc-step-head"><span>step 4</span><strong>테스트</strong></div>
  <div class="wc-cell s-test"><strong>vitest</strong></div>
  <div class="wc-cell s-test"><strong>vitest</strong></div>
  <div class="wc-cell s-test"><strong>vitest</strong></div>
  <div class="wc-cell s-test"><strong>vitest</strong></div>

  <div class="wc-step-head"><span>step 5</span><strong>코드</strong></div>
  <div class="wc-cell s-code"><strong>app/**</strong></div>
  <div class="wc-cell s-code"><strong>app/**</strong></div>
  <div class="wc-cell s-code"><strong>app/**</strong></div>
  <div class="wc-cell s-code"><strong>app/**</strong></div>

  <div class="wc-legend">
    <span><i class="longi"></i>종단 — 약속 한 줄이 코드까지 내려가는 세로 chain</span>
    <span><i class="cross"></i>횡단 — 공통 advice가 step 사이를 가로질러 weave</span>
  </div>
</div>

이 그림은 메커니즘을 보여준다. 어디가 비었는지는 보지 못한다. 그래서 같은 두 축을 매트릭스로 다시 보면, 누락이 어느 칸에 있는지가 드러난다.

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

## 두 축이 한 격자에 있어야 빈틈이 보인다

종단만 본다면 이 매트릭스는 세로 줄로만 채워질 것이다. 약속이 어디까지 내려갔는지는 보이지만, 공통 규칙이 어느 기능에서 빠졌는지는 드러나지 않는다.

횡단만 본다면 반대다. 공통 규칙이 어느 기능에 적용됐는지는 보이지만, 그 기능 자체의 약속이 코드 표면까지 닫혔는지는 알 수 없다.

두 축을 한 격자에 같이 두면 어떤 종류의 빈틈인지가 비로소 드러난다. 약속 2가 리포트에서 누락됐다면 종단의 실패다. 공통 규칙 α가 워크스페이스에서 weave되지 않았다면 횡단의 실패다. 둘은 같은 "미통과"가 아니다. 다음 액션도 다르다.

여기서 한 가지 더. 코드가 지금 우연히 규칙을 따르고 있다가 아니라, 다음 변경에서도 사라지지 않도록 약속 구조 안에 규칙이 박혀 있다. 횡단이 보는 것은 일시적 일치가 아니라 약속 형식 안에 박힌 상태에 가깝다.

그래서 한 점수로 뭉개지 않는다. 종단과 횡단을 동시에 보는 매트릭스는 출시 판정을 게으르지 않게 만드는 도구라고 부를 수 있다.
