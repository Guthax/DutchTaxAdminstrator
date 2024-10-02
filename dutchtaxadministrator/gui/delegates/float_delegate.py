from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QItemDelegate, QLineEdit


class FloatDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        """
        Creates a QLineEdit widget for editing float values with specific validation rules.

        Parameters:
        parent : QWidget
            The parent widget of the QLineEdit.
        option : QStyleOptionViewItem
            Provides style options for the item.
        index : QModelIndex
            The index of the item being edited.

        Returns:
        QLineEdit
            A QLineEdit widget with a QDoubleValidator set to standard float notation and precision of 2 decimal places.
        """
        # Create a QLineEdit for editing float values
        editor = QLineEdit(parent)

        # Set QDoubleValidator with proper range and precision
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)  # Allow standard float notation
        validator.setDecimals(2)  # Set precision to 2 decimal places (or adjust as needed)
        editor.setValidator(validator)
        return editor

    def setEditorData(self, editor, index):
        """

        Set the editor data based on the model's data.

        This method retrieves the data from the model using the given index and sets it into the editor. If the data is a float or integer, it formats the value to two decimal places before setting it as the editor's text. For other data types, it simply converts the value to a string and sets it as the editor's text.

        Parameters:
        editor (QWidget): The editor widget that will display the data.
        index (QModelIndex): The index of the item in the model.
        """
        # Get the value from the model and set it to the editor
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if isinstance(value, (float, int)):
            # Set the text of the editor to a float string with precision
            editor.setText(f"{value:.2f}")
        else:
            # Handle invalid or non-float values
            editor.setText(str(value))

    def setModelData(self, editor, model, index):
        """
        Get the value from the editor and set it to the model.

        Parameters:
        - editor: The editor widget from which the value is fetched.
        - model: The model where the data needs to be set.
        - index: The index in the model where the data needs to be set.

        The value is fetched from the editor, attempting to convert it to a float.
        If the conversion is successful, the float value is set in the model.
        If conversion fails, the original string value is set as a fallback.
        """
        # Get the value from the editor and set it to the model
        text_value = editor.text().replace(',', '.')
        try:
            float_value = float(text_value)
            # Set the data in the model as a float
            model.setData(index, float_value, Qt.ItemDataRole.EditRole)
        except ValueError:
            # If conversion fails, still set the string value (fallback)
            model.setData(index, text_value, Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        """

        Updates the geometry of the editor widget.

        This method sets the geometry of the given editor to match the geometry specified in the option's rectangle.

        Parameters:
            editor (QWidget): The editor widget whose geometry is to be updated.
            option (QStyleOptionViewItem): Contains parameters for drawing the item.
            index (QModelIndex): The index of the item being edited.
        """
        editor.setGeometry(option.rect)
