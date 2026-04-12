---
date: 2026-04-03
source: "세션 116 — Codex Progress Board 자동화"
tags: [도구, 외부화, 에이전트]
used_in: []
---

codex-progress.py 스크립트 작성. lsof로 활성 세션 감지, 최근 72시간 내 세션 탐색, source=exec 세션을 필터링해 latest.json 생성. --watch N 모드로 주기적 갱신.
