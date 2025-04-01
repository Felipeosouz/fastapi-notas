from sqlalchemy.orm import Session
import models, schemas

# Criar uma nova nota
def criar_nota(db: Session, nota: schemas.NotaBase):
    nova_nota = models.Nota(**nota.dict())
    db.add(nova_nota)
    db.commit()
    db.refresh(nova_nota)
    return nova_nota

# Listar todas as notas
def listar_notas(db: Session):
    return db.query(models.Nota).all()

# Buscar uma nota por ID
def buscar_nota(db: Session, nota_id: int):
    return db.query(models.Nota).filter(models.Nota.id == nota_id).first()

# Atualizar uma nota
def atualizar_nota(db: Session, nota_id: int, nota: schemas.NotaBase):
    nota_db = buscar_nota(db, nota_id)
    if nota_db:
        nota_db.titulo = nota.titulo
        nota_db.conteudo = nota.conteudo
        db.commit()
        db.refresh(nota_db)
    return nota_db

# Deletar uma nota
def deletar_nota(db: Session, nota_id: int):
    nota_db = buscar_nota(db, nota_id)
    if nota_db:
        db.delete(nota_db)
        db.commit()
    return nota_db
