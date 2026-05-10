---
title: "신뢰도는 모델이 아니라 스택에서 온다"
draft: true
date: 2026-04-28
summary: "AI 제품의 신뢰도는 모델 한 줄에서 나오지 않는다. 의도를 잃지 않게 만드는 일곱 개의 기계적 장치가 맞물려 만들어진다."
translationKey: "trust-from-stack"
tags: ["생각", "경험"]
---

AI 제품이 흔들릴 때 가장 자주 듣는 답은 "모델이 더 똑똑해지면 된다"이다. 하지만 모델을 바꿔도 같은 자리에서 비슷한 어긋남이 다시 돈다. 신뢰도는 모델이 아니라 그 위에 쌓인 스택에서 오는 것에 가깝다.

라이트하우스에서 의도가 코드까지 내려가는 길을 닫으면서 본 것도 그렇다. 새로운 마법 도구 하나가 답을 준 것이 아니다. 이미 소프트웨어 공학에 있던 방법들을 AI 개발 환경에 맞게 다시 묶었을 뿐이다.

중요한 점은 각 방법이 맡는 구간이 다르다는 것이다. User Story는 거친 의도를 사용자 약속 단위로 자르고, Acceptance Criteria와 CIQ는 약속을 검사 가능한 조건으로 쪼갠다. SpecDown은 문서를 실행 가능한 계약으로 만들고, Traceability는 약속과 코드가 서로를 가리키게 한다. Aspect-Oriented 구조는 여러 기능을 가로지르는 공통 규칙을 따로 다루고, Judge와 Validator와 Contract Test는 구조적 성공과 의미적 성공을 나눠 검증한다. Quality Gate와 CI는 깨진 상태가 다음 단계로 넘어가지 못하게 막는다.

각각은 따로 보면 익숙하다. 의미가 생기는 건 이 방법들을 **AI가 의도를 임의로 채우지 못하게 만드는 하나의 체인**으로 묶었을 때다.

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

이 그림에서 가장 중요한 건 오른쪽의 "막는 실패" 칸이다. 일곱 단계가 각자 다른 종류의 실패를 막는다. 같은 실패를 일곱 번 막는 게 아니다.

User Story가 빠지면 의도가 구현 가능한 단위로 잘리지 않는다. AC와 CIQ가 빠지면 "풍부하다" 같은 말이 검사 가능한 조건이 되지 못한다. SpecDown이 빠지면 문서가 읽히기만 할 뿐 실행되지 않는다. Traceability가 빠지면 약속에서 코드 사이 어딘가에서 연결이 끊긴다. Aspect-Oriented 구조가 빠지면 여러 기능에 걸리는 공통 규칙이 한 기능 안에 숨어 사라진다. Judge·Validator·Contract Test가 빠지면 형식만 맞춘 그럴듯한 출력이 통과한다. Quality Gate가 빠지면 깨진 상태가 그대로 main과 release로 흘러간다.

한 단계만 빠져도 다른 단계가 만든 신뢰도가 그쪽으로 새어 나간다. 그래서 이 스택은 더하기가 아니라 곱하기에 가깝다.

신뢰도는 AI가 똑똑해서 생기는 것이 아니다. **AI가 빠뜨리기 쉬운 중간 단계를 시스템이 강제로 요구하기 때문에** 생긴다. 모델이 한 번 더 영리해지길 기다리는 대신, 의도가 새지 않도록 일곱 개의 자리를 미리 만들어 두는 일에 가깝다.
