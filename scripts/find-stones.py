#!/usr/bin/env python3
"""돌 시맨틱 검색: 쿼리와 가장 유사한 돌을 찾는다.

사용법:
  python3 scripts/find-stones.py --query "에이전트 자유도 제한"
  python3 scripts/find-stones.py --query "삭제" --tags "경험,숫자" --top 5
"""

import json
import argparse
import os
import sys
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
STONES_DIR = PROJECT_ROOT / "stones"
INDEX_PATH = STONES_DIR / "index.json"
EMBEDDINGS_PATH = STONES_DIR / "embeddings.npy"


def load_env():
    """mirror-mind .env에서 OPENAI_API_KEY를 로드한다."""
    env_path = Path.home() / "mirror-mind" / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, val = line.partition("=")
                    os.environ.setdefault(key.strip(), val.strip())


def embed_query(query: str) -> np.ndarray:
    """쿼리를 임베딩한다."""
    from openai import OpenAI

    client = OpenAI()
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[query],
    )
    return np.array(response.data[0].embedding, dtype=np.float32)


def cosine_similarity(query_vec: np.ndarray, embeddings: np.ndarray) -> np.ndarray:
    """코사인 유사도를 계산한다."""
    # 정규화
    query_norm = query_vec / max(np.linalg.norm(query_vec), 1e-10)
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1
    emb_normed = embeddings / norms
    return emb_normed @ query_norm


def main():
    parser = argparse.ArgumentParser(description="돌 시맨틱 검색")
    parser.add_argument("--query", required=True, help="검색 쿼리")
    parser.add_argument("--tags", default="", help="태그 필터 (쉼표 구분)")
    parser.add_argument("--top", type=int, default=10, help="반환 개수 (기본: 10)")
    parser.add_argument("--json", action="store_true", help="JSON 포맷 출력")
    args = parser.parse_args()

    # 인덱스 존재 확인
    if not INDEX_PATH.exists() or not EMBEDDINGS_PATH.exists():
        print(
            "[오류] 인덱스가 없다. 먼저 index-stones.py를 실행하라.",
            file=sys.stderr,
        )
        sys.exit(1)

    load_env()

    # 로드
    with open(INDEX_PATH, encoding="utf-8") as f:
        index = json.load(f)

    embeddings = np.load(EMBEDDINGS_PATH)

    # 태그 필터
    tag_filter = set()
    if args.tags:
        tag_filter = {t.strip() for t in args.tags.split(",") if t.strip()}

    if tag_filter:
        filtered_indices = [
            i
            for i, entry in enumerate(index)
            if tag_filter & set(entry.get("tags", []))
        ]
        if not filtered_indices:
            print("[결과 없음] 해당 태그를 가진 돌이 없다.", file=sys.stderr)
            sys.exit(0)
        index = [index[i] for i in filtered_indices]
        embeddings = embeddings[filtered_indices]

    # 쿼리 임베딩
    query_vec = embed_query(args.query)

    # 유사도 계산
    similarities = cosine_similarity(query_vec, embeddings)

    # 상위 N개
    top_n = min(args.top, len(index))
    top_indices = np.argsort(similarities)[::-1][:top_n]

    results = []
    for idx in top_indices:
        entry = index[idx]
        sim = float(similarities[idx])
        results.append(
            {
                "file": entry["file"],
                "similarity": round(sim, 4),
                "tags": entry.get("tags", []),
                "date": entry.get("date", ""),
                "text": entry["text"],
            }
        )

    # 출력
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"[검색] \"{args.query}\" → 상위 {top_n}개\n")
        for i, r in enumerate(results, 1):
            tags_str = ", ".join(r["tags"]) if r["tags"] else "-"
            preview = r["text"][:80] + "..." if len(r["text"]) > 80 else r["text"]
            print(f"{i}. [{r['similarity']:.4f}] {r['file']}")
            print(f"   태그: {tags_str}")
            print(f"   {preview}")
            print()


if __name__ == "__main__":
    main()
