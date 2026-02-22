#!/usr/bin/env python3
import json
import re
import sys


WEB_INTENT_PATTERNS = [
    r"\blatest\b",
    r"\brecent\b",
    r"\bcurrent\b",
    r"\btrend(s)?\b",
    r"\bnews\b",
    r"\bfind\b",
    r"\bsearch\b",
    r"\bcompare\b",
    r"\bpricing\b",
    r"\bbilling\b",
    r"\btoken(s)?\b",
    r"\bcredit(s)?\b",
    r"\bbyok\b",
    r"최신",
    r"트렌드",
    r"찾아",
    r"검색",
    r"비교",
    r"가격",
    r"요금",
    r"토큰",
    r"크레딧",
]


def needs_web_skill(prompt: str) -> bool:
    lowered = prompt.lower()
    for pattern in WEB_INTENT_PATTERNS:
        if re.search(pattern, lowered):
            return True
    return False


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        sys.exit(0)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(0)

    prompt = data.get("prompt", "")
    if not isinstance(prompt, str) or not prompt.strip():
        sys.exit(0)

    if not needs_web_skill(prompt):
        sys.exit(0)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": (
                "MANDATORY ROUTING: This prompt requires web or freshness-sensitive research. "
                "Before using direct web tools, invoke /aigksh:aggressive-web-research "
                "and follow its workflow (clarify-first, parallel search, confidence scoring, "
                "conflict log, citation-backed output)."
            ),
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
