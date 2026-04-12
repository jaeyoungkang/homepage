# Stones — 내러티브 메모리 기반 글감 검색

자연석(Fieldstone) 기법의 돌 저장소. 원본은 mirror-mind 내러티브 메모리에 있다.

## 구조

- **원본**: `~/mirror-mind/memory/narratives/sessions/*.json` + `topics/*.json`
- **인덱스**: `index.json` + `embeddings.npy` (로컬 전용, gitignore)
- **생성**: `close-session.py` 실행 시 자동 갱신

## 사용법

```bash
# 인덱스 갱신 (보통 close-session.py가 자동 실행)
python3 scripts/index-stones.py

# 글감 검색
python3 scripts/find-stones.py --query "에이전트 자유도 제한"
python3 scripts/find-stones.py --query "삭제" --tags "decision" --top 5
python3 scripts/find-stones.py --query "키워드" --json  # 파이프라인용
```

## 돌 단위

| 소스 | 돌 1개 |
|------|--------|
| 세션 내러티브 event | decision/discovery/direction/question 1개 |
| 주제 thesis | 주제의 현재 핵심 주장 |
| 주제 open_question | 아직 답이 없는 질문 |
| 주제 changelog | 주제가 바뀐 기록 1건 |
