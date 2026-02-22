# Sample Output Shape

| Service | Plan Baseline | Who Pays Model Cost | Overage Rule | Last Verified | Confidence |
| --- | --- | --- | --- | --- | --- |
| Cursor | Pro includes usage credit pool | Shared model cost via included pool, then user-funded overage if enabled | Additional usage billed at cost when spend enabled | 2026-02-22 | 0.84 |
| Windsurf | Pro monthly prompt credits | Service includes monthly credit allocation; user pays add-on credits when exhausted | Add-on credits consumed after monthly credits | 2026-02-22 | 0.89 |

## Evidence Log

- https://cursor.com/blog/june-2025-pricing - checked: 2026-02-22
- https://windsurf.com/pricing - checked: 2026-02-22
- https://docs.windsurf.com/windsurf/accounts/usage - checked: 2026-02-22

## Conflict Log

- Cursor:
  - Claim A (official blog): Pro includes a monthly usage pool and optional overage at cost.
  - Claim B (third-party articles): request-based limits and older quotas.
  - Resolution: treat official post as ground truth due to authority and recency.

## Practical Interpretation

Most modern coding assistants blend subscription with metered usage. Budget risk increases during heavy agentic workflows because token consumption variance scales with task complexity.
