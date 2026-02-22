# Pricing and Billing Responsibility Matrix (2026-02-22)

| Service | Plan Baseline | Who Pays Model Cost | Overage Rule | Last Verified | Confidence |
| --- | --- | --- | --- | --- | --- |
| Cursor | Pro starts at $20/mo | Included usage pool first; user pays overage when enabled | Usage billed at API-like rates after included pool | 2026-02-22 | 0.86 (HIGH) |
| Windsurf | Pro starts at $15/mo with prompt credits | Platform includes monthly credits; user buys add-ons after depletion | Add-on credits purchased as needed | 2026-02-22 | 0.90 (HIGH) |
| v0 | Premium $20/mo with included credits | Platform includes monthly credits and token-metered model pricing | Buy additional credits beyond included usage | 2026-02-22 | 0.88 (HIGH) |
| Bolt.new | Pro starts at $25/mo with token allowance | Platform includes token bucket | Hard token/plan limits and reload workflow, not simple open-ended PAYG | 2026-02-22 | 0.83 (HIGH) |
| Lovable | Credit-based subscription plans | Platform includes credits; user buys top-ups | Top-up purchases when credits run low | 2026-02-22 | 0.70 (MEDIUM) |
| Replit | Core starts at $20/mo with included credits | Platform includes credits; additional usage can become pay-as-you-go | Additional usage billed beyond included credits | 2026-02-22 | 0.87 (HIGH) |
| CodeRabbit | Per-developer subscription | Flat SaaS seat pricing model, no exposed user token bucket | Seat-based billing rather than explicit token overage | 2026-02-22 | 0.84 (HIGH) |

## Evidence Log

- https://cursor.com/pricing - checked: 2026-02-22
- https://cursor.com/blog/june-2025-pricing - checked: 2026-02-22
- https://windsurf.com/pricing - checked: 2026-02-22
- https://docs.windsurf.com/windsurf/accounts/usage - checked: 2026-02-22
- https://v0.dev/pricing - checked: 2026-02-22
- https://bolt.new/pricing - checked: 2026-02-22
- https://support.bolt.new/account-and-subscription/tokens - checked: 2026-02-22
- https://docs.lovable.dev/introduction/plans-and-credits - checked: 2026-02-22
- https://replit.com/pricing - checked: 2026-02-22
- https://www.coderabbit.ai/pricing - checked: 2026-02-22

## Conflict Log

- Cursor:
  - Some older third-party posts describe request-based limits.
  - Official pages and official blog describe included usage pools and updated usage semantics.
  - Resolution: official pages/blog treated as source of truth.
- Lovable:
  - Main site pricing content was not consistently fetchable in this session.
  - Docs page provided credit mechanics and plan semantics.
  - Resolution: confidence reduced to MEDIUM until pricing page snapshot is captured directly.

## Practical Interpretation

Most products blend subscription with metered usage abstractions (credits or tokens). Real user spend risk is highest where pay-as-you-go overage is enabled and lowest where usage hard-stops at plan limits.
