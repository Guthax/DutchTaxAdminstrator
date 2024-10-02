from math import trunc

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QItemDelegate, QWidget, QVBoxLayout, QPushButton


class FileUploadDelegate(QItemDelegate):
    """
    class FileUploadDelegate(QItemDelegate):

    def createEditor(self, parent, option, index):
        """
    def createEditor(self, parent, option, index):
        """
        Creates an editor widget for use in a delegate-based view.

        Parameters:
        parent: The parent widget for the editor.
        option: The options for the item being edited.
        index: The model index indicating the item being edited.

        Returns:
        A QWidget instance configured with a vertical layout and a button.
        """
        # Create a QWidget as the editor
        editor = QWidget(parent)
        layout = QVBoxLayout(editor)
        button = QPushButton("Upload File")

        # Connect button signal to open the file dialog
        button.clicked.connect(lambda: self.open_file_dialog(button, index))
        layout.addWidget(button)
        editor.setLayout(layout)

        return editor

    def open_file_dialog(self, button, index):
        # Open the file dialog to select a file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(button, "Select File")

        if file_path:
            # Set the selected file path in the model
            index.model().setData(index, file_path, Qt.ItemDataRole.EditRole)
