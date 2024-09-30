from typing import List

from dutchtaxadministrator.classes.Income import Income


class IncomeList(List):
    incomes: list[Income]

    def to_json(self):
        for income in self.incomes:
            income_json = income.to_json()

