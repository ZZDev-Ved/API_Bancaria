from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import ContaBancaria
from app.schemas import ContaCreate

# Criando uma nova conta
async def criar_conta(db: AsyncSession, conta: ContaCreate):
    db_conta = ContaBancaria(nome=conta.nome, saldo=conta.saldo)
    db.add(db_conta)
    await db.commit()
    await db.refresh(db_conta)
    return db_conta

# Consultar saldo
async def consultar_saldo(db: AsyncSession, conta_id: int):
    query = select(ContaBancaria).filter(ContaBancaria.id == conta_id)
    result = await db.execute(query)
    conta = result.scalar_one_or_none()
    return conta

# Transferência de valores
async def transferir_fundos(db: AsyncSession, conta_origem_id: int, conta_destino_id: int, valor: float):
    conta_origem = await consultar_saldo(db, conta_origem_id)
    conta_destino = await consultar_saldo(db, conta_destino_id)

    if not conta_origem or not conta_destino:
        return None  # Ou lançar uma exceção, dependendo da lógica de negócio

    if conta_origem.saldo < valor:
        return None  # Ou lançar exceção de saldo insuficiente

    conta_origem.saldo -= valor
    conta_destino.saldo += valor

    await db.commit()
    return conta_origem, conta_destino
