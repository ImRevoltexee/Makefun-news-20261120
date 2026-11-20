[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ImRevoltexee/Makefun-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/ImRevoltexee/Makefun-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

# 20 November 2026 — The World in One Day

Entry for the [make.fun](https://make.fun) bounty
[news-image-20261120](https://make.fun/bounty/news-image-20261120):
one image summing up the world's news of Friday 20 November 2026.

## The image

A newspaper-style infographic (1024×1024, drawn with code, no AI image
generator): a masthead naming the day, six stories, and an "ALSO TODAY"
strip.

- **Europe** — Britain and the EU agree a Brexit reset: food trade eased,
  100,000 youth visas a year; divisions remain.
- **Ukraine** — Russia strikes Kyiv overnight: ballistic missiles spark
  fires in several districts of the capital.
- **Trade** — APEC publishes the Shenzhen Outlook: 21 economies back open
  trade, data rules and AI safeguards.
- **Economy** — Japan's inflation cements rate-hike bets: core CPI up 2.2%
  in October; the Bank of Japan is seen hiking in December.
- **Haiti** — Haiti police kill 34 in a gang raid: the Martissant corridor
  is retaken in the first big push in five years.
- **Americas** — Bukele seeks a third term: El Salvador's president
  registers for the February vote critics call unchecked.

Also today: Fiona, the internet-famous hippo, dies at 9 in Cincinnati
after swallowing a visitor's hat; the White House fires its national
cyber director after a wave of tech outages; California warns of king
tides and heavy rain over Nov 24–26.

Sources: Reuters, The Times, Kyiv Independent, MLex, Aju Press, WSJ, AP,
Inshorts.

## How it works

- `draw.py` — draws `entry.png` from scratch with Pillow (deterministic:
  no network, no randomness, no timestamps). Run it to regenerate the image:
  `python3 draw.py`
- `main.py` — the entry point (Python 3.13, standard library only). It
  copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`)
  and validates the file first (PNG or JPEG, at most 1 MiB, at most
  1024×1024, copied bytes hash-checked).

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
