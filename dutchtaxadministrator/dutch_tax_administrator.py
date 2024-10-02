import sys
from PyQt6.QtWidgets import QApplication
from dutchtaxadministrator.gui.main_window import DutchTaxAdministrator


def main():
    application = QApplication(sys.argv)
    window = DutchTaxAdministrator()
    window.show()

    application.exec()

if __name__ == '__main__':
    main()
