from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Função de "IA" leve (regra simples) — gera sugestão de estudo a partir do tema
def sugestao_de_estudo(tema: str) -> str:
    tema = (tema or "").strip().lower()
    if not tema:
        return "Informe o tema da aula para gerar uma sugestão."
    if "algoritmo" in tema or "estrutura" in tema:
        return "Sugestão: reveja pseudocódigo e implemente um exercício prático (30 min). Faça testes e identifique casos de borda."
    if "rede" in tema or "tcp" in tema or "dhcp" in tema:
        return "Sugestão: monte um diagrama da topologia, atribua IPs e simule pacotes (Wireshark/VM)."
    return f"Sugestão rápida para '{tema}': resuma o conteúdo em 5 bullets e crie 1 exercício prático."
