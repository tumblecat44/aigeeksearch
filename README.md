# AI Geek Search Plugin

`aigeeksearch` is a Claude Code plugin that forces rigorous web research behavior for volatile facts such as pricing, billing, tokens, credits, and BYOK policy.

## What it does

- Clarify scope before deep research
- Run parallel source collection
- Prioritize first-party sources
- Perform contradiction-seeking checks
- Output table + evidence log + conflict log + confidence score

## Plugin structure

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `skills/aggressive-web-research/SKILL.md`
- `skills/aggressive-web-research/references/*`
- `skills/aggressive-web-research/templates/*`
- `skills/aggressive-web-research/examples/*`

## Local test

```bash
claude --plugin-dir ./
```

Then invoke:

```text
/aigeeksearch:aggressive-web-research
```

## Notes for marketplace

This repository already follows Claude plugin directory rules:

- manifest in `.claude-plugin/plugin.json`
- marketplace index in `.claude-plugin/marketplace.json`
- skills at plugin root under `skills/`
- namespaced invocation as `/aigeeksearch:aggressive-web-research`
