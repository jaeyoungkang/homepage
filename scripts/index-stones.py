#!/usr/bin/env python3
"""돌 인덱싱: stones/ 폴더의 마크다운 파일을 임베딩하여 검색 인덱스를 생성한다.

사용법:
  python3 scripts/index-stones.py
"""

import json
import os
import sys
import re
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


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """YAML frontmatter와 본문을 분리한다."""
    import yaml

    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}

    body = parts[2].strip()
    return meta, body


def build_text(meta: dict, body: str) -> str:
    """임베딩용 텍스트를 구성한다. tags + 본문."""
    tags = meta.get("tags", [])
    tag_str = ", ".join(tags) if tags else ""
    parts = []
    if tag_str:
        parts.append(f"[{tag_str}]")
    parts.append(body)
    return " ".join(parts)


def embed_texts(texts: list[str], batch_size: int = 100) -> np.ndarray:
    """OpenAI text-embedding-3-small로 텍스트 리스트를 임베딩한다."""
    from openai import OpenAI

    client = OpenAI()
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch,
        )
        for item in response.data:
            all_embeddings.append(item.embedding)

    return np.array(all_embeddings, dtype=np.float32)


def main():
    load_env()

    # stones/ 에서 .md 파일 수집 (README.md 제외)
    stone_files = sorted(
        f for f in STONES_DIR.glob("*.md") if f.name != "README.md"
    )

    if not stone_files:
        print("돌 파일이 없다.", file=sys.stderr)
        sys.exit(1)

    print(f"[인덱싱] {len(stone_files)}개 돌 발견")

    index = []
    texts = []

    for stone_path in stone_files:
        content = stone_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(content)

        text = build_text(meta, body)
        texts.append(text)

        raw_date = meta.get("date", "")
        date_str = str(raw_date) if raw_date else ""

        entry = {
            "file": stone_path.name,
            "date": date_str,
            "source": meta.get("source", ""),
            "tags": meta.get("tags", []),
            "used_in": meta.get("used_in", []),
            "text": text,
        }
        index.append(entry)

    # 임베딩 생성
    print("[임베딩] OpenAI text-embedding-3-small 호출 중...")
    embeddings = embed_texts(texts)
    print(f"[임베딩] 완료: {embeddings.shape}")

    # 저장
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"[저장] {INDEX_PATH}")

    np.save(EMBEDDINGS_PATH, embeddings)
    print(f"[저장] {EMBEDDINGS_PATH}")

    print(f"[완료] {len(index)}개 돌 인덱싱 완료")


if __name__ == "__main__":
    main()
