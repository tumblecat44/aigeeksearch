# AI Geek Search Plugin

`aigksh` is a Claude Code plugin that forces rigorous web research behavior for volatile facts such as pricing, billing, tokens, credits, and BYOK policy.

## What it does

- Clarify scope before deep research
- Run parallel source collection
- Prioritize first-party sources
- Perform contradiction-seeking checks
- Output table + evidence log + conflict log + confidence score
- Auto-route web-search-like prompts through the plugin skill via `UserPromptSubmit` hook
- Use a Silicon Valley signal network (official launches -> build signals -> market context -> social sentiment)
- Force trend outputs into `Adopt now / Watch / Ignore` decisions with weekly actions

## Install

First add your plugin marketplace, then install this plugin:

```text
/plugin marketplace add <marketplace-url>
/plugin install aigksh
```

If you installed an older plugin name first, remove it and reinstall:

```text
/plugin uninstall aigeeksearch
/plugin uninstall aigksh
/plugin install aigksh
```

After installation, restart Claude Code.

## Plugin structure

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `hooks/hooks.json`
- `hooks/auto-skill-router.py`
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
/aigksh:aggressive-web-research
```

For web-search-like prompts (latest/current/trends/pricing/billing/search/find), the hook injects routing context so Claude uses this skill workflow first.

## After install/update

Restart Claude Code after install or plugin updates so hooks and skill metadata are reloaded.

## Notes for marketplace

This repository already follows Claude plugin directory rules:

- manifest in `.claude-plugin/plugin.json`
- marketplace index in `.claude-plugin/marketplace.json`
- skills at plugin root under `skills/`
- namespaced invocation as `/aigksh:aggressive-web-research`
