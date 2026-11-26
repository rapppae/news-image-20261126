# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/rapppae/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/rapppae/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A one-image summary of the world's news of Thursday 26 November 2026, pre-rendered by the Python renderer in `draw.py`: the US proposes tariffs on 14 trading partners, Houthi strikes hit Saudi ports and the Ras Tanura refinery, a fuel tanker fire near Cairo kills at least 31, the first Pakistani astronaut reaches China's Tiangong station, Ukraine says it hit five Russian jets at Savasleyka airbase, and the FCC clears SpaceX's plan for up to a million orbital data-centre satellites — plus a ticker with the postponed Macy's parade, the Nasdaq AI sell-off and Liverpool's 3–0 win.

## Run it

```sh
python3 draw.py          # re-render entry.png (needs Pillow + DejaVu fonts)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under 1 MiB). The entrypoint is standard library only, so it runs in the grader's sandbox: it copies the pre-rendered `entry.png` to the output and sanity-checks it (PNG signature, 1024×1024, under 1 MiB).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
