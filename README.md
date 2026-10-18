# demo-web-reference (Coffee Atlas)

A structured coffee reference built with Sphinx, Furo, MyST, sphinx-design, and optional C++ API docs via Doxygen + Breathe.

## Run locally
    python3 -m venv .venv && . .venv/bin/activate
    pip install -r requirements.txt
    sphinx-build -W --keep-going -b html docs docs/_build/html
    python3 -m http.server -d docs/_build/html

## Doxygen / Breathe
`docs/conf.py` runs `doxygen` if installed and enables Breathe only when `docs/xml/index.xml` exists. Without Doxygen the build still succeeds and the API page shows a note. CI installs doxygen with apt.

## Deploy
GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys to Pages on push to main. Optional secret `HUB_DISPATCH_TOKEN` notifies `sthudiR/demo-web-hub`.

## Video
Embed with a raw HTML block (see `docs/index.md`): a `youtube-nocookie.com` iframe in a `.video-wrap` 16:9 container with `loading="lazy"`.

## Base path
Served at `/demo-web-reference/`. Sphinx emits relative links, and `html_baseurl` is `https://sthudir.github.io/demo-web-reference/`. `site.json` and `thumbnail.svg` come from `docs/_extra` via `html_extra_path`.

## Licence
Public domain (CC0). Everything here is made up for a demo; use and share it freely. See `LICENSE`.
