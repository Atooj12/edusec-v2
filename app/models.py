from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="aluno")  # aluno | professor | admin

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    curso = Column(String, default="ADS")
    atividades = relationship("Atividade", back_populates="aluno")

class Turma(Base):
    __tablename__ = "turmas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    semestre = Column(String)
    aulas = relationship("Aula", back_populates="turma")

class Aula(Base):
    __tablename__ = "aulas"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    tema = Column(String)
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    turma = relationship("Turma", back_populates="aulas")

class Atividade(Base):
    __tablename__ = "atividades"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(Text)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    aluno = relationship("Aluno", back_populates="atividades")
