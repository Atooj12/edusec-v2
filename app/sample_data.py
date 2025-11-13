from sqlalchemy.orm import Session
from . import crud, schemas, models

def load_sample(db: Session):
    # Verifica se já há usuários
    if db.query(models.Usuario).count() == 0:
        admin = schemas.UsuarioCreate(username="prof01", password="senhaprof", role="professor")
        aluno_user = schemas.UsuarioCreate(username="aluno1", password="senhaaluno", role="aluno")
        crud.create_usuario(db, admin)
        crud.create_usuario(db, aluno_user)

    # Verifica se já há alunos
    if db.query(models.Aluno).count() == 0:
        crud.create_aluno(db, schemas.AlunoCreate(nome="João Silva", email="joao@example.com", curso="ADS")) # type: ignore

    # Verifica se já há turmas
    if db.query(models.Turma).count() == 0:
        crud.create_turma(db, schemas.TurmaCreate(nome="ADS-2025-2", semestre="2025/2"))
