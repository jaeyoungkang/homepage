#!/usr/bin/env python3
"""돌 인덱싱: mirror-mind 내러티브 메모리에서 events를 추출해 검색 인덱스를 생성한다.

소스:
  - mirror-mind/memory/narratives/sessions/*.json → events 단위
  - mirror-mind/memory/narratives/topics/*.json → thesis + open_questions + changelog

사용법:
  python3 scripts/index-stones.py
  python3 scripts/index-stones.py --since 2026-04-05  # 날짜 필터
"""

import json
import os
import sys
import argparse
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
MIRROR_MIND = Path.home() / "mirror-mind"
NARRATIVES_DIR = MIRROR_MIND / "memory" / "narratives"
SESSIONS_DIR = NARRATIVES_DIR / "sessions"
TOPICS_DIR = NARRATIVES_DIR / "topics"

# 인덱스는 homepage/stones/ 에 저장 (기존 호환)
STONES_DIR = PROJECT_ROOT / "stones"
INDEX_PATH = STONES_DIR / "index.json"
EMBEDDINGS_PATH = STONES_DIR / "embeddings.npy"


def load_env():
    env_path = MIRROR_MIND / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, val = line.partition("=")
                    os.environ.setdefault(key.strip(), val.strip())


def extract_session_events(since: str | None = None) -> list[dict]:
    """세션 내러티브에서 event 단위 돌을 추출한다."""
    entries = []
    for path in sorted(SESSIONS_DIR.glob("*.json")):
        data = json.loads(path.read_text("utf-8"))
        date = data.get("date", "")
        if since and date < since:
            continue

        session_id = data.get("id", path.stem)
        title = data.get("title", "")
        events = data.get("events", [])
        entities = data.get("entities", [])
        topic_refs = data.get("topic_refs", [])

        # 태그: kind + topic_refs + entities
        for i, ev in enumerate(events):
            kind = ev.get("kind", "")
            content = ev.get("content", "")
            if not content:
                continue

            tags = [kind] if kind else []
            tags.extend(topic_refs[:3])  # 상위 3개 토픽만

            text = f"[{session_id}] {content}"
            entries.append({
                "file": f"{session_id}/event-{i}",
                "date": date,
                "source": f"{session_id} — {title}",
                "tags": tags,
                "used_in": [],
                "text": text,
            })

    return entries


def extract_topic_entries() -> list[dict]:
    """주제 내러티브에서 thesis, open_questions, 최근 changelog를 추출한다."""
    entries = []
    for path in sorted(TOPICS_DIR.glob("*.json")):
        data = json.loads(path.read_text("utf-8"))
        topic_id = data.get("id", path.stem)
        title = data.get("title", "")
        domain_tags = data.get("domain_tags", [])
        last_activity = data.get("last_activity", "")

        # thesis
        thesis = data.get("thesis", "")
        if thesis:
            entries.append({
                "file": f"topic/{topic_id}/thesis",
                "date": last_activity,
                "source": f"topic — {title}",
                "tags": ["thesis"] + domain_tags[:2],
                "used_in": [],
                "text": f"[{topic_id}] {thesis}",
            })

        # open_questions
        for j, q in enumerate(data.get("open_questions", [])):
            entries.append({
                "file": f"topic/{topic_id}/question-{j}",
                "date": last_activity,
                "source": f"topic — {title}",
                "tags": ["question"] + domain_tags[:2],
                "used_in": [],
                "text": f"[{topic_id}] {q}",
            })

        # 최근 changelog 3개
        changelog = data.get("changelog", [])
        for ch in changelog[-3:]:
            ch_date = ch.get("date", "")
            what = ch.get("what_changed", "")
            if what:
                entries.append({
                    "file": f"topic/{topic_id}/change-{ch_date}",
                    "date": ch_date,
                    "source": f"topic — {title} ({ch.get('session', '')})",
                    "tags": ["변화"] + domain_tags[:2],
                    "used_in": [],
                    "text": f"[{topic_id}] {what}",
                })

    return entries


def embed_texts(texts: list[str], batch_size: int = 100) -> np.ndarray:
    from openai import OpenAI
    client = OpenAI()
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch,
        )
        for item in response.data:
            all_embeddings.append(item.embedding)
    return np.array(all_embeddings, dtype=np.float32)


def main():
    parser = argparse.ArgumentParser(description="내러티브 메모리 → 돌 인덱싱")
    parser.add_argument("--since", default=None, help="세션 날짜 필터 (YYYY-MM-DD)")
    args = parser.parse_args()

    load_env()

    # 추출
    session_entries = extract_session_events(since=args.since)
    topic_entries = extract_topic_entries()
    all_entries = session_entries + topic_entries

    if not all_entries:
        print("추출된 항목이 없다.", file=sys.stderr)
        sys.exit(1)

    print(f"[추출] 세션 events: {len(session_entries)}, 주제 항목: {len(topic_entries)}, 총: {len(all_entries)}")

    texts = [e["text"] for e in all_entries]

    # 임베딩
    print("[임베딩] OpenAI text-embedding-3-small 호출 중...")
    embeddings = embed_texts(texts)
    print(f"[임베딩] 완료: {embeddings.shape}")

    # 저장
    STONES_DIR.mkdir(exist_ok=True)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)
    print(f"[저장] {INDEX_PATH}")

    np.save(EMBEDDINGS_PATH, embeddings)
    print(f"[저장] {EMBEDDINGS_PATH}")

    print(f"[완료] {len(all_entries)}개 항목 인덱싱 완료")


if __name__ == "__main__":
    main()
