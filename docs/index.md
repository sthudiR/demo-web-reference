# Coffee Atlas

A friendly reference to where coffee comes from, how people brew it, and the numbers that make a good cup.

> **Try this:** press `/` and search for "espresso" to jump straight to it.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Origins
:link: origins
:link-type: doc
Regions that grow the world's coffee.
:::
:::{grid-item-card} Brew methods
:link: methods
:link-type: doc
Espresso, pour-over, immersion and cold brew.
:::
:::{grid-item-card} Brewing ratios
:link: ratios
:link-type: doc
How much water for how much coffee.
:::
:::{grid-item-card} Glossary
:link: glossary
:link-type: doc
Plain-language definitions.
:::
::::

::::{dropdown} Behind this page
| | |
|---|---|
| **Built with** | Sphinx with the Furo theme; Doxygen and Breathe for the C++ API pages |
| **The numbers** | 42 KB to load · ready in about 0.2 s · builds in 32 s · 190 lines of source · you write Markdown |
| **Good for** | Reference docs and API lookup, for Python, C++ and other languages |
| **Not for** | Interactive demos |
| **More** | [Source on GitHub](https://github.com/sthudiR/demo-web-reference) · [Pick your tool](https://sthudir.github.io/demo-web-hub/which/) · [Back to hub](https://sthudir.github.io/demo-web-hub/) |

Ready time: median of 5 cold loads on one home connection, 23 Oct 2026. Size is what a first visit downloads. Build time is the median of the last 5 GitHub Actions builds and includes installing the tools.
::::

```{toctree}
:hidden:
:maxdepth: 2

origins
methods
ratios
glossary
api
```
