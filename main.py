from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Criar as tabelas no banco (caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar uma nova nota
@app.post("/notas/", response_model=schemas.NotaResponse)
def criar_nota(nota: schemas.NotaBase, db: Session = Depends(get_db)):
    return crud.criar_nota(db, nota)

# Listar todas as notas
@app.get("/notas/", response_model=list[schemas.NotaResponse])
def listar_notas(db: Session = Depends(get_db)):
    return crud.listar_notas(db)

# Buscar uma nota pelo ID
@app.get("/notas/{nota_id}", response_model=schemas.NotaResponse)
def buscar_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = crud.buscar_nota(db, nota_id)
    if nota is None:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota

# Atualizar uma nota
@app.put("/notas/{nota_id}", response_model=schemas.NotaResponse)
def atualizar_nota(nota_id: int, nota: schemas.NotaBase, db: Session = Depends(get_db)):
    nota_atualizada = crud.atualizar_nota(db, nota_id, nota)
    if nota_atualizada is None:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota_atualizada

# Deletar uma nota
@app.delete("/notas/{nota_id}")
def deletar_nota(nota_id: int, db: Session = Depends(get_db)):
    nota_excluida = crud.deletar_nota(db, nota_id)
    if nota_excluida is None:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return {"message": "Nota excluída com sucesso"}
