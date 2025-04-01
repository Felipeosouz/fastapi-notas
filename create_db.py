from database import engine, Base

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

print("Banco de dados criado com sucesso!")
