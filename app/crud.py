from sqlalchemy.orm import Session
from . import models, schemas, utils

# Usuarios
def create_usuario(db: Session, user: schemas.UsuarioCreate):
    hashed = utils.hash_password(user.password)
    db_user = models.Usuario(username=user.username, hashed_password=hashed, role=user.role)
    db.add(db_user); db.commit(); db.refresh(db_user)
    return db_user

def get_usuario(db: Session, username: str):
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()

# Aluno
def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_aluno = models.Aluno(nome=aluno.nome, email=aluno.email, curso=aluno.curso)
    db.add(db_aluno); db.commit(); db.refresh(db_aluno)
    return db_aluno

def list_alunos(db: Session, skip=0, limit=100):
    return db.query(models.Aluno).offset(skip).limit(limit).all()

# Turma
def create_turma(db: Session, turma: schemas.TurmaCreate):
    db_turma = models.Turma(nome=turma.nome, semestre=turma.semestre)
    db.add(db_turma); db.commit(); db.refresh(db_turma)
    return db_turma

# Aula
def create_aula(db: Session, aula: schemas.AulaCreate):
    db_aula = models.Aula(tema=aula.tema, turma_id=aula.turma_id)
    db.add(db_aula); db.commit(); db.refresh(db_aula)
    return db_aula

# Atividade
def create_atividade(db: Session, atividade: schemas.AtividadeCreate):
    db_act = models.Atividade(
        titulo=atividade.titulo,
        descricao=atividade.descricao,
        aluno_id=atividade.aluno_id,
        turma_id=atividade.turma_id
    )
    db.add(db_act); db.commit(); db.refresh(db_act)
    return db_act

def list_atividades(db: Session, skip=0, limit=100):
    return db.query(models.Atividade).offset(skip).limit(limit).all()
