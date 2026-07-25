# GitHub AI Trend Radar Dashboard

Static GitHub Pages dashboard built from `outputs/github-radar/daily/*/repos.json`.

```bash
npm install
npm run build
npm run dev
```

`npm run build` regenerates browser data from the daily snapshots before building `dist/`. Publish `dist/` to GitHub Pages. The dashboard deliberately excludes live GitHub Trending observations from its star-delta time series.

## Daily automation handoff

After the daily radar report verifies `analysis.md`, `repos.json`, `report.md`, and its snapshot, run:

```bash
rtk --ultra-compact npm run build
```

The daily automation stages only that date's output folder and `dashboard/`, using `git add -f` for the ignored radar snapshots, then creates a bilingual Git commit. It pushes only when the current branch has an upstream remote, so an unconfigured remote does not turn a successful radar run into a failed one.
