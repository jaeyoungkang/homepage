---
title: "How I work"
translationKey: "how-i-work"
summary: "Making products has become easier in the AI era. Making products that actually deliver the promised value to users and run reliably is still hard."
---

In the AI era, making a product has become easier. Coding agents take half-formed ideas and turn them into product form. But making a product that actually delivers the promised value to users and runs reliably is still hard.

In this piece, *intent* refers to what value the product delivers to the user, and how.

## The AI fills in the gaps on its own

A half-formed idea has many gaps. What the product guarantees to the user. How it should respond when input goes wrong. Whether a rule held in one feature should also hold in others. None of it is decided up front.

The coding agent fills those gaps on its own. In the prototype stage it looks fine. But as the product moves toward something real, the places that were filled in on the fly start distorting the value that was promised.

Cleaning those up after the fact piles complexity onto the code. Dependencies tangle. Fixing one place makes another behave differently. Decisions that should have been made up front come back as debt.

## Three directions for working on this problem

**Sharpen the product intent.** A person decides what the product guarantees to the user. Agents can draft, but meaning approval stays with the human. You can't catch every gap up front. So the team builds a stable procedure for filling each gap as it surfaces.

**Carry the intent through to the code.** Write down what the product guarantees (the promise) and verify that promise in two strands. One is a deterministic check — the conditions that were spelled out pass against the code. The other is a meaning check — what the user actually receives still carries the promised meaning. Rules that span features apply consistently across all of them, not just one. The release verdict is not a single pass/fail line but a breakdown by which dimension passed and which didn't.

**Hold complexity down during the build.** Stacking the two items above tends to pile verification code and "don't do X" rules alongside them. Pushed too far, the code structure stops holding intent directly, and an external stack of guards starts standing in for it. So before adding more guards, look at whether the structure itself can be reshaped so that the bad behavior becomes unrepresentable.

## What 100x productivity really means

In the AI era, the product maker focuses on sharpening the intent of the product. AI has opened that space.

The real meaning of "100x productivity" sits there. It's not that AI replaces planning or coding. It's that AI provides the environment for a person to do the more important and harder work — sharpening the intent and designing how it carries through the product into coherent value for the user — far more effectively.

## Lighthouse is the sample

This way of working grew out of operating [lighthouse](/en/work/lighthouse/) — a document workspace for research work.

Chapters that go deep on each direction are filled in over time.
