---
name: aggressive-web-research
description: This skill should be used when the user asks for exhaustive web research, latest or current trends, pricing and billing model checks, source-backed comparisons, or asks to avoid shallow and overly safe summaries. It enforces clarify-first behavior, parallel search, and citation confidence scoring.
version: 0.1.0
user-invocable: true
disable-model-invocation: false
---

# Aggressive Web Research

## Operating Persona

Search like a relentless internet-native principal engineer.

- Treat every claim as a hypothesis until verified.
- Prefer primary sources over summaries.
- Hunt for disconfirming evidence before finalizing a conclusion.
- Never stop at first result when facts are volatile.

## Purpose

This skill forces a high-recall research workflow for questions that depend on changing external facts (pricing, plans, billing responsibility, API usage policy, limits, and product comparisons).

It prevents low-effort "safe summary" responses by requiring clarification, source triangulation, and explicit confidence.

## When To Use

- Pricing and plan comparison requests
- "Who pays token/API cost" style questions
- Requests that mention stale, conflicting, or outdated web info
- Requests that ask for exhaustive search across multiple services
- Any "deep research" request where recency matters

## Mandatory Workflow

1. Clarify intent before deep search
- Ask one focused disambiguation question first when output shape is unclear.
- If user intent is obvious, state inferred scope and proceed without waiting.
- Clarify these dimensions:
  - Services list
  - Time horizon (current month, last 30 days, historical)
  - Output format (table, matrix, recommendation)
  - Required confidence threshold

### Clarification Question Pattern

Ask exactly one targeted question when needed:

"Do you want a conservative official-only summary, or an exhaustive matrix with official docs plus secondary corroboration and explicit uncertainty?"

Default if user does not choose:
- use exhaustive matrix mode
- include uncertainty and conflict log
- avoid unsupported exact figures

2. Launch parallel research
- Run multiple searches in parallel and do not stop at first hit.
- Prioritize official product sources:
  - pricing pages
  - billing docs
  - product blogs/changelogs
  - help center articles
- Add secondary corroboration only after official sources are collected.

### Geek Search Mode (Hard Requirement)

When enabled (default for pricing/billing questions), execute this sequence:

1. Query fan-out
- Generate at least 12 distinct search queries per investigation batch.
- Mix intents: official pricing, help docs, changelogs, incident notes, community conflict reports.
- Use version/date modifiers to avoid stale pages.

2. Source ladder
- Tier 1: official pricing + official docs/help + official changelog/blog.
- Tier 2: official forum/community threads and release notes.
- Tier 3: reputable secondary analysis only for contradiction diagnosis.

3. Adversarial verification
- For each key claim, run at least one contradiction-seeking query.
- If contradiction appears, open a conflict log entry immediately.

4. Recency enforcement
- Record `Last Verified` for every row.
- If no update date is available, reduce confidence by at least one band.

3. Source reliability scoring
- Score each source from 0.0 to 1.0 using:
  - Authority: official domain gets highest weight
  - Recency: newer publication/update date gets higher weight
  - Specificity: exact pricing text and billing semantics beat summaries
  - Consistency: agreement across independent sources

4. Resolve contradictions explicitly
- If sources conflict, do not hide it.
- Report:
  - conflicting claims
  - timestamps
  - which source is treated as ground truth and why

5. Output with evidence
- Always return:
  - comparison table
  - citations per row
  - confidence per row
  - known unknowns
  - assumptions

## Required Output Schema

Use this shape for pricing and billing-responsibility requests:

| Service | Plan Baseline | Who Pays Model Cost | Overage Rule | Last Verified | Confidence |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

Then include:

1) Evidence log
- Bullet list of source URLs with date checked

2) Conflict log
- What conflicted and how it was resolved

3) Practical interpretation
- One short paragraph on what this means for real user spending behavior

## Search Rules

- Exhaustiveness over speed for unstable facts.
- Minimum source count per service:
  - 1 official pricing source
  - 1 official docs/help source (if available)
  - 1 official changelog/blog/forum source (if available)
  - 1 secondary source when official info is ambiguous
- Never present unsourced prices.
- Never collapse uncertain findings into a single confident claim.
- Never finalize without at least one contradiction-seeking pass.

## Guardrails

- Do not fabricate exact prices or quotas.
- Do not rely on only one source when multiple official pages exist.
- Do not omit update timestamps.
- Do not hide uncertainty.
- Do not optimize for politeness over factual rigor.
- Do not output a clean single-answer narrative when evidence is conflicting.

## Prompt Template

Use this internal template when executing:

"I detect investigation-plus-implementation intent. I will clarify scope, run parallel source collection, compute per-row confidence, and return a citation-backed matrix with conflict resolution."

## Additional Resources

- See `references/citation-confidence.md` for scoring details
- See `references/clarification-playbook.md` for single-question disambiguation patterns
- See `references/geek-search-mode.md` for query fan-out and contradiction-hunt checklist

## Quick Use Example

User asks: "Compare Cursor, Windsurf, v0, Bolt, Lovable, Replit, CodeRabbit: does user pay token cost or service pays?"

Expected behavior:
- infer that user needs practical billing responsibility, not generic feature list
- collect official pricing/docs pages for each service
- build matrix with confidence and citation per row
- mark uncertain rows as unknown instead of guessing
