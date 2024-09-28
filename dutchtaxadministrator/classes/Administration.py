from dataclasses import dataclass
from datetime import datetime

from dutchtaxadministrator.classes import Income, Expense


class Administration:
    name: str
    year: int
    date_started: datetime
    save_location: str
    incomes: list[Income]
    expenses: list[Expense]
