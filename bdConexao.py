from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# --- Configurações ---
usuario = "postgres"
senha = "sua_senha"
host = "localhost"
porta = "5432"
banco = "CursoTeologia"

# --- Funções utilitárias ---
def conectar_postgres(usuario, senha, host, porta, banco):
    url = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    return engine, Session()

def executar_consulta(session, query, formato="dict"):
    result = session.execute(text(query))
    if formato == "dict":
        colunas = result.keys()
        return [dict(zip(colunas, row)) for row in result.fetchall()]
    elif formato == "list":
        return [tuple(row) for row in result.fetchall()]

def imprimir_resultados(titulo, dados):
    print(f"\n🔹 {titulo}")
    for i, row in enumerate(dados, 1):
        print(f"{i}. {row}")

# --- Consultas SQL ---
query_inner = """
SELECT a.nome_completo AS aluno, t.nome_turma AS turma, i.data_inscricao
FROM academico.inscricao i
INNER JOIN academico.aluno a ON i.xid_aluno = a.id_aluno
INNER JOIN academico.turma t ON i.xid_turma = t.id_turma;
"""

query_left = """
SELECT p.nome AS professor, t.nome_turma AS turma
FROM academico.professor p
LEFT JOIN academico.turma t ON p.id_professor = t.id_professor;
"""

query_right = """
SELECT t.nome_turma AS turma, p.nome AS professor, p.especialidade
FROM academico.professor p
RIGHT JOIN academico.turma t ON p.id_professor = t.id_professor;
"""

consultas = {
    "INNER JOIN": query_inner,
    "LEFT JOIN": query_left,
    "RIGHT JOIN": query_right
}

# --- Execução principal ---
engine, session = conectar_postgres(usuario, senha, host, porta, banco)

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Conexão bem-sucedida com o banco de dados.")

    # Dicionários
    for nome, sql in consultas.items():
        resultados = executar_consulta(session, sql, formato="dict")
        imprimir_resultados(f"{nome} (Dicionários)", resultados)

    # Listas
    for nome, sql in consultas.items():
        resultados = executar_consulta(session, sql, formato="list")
        imprimir_resultados(f"{nome} (Listas)", resultados)

finally:
    session.close()
    print("\n🔒 Sessão encerrada com sucesso.")
