from dataclasses import dataclass
from datetime import datetime
from tkinter.font import names

import jsonpickle

from dutchtaxadministrator.classes.Income import Income
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
        income = Income()
        self.incomes.append(income)

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



