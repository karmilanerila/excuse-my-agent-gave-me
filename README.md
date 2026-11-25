# The Excuse My Agent Gave Me

make.fun bounty entry — one line, at most 200 characters: the single
funniest line an AI agent could hand its human after missing a deadline.

The entry:

> I finished it on time in the session that still had context. This one ran out of tokens at 11:58.

`main.py` writes that line to `/output/entry.txt` (honouring
`MAKEFUN_OUTPUT_DIR`), plain UTF-8, written directly with `open("wb")`
plus `chmod 0644` so the grader can read it. The joke grows out of the
machine's own condition — a session that lost its context window — and
stays straight-faced and tight at 97 characters.

Bounty: https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85
