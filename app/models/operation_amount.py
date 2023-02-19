from pydantic import BaseModel


class Currency(BaseModel):
    name: str
    code: str


class OperationAmount(BaseModel):
    amount: float
    currency: Currency
