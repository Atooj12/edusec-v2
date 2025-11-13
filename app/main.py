from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, crud, schemas, utils
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PIM - Sistema Acadêmico API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    database.init_db()
    # carregar dados de exemplo se necessário
    db = database.SessionLocal()
    from . import sample_data
    sample_data.load_sample(db)
    db.close()

# Usuarios
@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def criar_usuario(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existing = crud.get_usuario(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username já existe.")
    u = crud.create_usuario(db, user)
    return u

# Alunos
@app.post("/alunos/", response_model=schemas.AlunoOut)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return crud.create_aluno(db, aluno)

@app.get("/alunos/", response_model=list[schemas.AlunoOut])
def listar_alunos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_alunos(db, skip, limit)

# Turmas
@app.post("/turmas/", response_model=schemas.TurmaOut)
def criar_turma(turma: schemas.TurmaCreate, db: Session = Depends(get_db)):
    return crud.create_turma(db, turma)

# Aulas
@app.post("/aulas/", response_model=schemas.AulaOut)
def criar_aula(aula: schemas.AulaCreate, db: Session = Depends(get_db)):
    return crud.create_aula(db, aula)

# Atividades
@app.post("/atividades/", response_model=schemas.AtividadeOut)
def criar_atividade(atividade: schemas.AtividadeCreate, db: Session = Depends(get_db)):
    return crud.create_atividade(db, atividade)

@app.get("/atividades/", response_model=list[schemas.AtividadeOut])
def listar_atividades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_atividades(db, skip, limit)

# Endpoint de "IA" (simples)
@app.get("/ai/sugestao")
def ai_sugestao(tema: str = "", db: Session = Depends(get_db)):
    return {"sugestao": utils.sugestao_de_estudo(tema)}
