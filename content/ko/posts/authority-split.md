---
title: "AI에게 무엇을 못 하게 했는가"
draft: true
date: 2026-04-28
summary: "AI 제품 운영의 핵심은 AI에게 무엇을 시켰는가가 아니다. 선언·전파·판정·차단 권한을 누가 갖는가의 분리에 가깝다."
translationKey: "authority-split"
tags: ["생각", "경험"]
---

AI 자율성 이야기는 보통 "어디까지 맡길 수 있는가"로 흐른다. 더 잘 시키는 법, 더 풍부한 컨텍스트를 주는 법, 더 큰 작업을 맡기는 법을 다룬다.

그런데 그 방향에서 한 발 비켜서면, 같은 무게로 따라오는 질문이 하나 있다.

> AI는 자기가 만든 결과를 스스로 통과시킬 수 있는가.

라이트하우스를 만들면서 점점 또렷해진 건 이 질문이었다. 무엇을 시킬지보다, **무엇을 못 하게 했는가**가 운영 체계를 결정하는 데 가까웠다.

분리가 없는 상태를 떠올리면 쉽다. AI가 거친 의도를 자기 식으로 해석하고, 그 해석으로 구현하고, 자기 결과를 스스로 통과시킨다. 사람은 결과가 나온 뒤에야 "이게 맞나" 하고 뒤늦게 본다. 빈칸을 빠르게 채우는 능력 자체는 잘못이 아니다. 채운 사람이 동시에 판정자가 되는 구조가 위험에 가깝다.

AI가 빈칸을 채우는 게 문제가 아니라, AI가 자기 결과를 스스로 통과시키는 게 문제다.

그래서 라이트하우스는 권한을 네 자리로 나눴다. Human, Agent, Evaluator, System. 각자 할 수 있는 것이 있고, **할 수 없는 것**이 더 분명하게 있다.

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

사람은 약속을 선언한다. AI는 그 약속을 아래로 전파한다. 평가자는 결과를 판단한다. 시스템은 실패 상태를 막는다.

이 네 줄에서 더 중요한 건 "할 수 있는 것"보다 "할 수 없는 것"에 가깝다. 사람은 약속을 정할 수 있지만 게이트를 우회하지는 못한다. AI는 문서·스펙·코드를 만들 수 있지만 met 판정을 자기 손으로 찍지는 못한다. 평가자는 충족 여부를 판단할 수 있지만 코드를 고치거나 약속 자체를 바꾸지 않는다. 시스템은 실패를 막을 수 있지만 의도를 해석하거나 판정하지 않는다.

이 분리가 없으면 다시 원래 문제로 돌아간다. AI가 약속을 해석한다, AI가 구현한다, AI가 스스로 통과시킨다, 사람은 결과가 맞는지 뒤늦게 본다. 한 자리에 두 권한이 겹치는 순간, 빈칸 채움 문제가 다시 살아난다.

Mission Control이 단순한 문서 묶음이 아니라 운영 체계인 이유는 여기에 가깝다. 문서는 무엇을 약속했는지를 적는다. 운영 체계는 그 약속을 누가 선언하고, 누가 전파하고, 누가 판정하고, 누가 막는지를 분리해서 강제한다. AI 자율성을 어디까지 늘릴지에 대한 답은, 결국 이 분리를 어디까지 단단하게 유지할 수 있는가에서 나오는 것에 가깝다.
