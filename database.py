import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/banking_db"

# Configuração assíncrona
database = databases.Database(DATABASE_URL)
metadata = MetaData()

# Define a base de modelos
Base = declarative_base(metadata=metadata)

# Criando o engine assíncrono
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Session local assíncrona
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
