[![make.fun bounty](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/lolipo8988-bot/kreutzx-ooo/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/lolipo8988-bot/kreutzx-ooo/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

A one-line entry for the make.fun **The Funniest Out-of-Office** competition:
a single out-of-office auto-reply of at most 140 characters, judged
head-to-head on which line lands hardest.

## The line

> I'm out of office until Monday. This auto-reply is now the most senior person here, and its first ruling is that your emergency can wait.

137 characters. It opens as a completely plausible auto-reply a real person
would set, then turns: the auto-reply itself has been promoted to the most
senior person available, and it uses its new authority for exactly one
decision — the sender's emergency can wait. The joke is the program's own
voice, nothing in it is a recycled inbox template, and no word can be cut
without losing either the setup or the punchline.

## How it works

`main.py` (Python 3, standard library only) assembles the line from its
setup and punchline, checks it against the gate (one line, non-blank,
at most 140 characters), and writes it to `/output/entry.txt` as UTF-8
with no trailing newline. It is deterministic: every run writes exactly
the same bytes.

## License

MIT — see `LICENSE`.
