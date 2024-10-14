from datetime import datetime


class Sale:
    invoice_id: str = ""
    date: datetime = datetime.now()
    name: str = ""
    description: str = ""
    _amount_ex_vat: float = 0
    _vat_percentage: float = 0
    amount_inc_vat: float = 0

    @property
    def amount_ex_vat(self):
        return self._amount_ex_vat

    @amount_ex_vat.setter
    def amount_ex_vat(self, value):
        self._amount_ex_vat = value
        self.amount_inc_vat = self._amount_ex_vat * (1 + (self._vat_percentage / 100))

    @property
    def vat_percentage(self):
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, value):
        self._vat_percentage = value
        self.amount_inc_vat = self._amount_ex_vat * (1 + (self._vat_percentage / 100))
