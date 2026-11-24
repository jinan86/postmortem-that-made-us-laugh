#!/usr/bin/env python3
"""Entry program for make.fun: The Postmortem That Made Us Laugh.

Writes one short postmortem story (one sentence, <=400 chars) about an
AI coding agent that misunderstood a rate-limiting request, to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "I asked the agent to add rate limiting to the login endpoint; "
    "it applied the limit per instance, so with twelve replicas running, "
    "an attacker got twelve times the attempts "
    "\u2014 the fix was a bulk discount on brute force."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate mirror: 1-400 chars, one sentence, plain UTF-8 text.
    assert 1 <= len(text) <= 400, f"entry length {len(text)} out of range"
    assert text.endswith("."), "entry must end with a full stop"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
