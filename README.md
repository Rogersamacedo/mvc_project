# 🎓 Sistema MVC — SENAI | Aula Teste Instrutor 3

Projeto de demonstração do padrão **MVC (Model-View-Controller)** usando:

- 🐍 **Python 3.12**
- 🗄️ **SQLite** como banco de dados
- 🌐 **Flask** como framework web (View)
- 🐳 **Docker** para o ambiente

---

## 📁 Estrutura do Projeto

```
mvc_project/
├── model/
│   └── conexao.py        ← Model: conexão e criação da tabela no SQLite
├── controller/
│   └── crud.py           ← Controller: operações CRUD (inserir, listar, alterar, excluir)
├── view/
│   ├── app.py            ← View: rotas Flask
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html    ← Tela principal com formulário e tabela
│   │   └── editar.html   ← Tela de edição
│   └── static/
│       └── style.css     ← Estilos da interface
├── main.py               ← Ponto de entrada da aplicação
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Como executar com Docker

### 1. Pré-requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado

### 2. Subir o ambiente
```bash
# Na pasta do projeto:
docker compose up --build
```

### 3. Acessar no navegador
```
http://localhost:5000
```

### 4. Parar o ambiente
```bash
docker compose down
```

---

## 🔧 Executar sem Docker (Python local)

```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar a aplicação
python main.py
```

---

## 🏗️ Arquitetura MVC

```
Usuário (navegador)
    ↕
  View  (view/app.py + HTML)        ← exibe a interface e recebe formulários
    ↕
Controller  (controller/crud.py)   ← processa as ações (INSERT/SELECT/UPDATE/DELETE)
    ↕
  Model  (model/conexao.py)         ← conecta ao SQLite e executa os SQLs
    ↕
 SQLite  (banco.db)                 ← armazena os dados
```

---

## 📋 Funcionalidades (CRUD)

| Operação | Rota Flask        | Método |
|----------|-------------------|--------|
| Listar   | `/`               | GET    |
| Inserir  | `/inserir`        | POST   |
| Editar   | `/editar/<id>`    | GET    |
| Alterar  | `/alterar/<id>`   | POST   |
| Excluir  | `/excluir/<id>`   | POST   |

---

*SENAI — Ribeirão Preto · Maio 2026*
# mvc_project
