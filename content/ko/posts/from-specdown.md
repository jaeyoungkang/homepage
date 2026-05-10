---
title: "처음엔 SpecDown만 있었다"
draft: true
date: 2026-04-28
summary: "라이트하우스의 정렬 시스템은 한 번에 만들어지지 않았다. SpecDown에서 출발해 User Story와 AOP, 검증 강화로 확장된 진화의 서사."
translationKey: "from-specdown"
tags: ["생각", "경험"]
---

라이트하우스의 정렬 시스템은 처음부터 일곱 단계가 다 있던 것이 아니다. 처음엔 한 가지 도구만 있었다. SpecDown.

[SpecDown](https://github.com/corca-ai/specdown)은 문서와 코드 사이의 일치를 목적으로 만든 도구다. 문서를 그냥 읽는 글로 두지 않고, 그 안의 명령과 검증 블록을 실행 가능한 계약으로 다룬다. 잘만 쓰면 "문서가 곧 테스트"가 된다.

처음엔 그게 답일 거라고 생각했다. 문서가 실행되면 코드와 문서가 어긋날 일이 줄어든다. 그러면 AI가 만든 코드도 문서를 기준으로 검증할 수 있다.

## 한계 1 — 스펙 자체가 잘 만들어지지 않았다

문제는 그다음에서 드러났다. 스펙이 잘 만들어지지 않는다. 무엇을 쪼개야 할지가 흐리고, 어디서부터 시작해야 할지가 비어 있다. 실행 가능한 형식은 정해졌는데, 그 안에 무엇을 적을지가 매번 새로웠다.

원인은 위에 있었다. 거친 의도가 약속으로 좁혀지기 전에 스펙으로 내려오면, 스펙이 그 빈칸을 떠안는다. SpecDown이 정직하게 동작할수록 빈칸이 더 도드라졌다.

그래서 앞단에 한 층을 더 두기로 했다. User Story.

## 해결 1 — User Story로 약속을 먼저 고정

User Story는 "기능을 만들자"가 아니라 "사용자가 어떤 경험을 받을 수 있어야 하는가"를 고정한다. 약속이 정해지면 검사 조건(AC)과 판단 질문(CIQ)으로 쪼갤 수 있다. 쪼개진 조건이 SpecDown으로 내려온다.

실제로 어떻게 바뀌었는지 한 사례로 보면 이렇다. 라이트하우스 초기에 "AI 코멘트가 너무 짧다, 풍부한 설명을 줘야 한다"는 요청이 있었다. 그대로 받으면 SpecDown은 "코멘트 길이가 N자 이상"이라는 형식 조건만 만들 수 있다. 그러면 길긴 하지만 의도와 어긋난 코멘트가 통과한다.

User Story 단계를 거치면 같은 요청이 다음으로 좁혀진다.

<div class="intent-visual intent-translate" role="img" aria-label="거친 말이 User Story로 좁혀지는 사례">
  <div>
    <span class="intent-label">거친 말</span>
    <p>AI 코멘트가 너무 짧다.</p>
  </div>
  <div class="intent-pivot">User Story로<br/>약속을<br/>고정한다</div>
  <div>
    <span class="intent-label">User Story</span>
    <p>사용자는 AI 코멘트에서 판단 근거와 다음 행동을 읽을 수 있어야 한다.</p>
  </div>
</div>

이렇게 좁혀지면 AC가 자연스럽게 따라온다. "코멘트는 단순 요약을 넘어 판단 이유를 포함한다", "사용자가 다음에 무엇을 할 수 있는지 제안한다", "근거가 부족하면 확신하는 척하지 않는다." 이 조건들이 SpecDown 안에 그대로 검증 블록으로 내려온다. 스펙이 잘 만들어지지 않던 것은 형식 문제가 아니라 위에서 내려올 약속이 비어 있었던 문제에 가까웠다는 게 이때 분명해졌다.

## 한계 2 — 종단은 닫혔지만 횡단이 빠졌다

User Story가 생기자 새로운 한계가 보였다. User Story는 한 기능 한 줄을 책임진다. 한 약속이 검사 조건과 스펙과 코드까지 내려갔는지를 본다. 이걸 종단이라고 부른다.

그런데 어떤 규칙은 한 기능에만 속하지 않는다. "근거 없이 단정하지 않는다", "한국어 품질을 지킨다" 같은 규칙은 검색에도, PDF에도, 워크스페이스에도, 리포트에도 동시에 걸린다. User Story 한 줄로는 이런 규칙이 흩어진다. 어떤 기능에선 잘 지키고 다른 기능에선 슬쩍 빠져 있어도 종단 검증은 통과한다.

가로로 흐르는 규칙을 책임지는 자리가 비어 있다는 뜻이었다.

## 해결 2 — AOP로 횡단 규칙을 별도 축에

여기서 빌려 온 사고가 Aspect-Oriented Programming이다. AOP에서는 로깅이나 보안처럼 여러 기능에 흩어지는 공통 관심사를 aspect로 분리한다. 라이트하우스에서는 AI 응답 포맷이나 한국어 품질 같은 제품 규칙을 같은 방식으로 떼어냈다.

Pointcut으로 적용 대상을 정하고, Advice로 주입할 규칙을 적고, Weaving으로 그 규칙이 각 약속 안에 박혀 있는지를 본다. 종단을 책임지는 User Story와 횡단을 책임지는 Aspect가 두 축으로 나뉘었다.

사례를 라이트하우스의 실제 POL 하나로 보면 이렇다. **POL-RESPOND-001 — AI 반응 포맷**. 한 줄 표어나 단순 편수 나열로 닫지 않고 결과·문서의 의도·방법·결과를 충분히 설명하되, 마크다운 없이 평문으로, 본문 한도 안에서 닫는다. 이 규칙은 검색 기능에만 속하지 않는다. LLM이 만드는 모든 사용자 가시 응답에 걸린다.

User Story 한 줄에 묶어두면 어떤 응답에선 잘 지키고 다른 응답에선 표어 한 줄로 닫히는 일이 생긴다. Aspect로 떼어내면 한 advice가 6개 US 사이트에 동시에 weave된다.

<div class="intent-visual advice-fanout" role="img" aria-label="POL-RESPOND-001 AI 반응 포맷 advice가 검색 3개와 PDF 3개 사이트에 weave되는 사례">
  <div class="fan-source">
    <span>POL-RESPOND-001 · advice</span>
    <strong>충분한 설명, 평문, 본문 한도 안에서</strong>
    <em>title ≤ 30자 · body ≤ 400자 평문 · 표어 한 줄이나 단순 편수 나열로 닫지 않는다 · LLM이 만드는 모든 사용자 가시 응답에 걸린다.</em>
  </div>
  <div class="fan-arms">
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-SEARCH-01-02</strong>
      <em>검색 직후 가이드 트리 응답</em>
    </div>
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-SEARCH-02-02</strong>
      <em>추가 검색 응답</em>
    </div>
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-SEARCH-03-03</strong>
      <em>후속 액션 응답</em>
    </div>
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-PDF-01-02</strong>
      <em>PDF 응답</em>
    </div>
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-PDF-02-02</strong>
      <em>PDF 멀티모달 응답</em>
    </div>
    <div class="fan-arm">
      <span>pointcut</span>
      <strong>US-PDF-03-01</strong>
      <em>PDF 에러 상황 응답</em>
    </div>
  </div>
</div>

advice 하나가 6개 US AC에 동시에 박혀 있고, 검증은 한 곳(`specs/respond-contract.spec.md` §Sufficiency Review)이 α(Coverage: 6 US 응답이 모두 한도 통과)와 β(Wovenness: 6 US CIQ가 본문 충분성을 측정)를 한꺼번에 본다. 새 응답 사이트가 추가되면 그 자리에서 "이 aspect가 적용되어야 하는가"를 다시 묻게 된다. 공통 규칙이 한 기능 안에 숨어버리는 일이 줄었다.

## 강화 — 검증을 늘려 시스템을 두껍게

여기까지 와서 마지막으로 한 일이 검증의 강화다.

Judge는 "이 출력이 정말 의도에 맞는가"를 의미적으로 본다. Validator는 "구조가 빠지지 않았는가"를 본다. Contract Test는 입력·출력·동작 계약이 실제 구현에서 지켜지는지 확인한다. Quality Gate와 CI는 깨진 상태가 다음 단계로 못 넘어가게 막는다.

각 검증은 다른 종류의 실패를 막는다. 형식만 맞춘 출력, 구조 누락, 계약 위반, 우회 시도. 검증이 한 종류였을 때 새어 나가던 것들이 그제야 잡히기 시작했다.

<div class="intent-visual verification-shield" role="img" aria-label="Judge, Validator, Contract Test, Quality Gate 네 검증 장치가 각자 다른 실패면을 막는다">
  <div class="vs-cell judge">
    <span class="vs-no">01</span>
    <strong>Judge</strong>
    <em class="vs-asks">"이 출력이 정말 의도에 맞는가"를 의미적으로 본다.</em>
    <em class="vs-fail"><b>막는 실패</b>형식은 맞지만 의도와 어긋난 출력</em>
  </div>
  <div class="vs-cell validator">
    <span class="vs-no">02</span>
    <strong>Validator</strong>
    <em class="vs-asks">"구조가 빠지지 않았는가"를 본다. 스펙·run:shell·Coverage·태그.</em>
    <em class="vs-fail"><b>막는 실패</b>중간 연결이나 표면 태그 누락</em>
  </div>
  <div class="vs-cell contract">
    <span class="vs-no">03</span>
    <strong>Contract Test</strong>
    <em class="vs-asks">입력·출력·동작 계약이 실제 구현에서 지켜지는가.</em>
    <em class="vs-fail"><b>막는 실패</b>스펙과 코드 사이 계약 위반</em>
  </div>
  <div class="vs-cell gate">
    <span class="vs-no">04</span>
    <strong>Quality Gate · CI</strong>
    <em class="vs-asks">깨진 상태가 commit / push / release로 못 넘어간다.</em>
    <em class="vs-fail"><b>막는 실패</b>말로만 있는 규칙 · 우회</em>
  </div>
</div>

같은 실패를 네 번 막는 구조가 아니다. 의미·구조·계약·차단으로 실패면을 나눠서 각각 다른 자리에서 잡는다. 한 자리에 다 맡기지 않은 게 시스템을 두껍게 만들었다.

<div class="intent-visual evolution-stack" role="img" aria-label="SpecDown만 있던 시점에서 User Story, AOP, 검증 강화가 차례로 누적되며 시스템이 두꺼워지는 진화 서사">
  <div class="evo-col">
    <span class="evo-phase">Phase 1</span>
    <strong class="evo-title">SpecDown만</strong>
    <div class="evo-stack">
      <div class="evo-layer l-spec fresh"><span>실행 가능 계약</span><strong>SpecDown</strong></div>
    </div>
    <em class="evo-note">문서와 코드의 일치만 본다. 스펙 자체가 비어 있으면 작동하지 않는다.</em>
    <i class="evo-arrow">→</i>
  </div>

  <div class="evo-col">
    <span class="evo-phase">Phase 2</span>
    <strong class="evo-title">+ User Story</strong>
    <div class="evo-stack">
      <div class="evo-layer l-spec"><span>이전</span><strong>SpecDown</strong></div>
      <div class="evo-layer l-us fresh"><span>NEW · 종단</span><strong>User Story · AC · CIQ</strong></div>
    </div>
    <em class="evo-note">약속을 먼저 고정한다. 종단 한 줄이 닫히기 시작한다.</em>
    <i class="evo-arrow">→</i>
  </div>

  <div class="evo-col">
    <span class="evo-phase">Phase 3</span>
    <strong class="evo-title">+ AOP</strong>
    <div class="evo-stack">
      <div class="evo-layer l-spec"><span>이전</span><strong>SpecDown</strong></div>
      <div class="evo-layer l-us"><span>이전</span><strong>User Story · AC · CIQ</strong></div>
      <div class="evo-layer l-aop fresh"><span>NEW · 횡단</span><strong>Aspect · Pointcut · Weaving</strong></div>
    </div>
    <em class="evo-note">여러 기능을 가로지르는 규칙을 별도 축으로 관리한다.</em>
    <i class="evo-arrow">→</i>
  </div>

  <div class="evo-col">
    <span class="evo-phase">Phase 4</span>
    <strong class="evo-title">+ 검증 강화</strong>
    <div class="evo-stack">
      <div class="evo-layer l-spec"><span>이전</span><strong>SpecDown</strong></div>
      <div class="evo-layer l-us"><span>이전</span><strong>User Story · AC · CIQ</strong></div>
      <div class="evo-layer l-aop"><span>이전</span><strong>Aspect · Pointcut · Weaving</strong></div>
      <div class="evo-layer l-gate fresh"><span>NEW · 차단</span><strong>Judge · Validator · Gate · CI</strong></div>
    </div>
    <em class="evo-note">서로 다른 실패면을 여러 장치가 나눠서 막는다.</em>
  </div>
</div>

## 한 번에 만들어지지 않았다

지금 보면 일곱 단계가 깔끔하게 늘어선 스택처럼 보인다. 하지만 그 모양은 처음부터 그려진 게 아니라, 한 단계의 한계가 다음 단계를 부르면서 차례로 쌓인 것에 가깝다.

SpecDown만으론 빈칸이 떠안겼다. User Story를 얹자 종단이 닫혔다. 종단만으론 횡단이 새어 나갔다. AOP를 얹자 두 축이 채워졌다. 검증을 강화하자 여러 종류의 실패가 분리됐다.

정렬 시스템은 한 번 그린 도면이 아니라, 자기 한계를 발견하면서 자란 운영 체계에 가깝다. 다음 한계가 다음 층을 부른다. 그게 이 스택의 진짜 형태다.
