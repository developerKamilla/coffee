from PyQt6.QtWidgets import QApplication, QMainWindow
from window import Window
import sys

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
