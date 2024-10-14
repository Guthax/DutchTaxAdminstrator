from PyQt6.QtWidgets import QTableWidgetItem


def show_as_euro(value) -> QTableWidgetItem:
    return QTableWidgetItem(f"€ {value}")