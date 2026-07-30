--

# 🎓 Sistema de Gestão de Alunos com MVC, Flask e Docker

> Projeto desenvolvido para demonstrar a implementação prática do padrão arquitetural MVC (Model-View-Controller), operações CRUD e containerização utilizando Docker.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![MVC](https://img.shields.io/badge/Architecture-MVC-orange)

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de demonstrar a aplicação prática do padrão de arquitetura MVC (Model-View-Controller) em uma aplicação web completa.

A solução permite o gerenciamento de alunos através das operações CRUD (Create, Read, Update e Delete), utilizando Python, Flask e SQLite.

Como diferencial, a aplicação foi totalmente containerizada utilizando Docker e Docker Compose, permitindo sua execução em qualquer ambiente com um único comando.

---

## 🎯 Objetivos do Projeto

* Demonstrar a arquitetura MVC na prática.
* Aplicar conceitos de desenvolvimento web com Flask.
* Implementar operações CRUD completas.
* Utilizar banco de dados SQLite.
* Demonstrar containerização com Docker.
* Criar um ambiente reproduzível para fins educacionais.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia     | Finalidade          |
| -------------- | ------------------- |
| Python 3.12    | Linguagem principal |
| Flask          | Framework Web       |
| SQLite         | Banco de Dados      |
| Jinja2         | Templates HTML      |
| HTML5          | Interface           |
| CSS3           | Estilização         |
| Docker         | Containerização     |
| Docker Compose | Orquestração        |

---

## 🏗️ Arquitetura MVC

O projeto segue rigorosamente a separação de responsabilidades proposta pelo padrão MVC.

### Model

Responsável pela persistência e acesso aos dados.

* Conexão com SQLite
* Criação automática da tabela
* Execução de comandos SQL

### Controller

Responsável pelas regras de negócio.

* Inserir registros
* Consultar registros
* Atualizar registros
* Excluir registros

### View

Responsável pela interação com o usuário.

* Interface web
* Formulários
* Tabelas de consulta
* Navegação da aplicação

---

## 📂 Estrutura do Projeto

```text
mvc_project/
├── model/
│   └── conexao.py
├── controller/
│   └── crud.py
├── view/
│   ├── app.py
│   ├── templates/
│   └── static/
├── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 📸 Demonstração

### Arquitetura MVC

> Inserir imagem: mvc-conceito.png

### Estrutura do Projeto

> Inserir imagem: estrutura-projeto.png

### Cadastro de Alunos

> Inserir imagem: create-aluno.png

### Consulta de Alunos

> Inserir imagem: read-alunos.png

### Fluxo Completo MVC

> Inserir imagem: fluxo-mvc.png

---

## 🔄 Funcionalidades

### CREATE

Cadastro de novos alunos.

### READ

Consulta dos registros cadastrados.

### UPDATE

Atualização dos dados dos alunos.

### DELETE

Exclusão de registros.

---

## 🐳 Containerização

A aplicação foi containerizada utilizando Docker Compose.

Embora não fosse um requisito do projeto original, a containerização foi adotada para garantir:

* Portabilidade
* Facilidade de implantação
* Padronização do ambiente
* Isolamento de dependências
* Reprodutibilidade

### Executar o Projeto

```bash
docker compose up --build
```

Acessar:

```text
http://localhost:5000
```

### Encerrar o Ambiente

```bash
docker compose down
```

---

## 💾 Persistência de Dados

Os dados são armazenados em SQLite e preservados através de volume Docker, permitindo manter as informações mesmo após reinicializações do container.

---

## 📚 Conceitos Demonstrados

* Arquitetura MVC
* CRUD
* Flask
* SQLite
* Docker
* Docker Compose
* Persistência de Dados
* Volume Docker
* Containerização
* Organização de Código
* Separação de Responsabilidades

---

## 🚀 Evoluções Futuras

* PostgreSQL
* API REST
* Autenticação de Usuários
* GitHub Actions
* CI/CD
* Deploy em Oracle Cloud Infrastructure (OCI)
* Monitoramento com Prometheus e Grafana
* Kubernetes

---

## 👨‍💻 Autor

Rogério Sá de Macedo

Analista de Tecnologia | Cloud | DevOps | Inteligência Artificial

📍 Ribeirão Preto - SP

LinkedIn:
[https://www.linkedin.com/in/rogerio-macedo-11201229/](https://www.linkedin.com/in/rogerio-macedo-11201229/)

---

## 🎓 Contexto Acadêmico

Projeto utilizado como demonstração prática durante aula teste para o cargo de Instrutor de Tecnologia da Informação, apresentando conceitos de arquitetura de software, desenvolvimento web e containerização.

