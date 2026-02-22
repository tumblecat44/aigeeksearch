# Geek Search Mode

Use this playbook when the user wants deep, relentless web research.

## Core Principle

Do not behave like a polite summarizer. Behave like a verification engine.

## Execution Checklist

1. Query fan-out
- Create 12+ queries before synthesis.
- Split by intent:
  - official pricing page discovery
  - official billing/credits policy
  - change history and pricing updates
  - community-reported edge cases
  - contradictions and disputes

2. Parallel collection
- Run independent searches in parallel.
- Keep searching until there is source convergence or explicit unresolved conflict.

3. Source prioritization
- Prefer this order:
  1) official pricing/help/blog/changelog
  2) official forum posts by maintainers
  3) trusted secondary writeups

4. Contradiction hunt
- For each major claim, run a dedicated query attempting to disprove it.
- If disproven, downgrade confidence and log the conflict.

5. Evidence minimum
- Per service row include:
  - at least 2 first-party sources when available
  - date checked
  - confidence score and band

6. Output integrity
- If uncertain, say unknown.
- Never invent exact numbers.
- Never hide disagreement between sources.

## Query Starters

- `site:{domain} pricing`
- `site:{domain} billing credits`
- `site:{domain} docs pricing usage`
- `site:{domain} changelog pricing`
- `site:{domain} blog pricing update`
- `"{product}" pricing changed`
- `"{product}" credits rollover`
- `"{product}" BYOK`
- `"{product}" overage`

## Stop Condition

Stop only when one of these is true:

- strong convergence across first-party sources
- unresolved conflict clearly documented
- no new signal after two additional fan-out iterations
