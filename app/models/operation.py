import re
from datetime import datetime

from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.fields import Field

from app.models.operation_amount import OperationAmount


class Operation(BaseModel):
    id: int
    state: str
    date: datetime
    operationAmount: OperationAmount
    description: str
    from_: str | None = Field(alias='from')
    description: str
    to: str
    _encoded_date: str | None

    @staticmethod
    def _encode_data(value: str) -> str:
        data = value.split()
        number_card = data[-1]
        if value.startswith('Счет'):
            data[-1] = '**' + data[-1][-4:]
            return ' '.join(data)

        hidden_number = number_card[0:6] + '******' + number_card[-4:]
        result = ' '.join(re.findall('(.{%s}|.+$)' % 4, hidden_number))
        data[-1] = result
        return ' '.join(data)

    @validator('from_')
    def _encoded_from(cls, value):
        return cls._encode_data(value)

    @validator('to')
    def _encoded_to(cls, value):
        return cls._encode_data(value)

    @property
    def _encoded_date(self):
        return self.date.date().strftime("%d.%m.%Y")

    def get_info_for_operation(self):
        return f'{self._encoded_date} {self.description} {self.from_ if self.from_ else ""} -> {self.to}'
