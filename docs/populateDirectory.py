import json
from pathlib import Path

with (Path(__file__).parent.parent / "plugins.json").open("r", encoding="UTF-8") as f:
    pluginsList = json.load(f)

code = (
    "PsychoPy Plugins Directory\n"
    "=====================================\n"
    "\n"
    "The following plugins are currently available:\n"
    "\n"
)
for plugin in pluginsList:
    line = "- `%(name)s <%(homepage)s>`_ [``%(pipname)s``]: %(description)s\n" % plugin
    code += line

with (Path(__file__).parent / "directory.rst").open("w", encoding="UTF-8") as f:
    f.write(code)

