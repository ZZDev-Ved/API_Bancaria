from pydantic import BaseModel

class ContaBase(BaseModel):
    nome: str
    saldo: float

class ContaCreate(ContaBase):
    pass

class Conta(ContaBase):
    id: int

    class Config:
        orm_mode = True
