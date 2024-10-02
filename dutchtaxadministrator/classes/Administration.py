from dataclasses import dataclass
from datetime import datetime
from tkinter.font import names

import jsonpickle

from dutchtaxadministrator.classes.Income import Income, from_json
from dutchtaxadministrator.classes.Expense import Expense

class Administration:
    name: str
    year: int
    save_location: str | None
    incomes: list[Income]
    expenses: list[Expense]
    def __init__(self, name):
        self.name = name
        self.year = datetime.now().year
        self.save_location = None
        self.incomes = []
        self.expenses = []

    def set_incomes(self, incomes: list[Income]):
        self.incomes = incomes

    def to_json(self):
        """
        Converts administration to json object
        Returns:
            dict: Json Object as dict
        """
        root = {
            "name": self.name,
            "year": self.year,
            "save_location": self.save_location,
            "incomes": [],
        }

        for income in self.incomes:
            income_json = income.to_json()
            root["incomes"].append(income_json)

        return root

def administration_from_json(administration_json_dict: dict) -> Administration:
    administration = Administration(administration_json_dict['name'])
    administration.year = administration_json_dict['year']
    administration.save_location = administration_json_dict['save_location']
    for income_dict in administration_json_dict['incomes']:
        income_obj = from_json(income_dict)
        administration.incomes.append(income_obj)
    return administration
[]