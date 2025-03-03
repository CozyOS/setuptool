# ======================
# |  CozyOS SetupTool  |
# |  (C) 2025 CozyOS   |
# |   Python powered   |
# ======================


# Python modules (pip)

import typer
import numpy
import fs

# Local Modules

from lib.git import gitcloner
from lib.targetScript import TargetDevice

app = typer.Typer()

@app.command()
def configure():
    # configuration menu
    pass


