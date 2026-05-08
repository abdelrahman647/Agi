import sys
from PySide6.QtWidgets import QApplication
from gui.dashboard import TaherGUI

def main():
    app = QApplication(sys.argv)
    window = TaherGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
