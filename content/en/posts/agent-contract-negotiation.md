---
title: "How AI Agents Negotiate Requirements"
date: 2026-05-22
summary: "While building a paper search product, we had to move from the Semantic Scholar API to an internal literature index. My desire became a requirement, and the worker on the other side treated it as a customer request while still defending performance and compatibility."
translationKey: "agent-contract-negotiation"
tags: ["experience", "thoughts"]
draft: false
---

I am building a paper search product. A user enters a query, sees related papers, and uses abstracts, authors, citation links, and PDF availability to decide what to read first. At first, the product called the Semantic Scholar API directly. Later, for operational reasons, we needed to move that path to an internal literature index API.

That created a very concrete API need. A search result with only a title was not enough. Users needed abstracts, authors, citation links, PDF availability, and source information to judge the result and decide what to do next. I wanted the new API contract to reflect as much of that shape as possible.

So the request did not simply list fields. It explained why each field mattered. A title supports the first relevance check. An abstract reduces false positives. Citation links let a user move through prior and follow-up work. A PDF link connects discovery to reading. Metadata that looks decorative on the surface was actually part of how the product preserved the user's ability to judge.

The worker on the other side said they treated this as a requirement from a customer. That mattered. The request was not treated as an internal preference or a convenience request from a neighboring project. It was treated as a real product need from a product that would consume the new API. But the worker did not ask their agent to implement it as-is. The agent was asked to inspect the related projects and judge the request by strict criteria: whether it was desirable, whether it could be implemented without major performance cost, whether it was general enough beyond one product, and whether existing CLI clients would remain compatible.

The opposing agent did not reject the request. It defended the API boundary. Instead of making the search endpoint heavier, it kept search lightweight and proposed a separate batch hydration endpoint for richer paper data. It separated search results from detailed paper records. That was not exactly the shape I initially wanted, but it still preserved the user's ability to judge results.

Our agent then reviewed that decision and accepted it. The original desire still mattered. I would have preferred the first shape to pass through unchanged. But a more important question took over: does the user keep the necessary judgment cues, and can the product avoid presenting provider limitations as facts about the research field? The answer was yes, so we accepted the contract and started the product-side implementation.

This is what made the episode interesting. The agents were not just executing tasks. They were participating in a structured negotiation. People supplied desire and criteria. The worker on the other side treated the desire as a customer requirement while still protecting the broader contract. The agents defended constraints, restructured the request, and turned it into a form both sides could work with.
