from PyQt6.QtWidgets import QStyledItemDelegate, QDateEdit, QApplication
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPainter

class DateDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(DateDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        # Create a QDateEdit widget as the editor
        editor = QDateEdit(parent)
        editor.setDisplayFormat("dd/MM/yyyy")
        editor.setCalendarPopup(True)  # Show the date picker popup
        return editor

    def setEditorData(self, editor, index):
        # Get the current text from the model and set it to the editor
        date_str = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        date = QDate.fromString(date_str, "dd/MM/yyyy")
        if date.isValid():
            editor.setDate(date)
        else:
            editor.setDate(QDate.currentDate())

    def setModelData(self, editor, model, index):
        # When editing is finished, set the selected date to the model
        date = editor.date()
        model.setData(index, date.toString("dd/MM/yyyy"), Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        # Ensure the editor widget has the same geometry as the item it is editing
        editor.setGeometry(option.rect)

    def displayText(self, value, locale):
        # Customize how the date is displayed in the view
        date = QDate.fromString(value, "dd/MM/yyyy")
        if date.isValid():
            return date.toString("dd/MM/yyyy")
        else:
            return ""