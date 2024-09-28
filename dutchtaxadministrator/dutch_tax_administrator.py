import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QFileDialog,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget)

from dutchtaxadministrator.gui.main_window import DutchTaxAdministrator


def main():
    print("test")
    application = QApplication(sys.argv)
    window = DutchTaxAdministrator()
    window.show()

    application.exec()

if __name__ == '__main__':
    main()
