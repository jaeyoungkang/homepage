---
title: "Games After NPCs"
date: 2026-09-17
summary: "If humans and AI agents become players under the same rules, game agents will need both fast intuition and slow deliberation."
translationKey: "after-npc-human-agent-players"
tags: ["Thoughts"]
draft: false
---

The games I want to make will ultimately have no NPCs. Humans and AI agents will be players in the same world, governed by the same rules. Their behavior alone will not make it easy to tell which is which.

The important question is not whether an agent can talk like a person. It is whether the agent can perceive, react immediately, deliberate when necessary, and let experience change its next decision.

## System 1 and System 2

Daniel Kahneman described human thought in terms of a fast, automatic System 1 and a slower, deliberative System 2. I believe this distinction can be turned into an architecture for player agents.

[TypeSafe AI's Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) returns probabilities and confidence over predefined choices instead of generating prose. It could serve as a System 1 layer for judgments such as whether something is threatening, whom to trust, whether to speak, or whether to continue a plan. An LLM can take the System 2 role: setting longer-term goals, comparing alternatives, negotiating, and reflecting on failure.

Combining the two does not automatically produce a human-like agent. Jev is not the whole of human intuition, and an LLM does not deliberate merely because it generates a long answer. A control structure must decide when the agent should act immediately and when it should think further.

```text
Perception and memory
  → Jev: intuition, threat, trust, action preference
  → Control: act now or escalate to the LLM
  → LLM: planning, negotiation, reflection, goal revision
  → Action
  → Feed the result back into memory and relationships
```

Ordinary, familiar situations can end in System 1. A close distribution between choices, a novel situation, or a consequential decision such as an alliance or betrayal should invoke System 2. After deliberation, plans and memories change, and those changes become inputs to the next intuitive judgment.

## Human likeness comes from coherent limits

Giving an agent the complete game state will not make it human-like. The moment it knows hidden information, exact values, and a perfect history, it becomes a different kind of being. To become a player under the same conditions, it needs the same field of view, the same action surface, limited attention, and incomplete memory.

Its mistakes cannot be random either. A timid player should overestimate danger. A vengeful player may pursue an enemy despite the disadvantage. A player who has been betrayed should take longer to trust a similar gesture. When errors follow from personality and experience, they read as the behavior of one continuous subject.

## What it means for NPCs to disappear

An NPC is usually content placed for a human player. It performs an assigned role, reacts when the player arrives, and stops when the player leaves.

The agent described here is different. It has goals and memories of its own. It cooperates or competes with humans, experiences failure, and changes its next judgment. It continues to exist under the world's rules even when no human is watching. This is not about making NPCs smarter. It is about dissolving the NPC category into the category of players.

The game can disclose that humans and agents share its world without labeling every individual. That is not a trick that hides an agent's identity. It is a rule of a world in which two kinds of subjects meet as players.

This is still a product hypothesis, not an implementation result. Jev is newly released, and its effect in games has not been validated. The first experiment should be a small game built around trust, cooperation, and betrayal rather than combat performance. That is where we can see whether the combination of System 1 and System 2 creates more than a faster AI—whether it creates a subject worth playing with.

