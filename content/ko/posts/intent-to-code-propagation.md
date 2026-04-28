---
title: "거친 의도가 코드가 될 때"
date: 2026-04-28
summary: "AI가 빠르게 구현하는 시대에 제작자의 의도를 코드 레벨까지 전파하고 검증하는 방법."
translationKey: "intent-to-code-propagation"
tags: ["생각", "경험"]
---

AI 시대의 문제는 코드를 못 만드는 것이 아니다. 오히려 반대다. 거친 의도가 너무 빨리 코드가 된다.

예를 들어 제작자가 이렇게 말한다고 하자.

> AI 코멘트가 너무 짧다. 좀 더 풍부한 설명을 줘야 한다.

사람끼리 일할 때는 이 문장 사이에 대화가 더 있었다. 풍부하다는 것이 무슨 뜻인지, 어느 화면에서 보여야 하는지, 사용자가 무엇을 판단할 수 있어야 하는지, 실패하면 무엇을 막아야 하는지를 서로 좁혀갔다.

그런데 AI에게 바로 맡기면 이 빈칸이 너무 빨리 채워진다. AI는 그럴듯한 구현을 만든다. 하지만 그 결과가 제작자의 의도와 맞는지는 별개의 문제다.

그래서 라이트하우스에서 만든 Mission Control은 버그 관리 도구가 아니다. 더 정확히는 **제작자의 의도가 코드와 실제 제품 동작으로 번역되는 과정을 살아 있게 만드는 운영 체계**다.

<div class="intent-visual intent-chain" role="img" aria-label="거친 의도가 사용자 약속, 검사 조건, 실행 가능한 스펙, 테스트와 판정, 코드 표면, 출시 판정으로 내려가는 흐름">
  <div class="intent-step hot"><span>01</span><strong>거친 의도</strong><em>더 풍부하게</em></div>
  <div class="intent-step"><span>02</span><strong>사용자 약속</strong><em>무엇을 보장하는가</em></div>
  <div class="intent-step"><span>03</span><strong>검사 조건</strong><em>무엇을 통과해야 하는가</em></div>
  <div class="intent-step blue"><span>04</span><strong>실행 스펙</strong><em>어떤 명령으로 확인하는가</em></div>
  <div class="intent-step blue"><span>05</span><strong>Judge / Validator</strong><em>구조와 의미를 나눠 본다</em></div>
  <div class="intent-step green"><span>06</span><strong>코드 표면</strong><em>사용자에게 보이는가</em></div>
  <div class="intent-step green"><span>07</span><strong>출시 판정</strong><em>내보내도 되는가</em></div>
</div>

첫 단계는 거친 말을 User Story로 바꾸는 것이다. User Story는 기능을 만들자가 아니라 사용자가 어떤 경험을 받을 수 있어야 하는가를 고정한다.

<div class="intent-visual intent-translate" role="img" aria-label="거친 말을 User Story로 바꾸는 예시">
  <div>
    <span class="intent-label">거친 말</span>
    <p>AI 코멘트가 너무 짧다.</p>
  </div>
  <div class="intent-pivot">의도를<br/>사용자 경험으로<br/>고정한다</div>
  <div>
    <span class="intent-label">User Story</span>
    <p>사용자는 AI 코멘트에서 판단 근거와 다음 행동을 읽을 수 있어야 한다.</p>
  </div>
</div>

그다음 이 약속을 Acceptance Criteria와 CIQ로 쪼갠다. Acceptance Criteria는 통과해야 하는 조건이다. CIQ는 애매한 의도를 정밀하게 만드는 판단 질문이다.

```text
이 설명은 단순 요약을 넘어서 판단 이유를 말하는가?
사용자가 다음 행동을 정할 수 있게 하는가?
근거가 부족할 때 확신하는 척하지 않는가?
```

이렇게 해야 풍부한 설명이라는 말이 구현 가능한 단위로 바뀐다. 조건으로 쪼갤 수 없는 약속은 아직 구현 요청이 아니다. 검증할 수 없는 조건은 아직 완료 기준이 아니다.

다음은 SpecDown이다. SpecDown은 문서를 그냥 읽는 문서로 두지 않고, 실행 가능한 스펙으로 다룬다. 스펙 안에는 어떤 User Story를 커버하는지, 어떤 명령을 실행해야 하는지, 어떤 결과가 나와야 하는지가 들어간다.

```text
스펙 문서
  ↓
Coverage By Story
  ↓
run:shell
  ↓
실제 테스트 명령
  ↓
리포트
```

여기서 Traceability가 작동한다. Traceability는 원래 요구사항 공학에 있는 개념이다. 요구사항이 설계, 테스트, 코드, 릴리즈까지 어떻게 연결되는지 추적하는 것이다. 라이트하우스에서는 User Story, 검사 조건, 스펙, 테스트 명령, 실행 파일, 코드 표면이 서로를 가리켜야 한다.

<div class="intent-visual intent-trace" role="img" aria-label="User Story 조건에서 앱 코드까지 이어지는 Traceability 흐름">
  <div><span>User Story</span><strong>조건</strong></div>
  <div><span>feature-specs</span><strong>ledger</strong></div>
  <div><span>spec 문서</span><strong>Coverage By Story</strong></div>
  <div><span>run:shell</span><strong>테스트 명령</strong></div>
  <div><span>실행 파일</span><strong>test target</strong></div>
  <div><span>app</span><strong>코드 표면</strong></div>
</div>

한쪽 방향만 보면 부족하다. 문서에서 코드로 내려가는 길도 있어야 하고, 코드에서 나는 어떤 사용자 약속을 구현하는가를 설명하는 길도 있어야 한다. 그래서 사용자에게 보이는 화면과 컴포넌트에는 Code Surface Tagging을 붙인다. 이름은 라이트하우스식 조합에 가깝지만, 코드 주석이나 어노테이션으로 책임과 소유권을 표시하는 방식은 원래 개발 현장에도 있다.

이 장치가 없으면 AI가 만든 코드가 고아가 된다. 화면은 생겼는데 어떤 의도에서 왔는지 모르는 상태가 된다.

검증도 한 종류로 뭉치지 않는다. 구조적 검증과 의미적 검증을 나눈다.

Validator는 구조를 본다. 스펙 파일이 있는가, run:shell이 있는가, Coverage By Story가 있는가, aspect 구조가 빠지지 않았는가를 본다.

Judge는 의미를 본다. 필드는 있고 화면에도 표시되지만, 그 내용이 정말 사용자가 판단할 만큼 충분한 설명인지 본다. AI 제품에서는 이 차이가 크다. 형식이 맞는 출력과 의도에 맞는 출력은 다르다.

Contract Test도 같은 맥락이다. Contract Test는 원래 API나 서비스 사이의 계약이 깨지지 않았는지 보는 테스트 방식이다. 라이트하우스에서는 스펙 문서가 약속한 입력, 출력, 동작 계약이 실제 구현에서 지켜지는지 확인하는 데 쓴다.

또 하나 중요한 구조는 횡단 규칙이다. 어떤 약속은 기능 하나에만 속하지 않는다.

<div class="intent-visual intent-matrix" role="img" aria-label="근거 없이 단정 금지, 한국어 품질, 상태 추적 같은 횡단 규칙이 검색, PDF, 워크스페이스, 리포트를 가로지르는 표">
  <div class="matrix-corner">Aspect</div>
  <div class="matrix-head">검색</div>
  <div class="matrix-head">PDF</div>
  <div class="matrix-head">워크스페이스</div>
  <div class="matrix-head">리포트</div>
  <div class="matrix-rule">근거 없이 단정 금지</div>
  <div class="matrix-cell hot">weave</div>
  <div class="matrix-cell hot">weave</div>
  <div class="matrix-cell hot">weave</div>
  <div class="matrix-cell hot">weave</div>
  <div class="matrix-rule">한국어 품질</div>
  <div class="matrix-cell blue">weave</div>
  <div class="matrix-cell blue">weave</div>
  <div class="matrix-cell blue">weave</div>
  <div class="matrix-cell blue">weave</div>
  <div class="matrix-rule">상태 추적</div>
  <div class="matrix-cell green">weave</div>
  <div class="matrix-cell green">weave</div>
  <div class="matrix-cell green">weave</div>
  <div class="matrix-cell green">weave</div>
</div>

이건 Aspect-Oriented Programming의 사고와 닮아 있다. AOP에서는 로깅, 보안, 트랜잭션처럼 여러 기능에 흩어지는 공통 관심사를 aspect로 분리한다. 라이트하우스에서는 AI 응답 포맷, 이벤트 중복 차단, 빠른 반응성, 한국어 품질 같은 제품 규칙을 aspect로 분리한다.

즉 이 규칙은 검색 기능에만 적용된다가 아니라 AI가 사용자에게 응답하는 모든 곳에 적용되어야 한다고 보는 것이다. 새 기능이 생기면 이 aspect가 적용되어야 하는지 다시 물을 수 있다.

마지막은 Quality Gate와 CI다. Quality Gate는 정해진 기준을 통과하지 못하면 merge, deploy, release를 막는 장치다. CI는 Continuous Integration, 변경이 들어올 때 자동으로 빌드와 테스트를 돌리는 개발 운영 방식이다.

라이트하우스에서는 format, lint, typecheck, unit test, coverage, SpecDown, Mission Control validator, dependency boundary check, duplication check, build가 함께 돈다. 하나의 테스트가 모든 신뢰를 책임지는 것이 아니라, 서로 다른 실패면을 여러 장치가 나눠서 막는다.

<div class="intent-visual intent-gates" role="img" aria-label="commit 전 gate, push 전 gate, CI gate, release 판정으로 이어지는 품질 게이트">
  <div><span>commit</span><strong>staged gate</strong><em>깨진 정렬 차단</em></div>
  <div><span>push</span><strong>quality:fast</strong><em>핵심 품질 확인</em></div>
  <div><span>CI</span><strong>full run</strong><em>빌드와 경계 검증</em></div>
  <div><span>release</span><strong>verdict</strong><em>네 신호 모두 green</em></div>
</div>

이런 구조를 만들고 나면 AI가 코드를 잘 짰는가보다 더 중요한 질문을 할 수 있다.

```text
이 코드는 어떤 사용자 약속에서 왔는가?
그 약속은 검사 조건으로 쪼개졌는가?
스펙과 테스트 명령으로 내려갔는가?
실제 코드 표면과 연결됐는가?
사용자가 보는 결과가 의도에 맞는가?
깨진 상태가 release로 나가지 못하게 막히는가?
```

신뢰도는 AI 모델 하나에서 나오지 않는다. User Story, SpecDown, Traceability, Aspect-Oriented 구조, Contract Test, Judge, Validator, Static Analysis, Code Surface Tagging, Quality Gate, CI 같은 기계적 장치들이 서로 맞물릴 때 생긴다.

라이트하우스에서 얻은 결론은 단순하다.

의도는 문서에만 있으면 죽는다. 코드에만 있으면 왜곡된다. 테스트에만 있으면 좁아진다.

그래서 의도는 문서, 스펙, 테스트, Judge, 코드, 출시 판정 전체를 따라 살아 있어야 한다. AI로 제품을 만든다는 건 AI에게 일을 맡기는 것이 아니라, AI가 너무 빨리 채우는 빈칸을 시스템적으로 드러내고 닫는 일에 가깝다.
