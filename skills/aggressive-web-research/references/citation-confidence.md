# Citation Confidence Rules

Use this rubric for every factual claim.

## Score Formula

Compute confidence as:

`score = 0.40*A + 0.25*R + 0.20*S + 0.15*C`

Where each component is in `[0, 1]`:

- `A` (Authority): official product domain and first-party docs score highest
- `R` (Recency): recently updated pages or dated changelogs score higher
- `S` (Specificity): exact pricing and billing semantics score higher than summaries
- `C` (Consistency): agreement across independent sources

## Confidence Bands

- `HIGH`: score >= 0.80
- `MEDIUM`: 0.60 <= score < 0.80
- `LOW`: score < 0.60

## Required Citation Format

For each row or claim include:

- Source URL
- Checked date (YYYY-MM-DD)
- Confidence score and band

Example:

`Source: https://cursor.com/pricing | Checked: 2026-02-22 | Confidence: 0.86 (HIGH)`

## Conflict Handling

If two sources disagree:

1. Prefer official source over third-party source
2. Prefer newer timestamp when authority is equal
3. Keep both claims in a conflict log
4. Mark row as uncertain if conflict cannot be resolved from primary sources
