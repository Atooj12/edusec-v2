# PIM - API Acadêmica (FastAPI + SQLAlchemy)

## Como rodar (local)
1. Criar venv: `python -m venv .venv && source .venv/bin/activate`
2. Instalar: `pip install -r requirements.txt`
3. Rodar: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
4. Swagger UI: `http://127.0.0.1:8000/docs`

## Testes via terminal (exemplos)
Criar aluno:
curl -X POST "http://127.0.0.1:8000/alunos/" -H "Content-Type: application/json" -d '{"nome":"Ana","email":"ana@ex.com","curso":"ADS"}'

Pedir sugestão IA:
curl "http://127.0.0.1:8000/ai/sugestao?tema=redes"

## Observações
- Banco: SQLite `pim.db`
- Arquitetura: FastAPI (API REST) + SQLAlchemy (ORM)
- Para demonstração multiusuário: abrir duas abas do terminal ou executar em duas VMs e disparar requests simultâneos.
