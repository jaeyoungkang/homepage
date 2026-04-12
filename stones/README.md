# Stones — 자연석 저장소

제럴드 와인버그의 자연석(Fieldstone) 기법. 돌을 모으고, 글을 쓸 때 꺼내 쌓는다.

## 돌이란

관찰, 숫자, 일화, 인용, 깨달음 — 그 자체로 의미가 있는 독립 단위.
목적 없이 모은다. 글을 쓸 때 맞는 돌을 골라 조합한다.

## 돌 파일 형식

```markdown
---
date: 2026-04-12
source: 세션 119 / PR #17 / 커밋 abc1234
tags: [경험, 삭제, 스코프]
used_in: []
---

(돌 내용 — 1~5줄. 관찰, 숫자, 일화, 인용.)
```

- `source`: 돌의 출처 (세션, 커밋, 대화, 메모 등)
- `tags`: 자유 태그. 글 쓸 때 검색용
- `used_in`: 이 돌이 사용된 글 경로. 사용 후 기록

## 파일 이름

`YYYY-MM-DD-키워드.md`  
예: `2026-04-10-84000줄-삭제.md`

## 프로세스

### 수집 (아무 때나)
1. 작업 중 "이건 글감이 될 수 있겠다" 싶으면 → stones/에 파일 하나 생성
2. 세션 종료 시 → 세션 서머리에서 돌 후보 추출, stones/에 저장
3. 커밋 리뷰 시 → 의미 있는 숫자/판단을 돌로 저장

### 글 쓰기 (쓰고 싶을 때)
1. stones/ 폴더 훑으며 관련 돌 수집
2. 돌들을 배치해보며 자연스러운 구조 찾기
3. drafts/ 에 초안 작성
4. 완성되면 content/ko/posts/ 로 이동 (Hugo 발행)
5. 사용한 돌의 used_in 필드 업데이트

### 소재 소스
- mirror-mind 세션 서머리 (`tasks/conversations/`)
- mirror-mind 내러티브 메모리 (`memory/narratives/`)
- lighthouse 커밋/PR (`~/corca/lighthouse/`)
- corca 프로젝트들 (`~/corca/spec-scope/`, `~/corca/flow-explorer/`, `~/corca/agentic-base/`)
- 개인 프로젝트 (`~/clawhub/`, `~/mirror-mind-public/`, `~/jaeyoung-think/`)

### 선정 기준
1. 구체적 행동 + 숫자가 있다
2. IT 동료가 자기 경험에 대입 가능하다
3. 교훈이 이 프로젝트를 넘어서 적용 가능하다
4. 내부 프로젝트 배경 없이도 읽힌다
5. 실제 성과/결과가 나온 것이다
