"""Check GUI construction without running an interactive event loop."""
import os
import sys
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PyQt6.QtWidgets import QApplication
from cce.gui.app import MainWindow, get_resource_path

app = QApplication([])
window = MainWindow()
assert window.windowTitle() == "Chronix"
assert window.stack.count() == 2
for name in ("chronix_logo.png", "chronix_breit.png", "icon.ico"):
    assert Path(get_resource_path(f"assets/{name}")).is_file(), name
window.close()
print("Chronix GUI and bundled source assets: OK")
