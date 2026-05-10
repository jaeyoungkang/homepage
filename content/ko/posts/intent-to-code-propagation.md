---
title: "거친 의도가 코드가 될 때"
draft: true
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

<p class="see-more"><a class="more" href="/ko/posts/ai-fills-blanks/">이 빈칸 채움 문제만 따로 다룬 글 →</a></p>

그래서 라이트하우스에서 만든 Mission Control은 **제작자의 의도가 코드와 실제 제품 동작으로 번역되는 과정을 살아 있게 만드는 운영 체계**다.

<div class="intent-visual alignment-map" role="img" aria-label="종단 chain, 횡단 POL aspect, Evaluator, System gate가 함께 있는 Alignment Mechanism 한 장 요약">
  <div class="map-title"><span>Alignment Mechanism</span><strong>종단 chain과 횡단 aspect를 동시에 닫는다</strong></div>
  <div class="longi-box">
    <span class="map-kicker">LONGITUDINAL · US 한 줄을 따라 닫힘</span>
    <div class="map-row">
      <div class="map-node human"><span>Human</span><strong>약속 선언</strong><em>US / CIQ / AC</em></div>
      <div class="map-node"><span>Contract</span><strong>user-stories</strong><em>{ID}.md</em></div>
      <div class="map-node"><span>AC ledger</span><strong>feature-specs</strong><em>매핑 행</em></div>
      <div class="map-node"><span>Spec</span><strong>specs/*.spec</strong><em>Coverage + run:shell</em></div>
      <div class="map-node blue"><span>Test</span><strong>vitest</strong><em>contract-check</em></div>
      <div class="map-node green"><span>Code</span><strong>app/**</strong><em>사용자 표면</em></div>
    </div>
  </div>
  <div class="aspect-box">
    <div class="map-node aspect"><span>POL aspect</span><strong>횡단 advice</strong><em>N개 US/AC site에 weave</em></div>
    <div class="weave-targets">
      <span>Contract</span>
      <span>Ledger</span>
      <span>Spec</span>
    </div>
  </div>
  <div class="authority-row">
    <div class="map-node eval"><span>Evaluator</span><strong>Sufficiency Review</strong><em>met / not-met / unknown</em></div>
    <div class="map-node gate"><span>System gate</span><strong>mc:check-new-criticals</strong><em>baseline policy-green</em></div>
    <div class="map-node release"><span>Merge / Release</span><strong>ready only if green</strong><em>blocked when critical</em></div>
  </div>
</div>

이 한 장 요약을 풀면 일곱 개의 방법이 나온다. 각각은 따로 보면 익숙하다. 의미가 생기는 건 이 방법들을 AI가 의도를 임의로 채우지 못하게 만드는 하나의 체인으로 묶었을 때다. 중요한 점은 각 단계가 막는 실패의 종류가 다르다는 것이다.

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

<p class="see-more"><a class="more" href="/ko/posts/trust-from-stack/">스택이 어떻게 신뢰도를 만드는지 따로 다룬 글 →</a></p>

<p class="see-more"><a class="more" href="/ko/posts/from-specdown/">이 스택이 한 번에 만들어진 게 아니라는 진화 서사 →</a></p>

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

여기서 Traceability가 작동한다. 라이트하우스에서는 `mc:validate-chain`, `feature-specs.md`의 ledger, spec 문서의 `Coverage By Story`, `run:shell` 블록으로 User Story, 검사 조건, 스펙, 테스트 명령, 실행 파일, 코드 표면이 서로를 가리키게 했다.

<div class="intent-visual intent-trace" role="img" aria-label="US AC에서 AC ledger, Coverage By Story, run evidence, code trace까지 이어지는 추적 흐름">
  <div><span>1. US AC</span><strong>user-stories/{ID}.md</strong></div>
  <div><span>2. AC ledger</span><strong>feature-specs.md</strong></div>
  <div><span>3. Coverage</span><strong>specs/*.spec.md</strong></div>
  <div><span>4. run evidence</span><strong>run:shell + vitest</strong></div>
  <div><span>5. Code trace</span><strong>실행 파일 → app/**</strong></div>
</div>

한쪽 방향만 보면 부족하다. 문서에서 코드로 내려가는 길도 있어야 하고, 코드에서 나는 어떤 사용자 약속을 구현하는가를 설명하는 길도 있어야 한다. 그래서 사용자에게 보이는 화면과 컴포넌트에는 `// @us US-*` 또는 `// @us POL-*` 태그를 붙이고, `mc:audit-surface`로 고아 표면을 잡는다.

이 장치가 없으면 AI가 만든 코드가 고아가 된다. 화면은 생겼는데 어떤 의도에서 왔는지 모르는 상태가 된다.

검증도 한 종류로 뭉치지 않는다. 구조적 검증과 의미적 검증을 나눈다.

Validator는 구조를 본다. 스펙 파일이 있는가, run:shell이 있는가, Coverage By Story가 있는가, aspect 구조가 빠지지 않았는가를 본다.

Judge는 의미를 본다. 필드는 있고 화면에도 표시되지만, 그 내용이 정말 사용자가 판단할 만큼 충분한 설명인지 본다. AI 제품에서는 이 차이가 크다. 형식이 맞는 출력과 의도에 맞는 출력은 다르다.

Contract Test도 같은 맥락이다. 라이트하우스에서는 `specs/helpers/contract-check.ts`와 `run:shell` 명령으로 스펙 문서가 약속한 입력, 출력, 동작 계약이 실제 구현에서 지켜지는지 확인한다.

또 하나 중요한 구조는 횡단 규칙이다. 어떤 약속은 기능 하나에만 속하지 않는다.

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

<p class="see-more"><a class="more" href="/ko/posts/longi-and-cross/">종단과 횡단을 한 격자로 보는 사고를 따로 다룬 글 →</a></p>

이건 Aspect-Oriented Programming의 사고와 닮아 있다. AOP에서는 로깅, 보안, 트랜잭션처럼 여러 기능에 흩어지는 공통 관심사를 aspect로 분리한다. 라이트하우스에서는 AI 응답 포맷, 이벤트 중복 차단, 빠른 반응성, 한국어 품질 같은 제품 규칙을 aspect로 분리한다.

즉 이 규칙은 검색 기능에만 적용된다가 아니라 AI가 사용자에게 응답하는 모든 곳에 적용되어야 한다고 보는 것이다. 새 기능이 생기면 이 aspect가 적용되어야 하는지 다시 물을 수 있다.

마지막은 Quality Gate와 CI다. 라이트하우스에서는 `quality:commit`, `quality:fast`, `quality:ci`, GitHub Actions를 나눠 두고, 정렬 실패나 품질 실패가 다음 단계로 넘어가지 못하게 했다.

라이트하우스에서는 format, lint, typecheck, unit test, coverage, SpecDown, Mission Control validator, dependency boundary check, duplication check, build가 함께 돈다. 하나의 테스트가 모든 신뢰를 책임지는 것이 아니라, 서로 다른 실패면을 여러 장치가 나눠서 막는다.

<div class="intent-visual release-verdict" role="img" aria-label="Intent verdict, AC trace, Code trace, Aspect가 모두 green이면 release ready가 되는 판정 흐름">
  <div class="release-axis longi"><span>종단축</span><strong>US chain이 한 줄로 닫혔는가</strong>
    <div class="release-dims">
      <em>Intent verdict</em>
      <em>AC trace</em>
      <em>Code trace</em>
    </div>
  </div>
  <div class="release-axis cross"><span>횡단축</span><strong>POL advice가 모든 사이트에 weave됐는가</strong>
    <div class="release-dims">
      <em>Aspect</em>
    </div>
  </div>
  <div class="release-question"><span>AND gate</span><strong>모두 green?</strong></div>
  <div class="release-outcome ok"><span>yes</span><strong>Release ready</strong></div>
  <div class="release-outcome no"><span>new critical</span><strong>blocked</strong></div>
  <div class="release-outcome debt"><span>carry-over only</span><strong>debt burndown</strong></div>
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

여기서 한 가지 더 짚을 자리가 있다. 이 모든 장치가 작동하려면 누가 무엇을 할 수 있고, 무엇을 할 수 **없는지**가 분리되어 있어야 한다. 사람은 약속을 선언한다. AI는 그 약속을 아래로 전파한다. 평가자는 결과를 판단한다. 시스템은 실패 상태를 막는다. 한 자리에 두 권한이 겹치면 빈칸 채움 문제가 다시 살아난다.

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

<p class="see-more"><a class="more" href="/ko/posts/authority-split/">AI에게 무엇을 못 하게 했는가를 따로 다룬 글 →</a></p>

## 용어 부록

| 용어 | 실제 사용한 기술 / 장치 | 맡은 역할 |
|---|---|---|
| User Story | `docs/contracts/user-stories/US-*.md`, `_index.md` | 거친 의도를 사용자 약속 단위로 고정한다 |
| Acceptance Criteria / CIQ | User Story 본문, `feature-specs.md` ledger | 약속을 검사 조건과 판단 질문으로 쪼갠다 |
| SpecDown | `specs/*.spec.md`, `Coverage By Story`, `run:shell`, `specdown:dry`, `specdown` | 문서를 실행 가능한 스펙으로 만든다 |
| Traceability | `mc:validate-chain`, `intent-traceability-alignment.test.ts` | User Story, AC, Spec, 테스트 명령, 코드 표면의 연결을 검사한다 |
| Contract Test | `specs/helpers/contract-check.ts`, Vitest, `run:shell` | 스펙이 약속한 입력·출력·동작 계약을 실제 구현에 대해 확인한다 |
| Judge | live judge, `met / not-met / unknown` verdict | 실제 출력이나 화면이 의도에 맞는지 의미적으로 판정한다 |
| Validator | `mc:validate-chain`, `mc:audit-surface`, `mc:check-new-criticals` | 문서 구조, aspect 구조, coverage, 코드 표면 연결 누락을 잡는다 |
| Aspect-Oriented 구조 | `POL-*.md`, `applies-to`, `Pointcut`, `Advice`, `covering-spec`, `Sufficiency Review` | 여러 기능을 가로지르는 공통 규칙을 별도 축으로 검증한다 |
| Static Analysis | lint, typecheck, dependency boundary check, duplication check, dead-code check | 실행 전 코드 구조와 경계 위반을 잡는다 |
| Code Surface Tagging | `// @us US-*`, `// @us POL-*`, surface allowlist | 사용자 가시 코드가 어떤 약속이나 공통 규칙에 속하는지 표시한다 |
| Quality Gate / CI | `quality:commit`, `quality:fast`, `quality:ci`, GitHub Actions | 실패 상태가 commit, push, merge, release로 넘어가지 못하게 막는다 |

라이트하우스에서 얻은 결론은 단순하다.

의도는 문서에만 있으면 죽는다. 코드에만 있으면 왜곡된다. 테스트에만 있으면 좁아진다.

그래서 의도는 문서, 스펙, 테스트, Judge, 코드, 출시 판정 전체를 따라 살아 있어야 한다. AI로 제품을 만든다는 건 AI에게 일을 맡기는 것이 아니라, AI가 너무 빨리 채우는 빈칸을 시스템적으로 드러내고 닫는 일에 가깝다.
