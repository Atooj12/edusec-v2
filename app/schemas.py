from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "aluno"

class UsuarioOut(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    curso: Optional[str] = "ADS"

class AlunoOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    curso: str
    class Config:
        orm_mode = True

class TurmaCreate(BaseModel):
    nome: str
    semestre: str

class TurmaOut(BaseModel):
    id: int
    nome: str
    semestre: str
    class Config:
        orm_mode = True

class AulaCreate(BaseModel):
    tema: str
    turma_id: int

class AulaOut(BaseModel):
    id: int
    data: datetime
    tema: str
    turma_id: int
    class Config:
        orm_mode = True

class AtividadeCreate(BaseModel):
    titulo: str
    descricao: str
    aluno_id: int
    turma_id: int

class AtividadeOut(BaseModel):
    id: int
    titulo: str
    descricao: str
    aluno_id: int
    turma_id: int
    class Config:
        orm_mode = True
