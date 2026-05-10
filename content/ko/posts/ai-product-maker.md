---
title: "AI 제품을 만드는 영역을 탐색한다는 것"
draft: true
date: 2026-04-10
summary: "아직 정답이 없는 영역이다. 그래서 직접 만들어보면서 배운다."
translationKey: "ai-product-maker"
tags: ["생각"]
---

AI 제품을 만드는 일은 아직 교과서가 없는 영역이다. 모델의 성능은 매달 올라가고, 어제의 best practice가 오늘의 안티패턴이 된다. 그래서 이 분야에서 일한다는 건, 정해진 길을 따라가는 게 아니라 길을 만들면서 걷는 것에 가깝다.

내가 직접 부딪히면서 배운 것들이 있다. 예를 들어, 처음에는 프롬프트 하나를 잘 쓰면 좋은 제품이 나올 거라고 생각했다. 하지만 실제로 제품을 운영하면서 깨달은 건, 프롬프트는 빙산의 일각이라는 것이다. 진짜 어려운 건 LLM의 출력을 사용자가 신뢰할 수 있는 형태로 가공하고, 실패했을 때 자연스럽게 처리하며, 전체 흐름 안에서 녹여내는 일이다.

> 이 분야를 탐색하면서 가장 크게 바뀐 생각: AI 제품의 본질은 기술이 아니라, 기술과 사람 사이의 간극을 설계하는 것이다.

아직 모르는 게 훨씬 많다. AI 에이전트가 사용자와 어떻게 관계를 맺어야 하는지, 기억 시스템은 어떤 구조여야 하는지, 에이전트에게 어디까지 자율성을 줄 수 있는지. 이런 질문들에 대한 답은 논문에도 없고, 직접 만들어보면서 하나씩 찾아가는 수밖에 없다.

코드로 표현하면 이런 느낌이다:

```python
class AIProduct:
    def __init__(self, user_context, model):
        self.context = user_context
        self.model = model
        self.fallback = GracefulFallback()

    def solve(self, problem):
        try:
            raw = self.model.generate(
                problem=problem,
                context=self.context,
            )
            return self.refine(raw)
        except ModelError:
            return self.fallback.handle(problem)

    def refine(self, raw_output):
        """모델 출력을 사용자가 신뢰할 수 있는 형태로 변환"""
        validated = self.validate(raw_output)
        return self.format_for_human(validated)
```

<div style="background:#f6f6f6;border-radius:8px;padding:2rem;text-align:center;color:#999;margin:1.5rem 0;">
  [ 이미지: AI 제품 개발 워크플로우 다이어그램 ]
</div>

결국 나는 이 영역을 탐색하고 개발하는 사람이다. 완성된 전문가가 아니라, 매일 새로운 것을 실험하고 배우는 사람. 그 과정에서 발견한 것들을 여기에 기록하려고 한다.
