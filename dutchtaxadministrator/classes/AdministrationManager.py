import json
import os

from PyQt6.QtCore import pyqtSignal, QObject

from dutchtaxadministrator.classes.Administration import Administration, administration_from_json
from dutchtaxadministrator.classes.Expense import Expense
from dutchtaxadministrator.classes.Income import Income


class AdministrationManager(QObject):
    administration_changed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.administration = Administration("Template")

    def set_administration(self, administration):
        """
        Sets the administration property of the object and emits a signal indicating that the administration has changed.

        Parameters:
        administration - The new administration value to be set
        """
        self.administration = administration
        self.administration_changed.emit()

    def update_administration_incomes(self, incomes: list[Income]):
        """
        Updates the administration incomes with the provided list of Income objects.

        Parameters:
            incomes (list[Income]): A list of Income objects to update the administration's incomes.

        Actions:
            1. Sets the administration's incomes with the provided list.
            2. Emits the administration_changed signal to notify that the administration's incomes have been updated.
        """
        self.administration.set_incomes(incomes)
        self.administration_changed.emit()

    def update_administration_expenses(self, expenses: list[Expense]):
        """
        Updates the administration expenses with the provided list of Expense objects.

        Parameters:
            expenses (list[Expense]): A list of Expense objects to update the administration's expenses.

        Actions:
            1. Sets the administration's expense with the provided list.
            2. Emits the administration_changed signal to notify that the administration's expense have been updated.
        """
        self.administration.set_expenses(expenses)
        self.administration_changed.emit()

    def new_administration(self, name: str, year: int, save_location: str):
        """
        Sets up a new administration with the provided name and year,
        and saves it to the specified location. If the location does
        not exist, it will be created. Emits an administration_changed
        signal after setting up the new administration.

        Args:
            name (str): The name of the new administration.
            year (int): The year of the new administration.
            save_location (str): The directory path where the administration will be saved.

        Raises:
            OSError: If the directory cannot be created.
        """
        self.administration = Administration(name)
        self.administration.year = year
        self.administration.save_location = save_location
        if not os.path.exists(self.administration.save_location):
            os.mkdir(self.administration.save_location)
        self.administration_changed.emit()


    def load_administration_from_json(self, json_dict: dict):
        """
        Loads administration data from a given JSON dictionary, updates the internal state, and emits a signal indicating the change.

        Args:
            json_dict (dict): A dictionary containing the administration data in JSON format.
        """
        self.administration = administration_from_json(json_dict)
        self.administration_changed.emit()

    def save_administration(self):
        """
        Opens save dialog if administration has no save file and saves administration as json
        """
        folder = self.administration.save_location
        data_json_loc = f"{folder}/{self.administration.name}_data.json"

        try:
            with open(data_json_loc, 'w') as json_file:
                json_to_save = self.administration.to_json()
                json.dump(json_to_save, json_file, indent=4)

        except Exception as e:
            print(f"Error saving file: {e}")