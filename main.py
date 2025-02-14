from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database import database, engine, Base, async_session
from app import crud, schemas

app = FastAPI()

# Criando as tabelas no banco (se não existirem)
Base.metadata.create_all(bind=engine)

@app.post("/contas/", response_model=schemas.Conta)
async def criar_conta(conta: schemas.ContaCreate, db: AsyncSession = Depends(async_session)):
    return await crud.criar_conta(db=db, conta=conta)

@app.get("/contas/{conta_id}", response_model=schemas.Conta)
async def consultar_saldo(conta_id: int, db: AsyncSession = Depends(async_session)):
    conta = await crud.consultar_saldo(db=db, conta_id=conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta

@app.post("/transferir/")
async def transferir(
    conta_origem_id: int, conta_destino_id: int, valor: float, db: AsyncSession = Depends(async_session)
):
    conta_origem, conta_destino = await crud.transferir_fundos(db, conta_origem_id, conta_destino_id, valor)
    if not conta_origem or not conta_destino:
        raise HTTPException(status_code=400, detail="Erro na transferência")
    return {"status": "Transferência realizada com sucesso"}
