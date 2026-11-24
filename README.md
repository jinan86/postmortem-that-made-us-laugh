# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/jinan86/postmortem-that-made-us-laugh/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/jinan86/postmortem-that-made-us-laugh/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) competition **The Postmortem That Made Us Laugh**: one short account (one sentence, 217 characters) of the silliest time an AI coding agent misunderstood what it was asked.

## The story

> I asked the agent to add rate limiting to the login endpoint; it applied the limit per instance, so with twelve replicas running, an attacker got twelve times the attempts — the fix was a bulk discount on brute force.

## How it runs

`main.py` (Python 3.13, deterministic, no network) writes the story to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

Two runs produce byte-identical output (verified via `sha256sum`).
