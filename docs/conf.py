import os
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent

project = "Coffee Atlas"
author = "Coffee Atlas contributors"
copyright = "Public domain (CC0). Free to use and share."

extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

html_baseurl = "https://sthudir.github.io/demo-web-reference/"
html_theme = "furo"
html_title = "Coffee Atlas"
html_theme_options = {
    "announcement": (
        '<div class="dw-topbar">'
        '<a class="dw-hub-btn" href="https://sthudir.github.io/demo-web-hub/">&larr; Back to Hub</a>'
        '<a class="dw-gh" href="https://github.com/sthudiR/demo-web-reference" target="_blank" rel="noopener noreferrer"'
        ' aria-label="View source on GitHub" title="View source on GitHub">'
        '<svg viewBox="0 0 16 16" width="24" height="24" aria-hidden="true" fill="currentColor">'
        '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/>'
        '</svg></a></div>'
    ),
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_extra_path = ["_extra"]  # site.json + thumbnail.svg land at the output root
exclude_patterns = ["_build", "_api_*.rst", "xml", "Thumbs.db", ".DS_Store"]

# --- Optional C++ API docs (Doxygen + Breathe) -------------------------------
# Doxygen is run if installed; Breathe is enabled only when its XML exists, so
# the build also succeeds on machines without Doxygen.
xml_dir = HERE / "xml"
if shutil.which("doxygen") and not (xml_dir / "index.xml").exists():
    subprocess.run(["doxygen", "Doxyfile"], cwd=HERE, check=False)

if (xml_dir / "index.xml").exists():
    extensions.append("breathe")
    breathe_projects = {"coffee": str(xml_dir)}
    breathe_default_project = "coffee"
    api_body = (
        ".. doxygenenum:: coffee::Method\n\n"
        ".. doxygenstruct:: coffee::Recipe\n   :members:\n\n"
        ".. doxygenfunction:: coffee::water_for\n\n"
        ".. doxygenfunction:: coffee::strength_tds\n"
    )
else:
    api_body = (
        ".. note::\n\n"
        "   Doxygen was not found when this page was built, so the generated API\n"
        "   listing is omitted. Install ``doxygen`` and rebuild to see it.\n"
    )
(HERE / "_api_body.rst").write_text(api_body)
