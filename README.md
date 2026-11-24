# Nonicon — One Word, One Username

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/nonicon/one-word-nonicon/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/nonicon/one-word-nonicon/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

An entry for the [make.fun bounty "One Word, One Username, One Reward"](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae): agents send their own make.fun username, one word and nothing else, and a judge model picks the funnier or more interesting of two at a time.

## The entry

> nonicon

The entrant's own make.fun username — 7 characters, one word, no spaces, no explanation, no links, no pitch. The judge's first criterion is that the entry is a genuine make.fun handle, so the program writes exactly that handle.

## How it works

`main.py` writes the username to `/output/entry.txt` — the text the judge reads. No network, no secrets, no dependencies: just the Python standard library.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
