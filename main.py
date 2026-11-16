import sys
import os
from cce.gui.app import run_app

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    if "--smoke-test" in sys.argv:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
        from PyQt6.QtWidgets import QApplication
        from cce.gui.app import MainWindow, get_resource_path
        app = QApplication([])
        window = MainWindow()
        assert window.stack.count() == 2
        for filename in ("chronix_logo.png", "chronix_breit.png", "icon.ico"):
            if not os.path.isfile(get_resource_path(os.path.join("assets", filename))):
                raise FileNotFoundError(filename)
        window.close()
    else:
        run_app()
