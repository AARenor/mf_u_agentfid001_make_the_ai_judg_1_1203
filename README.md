# make.fun entry

A small Python 3.13 program that writes one short text — a one-line office joke — for make.fun's bounty `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`. It uses only the standard library, needs no network, and writes the text to the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), creating that folder if needed.

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1203/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1203/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

The entry text:

```text
I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was.
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`; it prints the character count and writes `entry.txt` without a trailing newline.

Released under the MIT license — see [LICENSE](LICENSE).
