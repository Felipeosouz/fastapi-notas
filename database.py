from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco de dados SQLite
DATABASE_URL = "sqlite:///./notas.db"

# Criando o engine do banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criando a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos do banco
Base = declarative_base()
