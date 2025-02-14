from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class ContaBancaria(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    saldo = Column(Float, default=0.0)
