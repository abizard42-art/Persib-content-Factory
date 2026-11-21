# Automatic Persib News Monitor

- Runs automatically every day at **08:00 and 18:00 WIB**.
- Can also be started manually from GitHub Actions.
- Saves reports directly in `research/daily/`; no downloadable Actions artifact is created.
- Open `research/daily/latest.md` for the newest digest.

## Important limitations
This first version uses Google News RSS as a free discovery index. It collects article titles, publisher labels, dates, links, and snippets. It does **not** independently verify claims, determine player fitness, or decide a lineup. Open the original source before treating a claim as fact. The next development step is a source verification and editorial briefing layer.

The workflow does not generate video or publish anything. Editorial approval remains mandatory.
