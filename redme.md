

## 🇧🇷 README.md — Projeto Python + PostgreSQL com SQLAlchemy

```markdown
# 📚 Projeto: Integração Python + PostgreSQL com SQLAlchemy

Este projeto demonstra como conectar uma aplicação Python a um banco de dados PostgreSQL utilizando SQLAlchemy, executar consultas SQL com diferentes tipos de JOINs e retornar os resultados em dois formatos: dicionários e listas.

---

## 🚀 Funcionalidades

- Conexão segura com banco PostgreSQL via SQLAlchemy
- Execução de três tipos de JOIN:
  - `INNER JOIN`: Alunos e turmas
  - `LEFT JOIN`: Professores e suas turmas (mesmo sem turma)
  - `RIGHT JOIN`: Turmas e seus professores (mesmo sem professor)
- Retorno dos dados como:
  - ✅ Dicionários (`dict`)
  - ✅ Listas de tuplas (`list`)
- Impressão formatada dos resultados no terminal

---

## 🧱 Estrutura do Projeto

```
TP3-banco-dados-python-projeto-bloco/
│
├── bdConexao.py         # Script principal com conexão, consultas e impressão
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências do projeto (opcional)
```

---

## 🛠️ Requisitos

- Python 3.8+
- PostgreSQL instalado e rodando localmente
- Banco de dados `CursoTeologia` com as tabelas e dados populados
- Bibliotecas Python:
  - `sqlalchemy`
  - `psycopg2-binary`

Instale as dependências com:

```bash
pip install sqlalchemy psycopg2-binary
```

---

## ⚙️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd TP3-banco-dados-python-projeto-bloco
   ```

2. Edite o arquivo `bdConexao.py` com suas credenciais de acesso ao PostgreSQL:
   ```python
   usuario = "postgres"
   senha = "sua_senha"
   host = "localhost"
   porta = "5432"
   banco = "CursoTeologia"
   ```

3. Execute o script:
   ```bash
   python bdConexao.py
   ```

---

## 📌 Autor

Desenvolvido por **Weslley Soares** como parte do projeto de bloco de Banco de Dados.

---

## 🇺🇸 README.md — Python + PostgreSQL Integration with SQLAlchemy

```markdown
# 📚 Project: Python + PostgreSQL Integration with SQLAlchemy

This project demonstrates how to connect a Python application to a PostgreSQL database using SQLAlchemy, run SQL queries with different types of JOINs, and return results in two formats: dictionaries and lists.

---

## 🚀 Features

- Secure PostgreSQL connection via SQLAlchemy
- Execution of three JOIN types:
  - `INNER JOIN`: Students and classes
  - `LEFT JOIN`: Professors and their classes (even without one)
  - `RIGHT JOIN`: Classes and their professors (even without one)
- Data returned as:
  - ✅ Dictionaries (`dict`)
  - ✅ Tuple lists (`list`)
- Formatted output in the terminal

---

## 🧱 Project Structure

```
TP3-banco-dados-python-projeto-bloco/
│
├── bdConexao.py         # Main script with connection, queries, and output
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies (optional)
```

---

## 🛠️ Requirements

- Python 3.8+
- PostgreSQL installed and running locally
- Database `CursoTeologia` with populated tables
- Python libraries:
  - `sqlalchemy`
  - `psycopg2-binary`

Install dependencies with:

```bash
pip install sqlalchemy psycopg2-binary
```

---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd TP3-banco-dados-python-projeto-bloco
   ```

2. Edit `bdConexao.py` with your PostgreSQL credentials:
   ```python
   usuario = "postgres"
   senha = "your_password"
   host = "localhost"
   porta = "5432"
   banco = "CursoTeologia"
   ```

3. Run the script:
   ```bash
   python bdConexao.py
   ```

---

## 📌 Author

Developed by **Weslley Soares** as part of a database course project.

---
