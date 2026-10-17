import os
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent

project = "Coffee Atlas"
author = "Coffee Atlas contributors"
copyright = "2026, Coffee Atlas contributors"

extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

html_baseurl = "https://sthudir.github.io/demo-web-reference/"
html_theme = "furo"
html_title = "Coffee Atlas"
html_theme_options = {
    "announcement": '<a href="https://sthudir.github.io/demo-web-hub/">&larr; All sites</a>',
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
