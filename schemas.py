from pydantic import BaseModel

# Schema para criação e atualização de notas
class NotaBase(BaseModel):
    titulo: str
    conteudo: str

# Schema para leitura (inclui o ID da nota)
class NotaResponse(NotaBase):
    id: int

    class Config:
        orm_mode = True
