# 🎓 ProjetoSGE - Sistema de Gestão Escolar

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?logo=python&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Tkinter-GUI-green" alt="Tkinter">
  <img src="https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite&logoColor=white" alt="SQLite">
</p>

## 📋 Descrição

O **ProjetoSGE** é um Sistema de Gestão Escolar desktop desenvolvido em Python com interface gráfica Tkinter. O sistema permite o gerenciamento completo de alunos, professores, cursos e turmas, utilizando **SQLAlchemy** como ORM para persistência dos dados em SQLite.

## ✨ Funcionalidades

### 👥 Gestão de Pessoas
- ✅ Cadastrar alunos e professores
- ✅ Verificação de CPF antes do cadastro (evita duplicatas)
- ✅ Atualizar informações pessoais
- ✅ Excluir registros
- ✅ Janela de visualização de dados após cadastro

### 📚 Gestão de Cursos
- ✅ Registrar cursos com nome, turno e duração
- ✅ Listar todos os cursos cadastrados

### 🏫 Gestão de Turmas
- ✅ Criar turmas vinculando curso e professor
- ✅ Matricular alunos em turmas
- ✅ Listar todas as turmas

### 📊 Listagens
- ✅ Visualizar todos os alunos
- ✅ Visualizar todos os professores
- ✅ Visualizar todos os cursos
- ✅ Visualizar todas as turmas

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **Python 3** | Linguagem de programação |
| **Tkinter** | Interface gráfica (GUI) |
| **SQLAlchemy** | ORM para banco de dados |
| **SQLite** | Banco de dados relacional |

##  Como Executar

### Pré-requisitos
- Python 3.x instalado
- pip (gerenciador de pacotes)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Giorgioeab/ProjetoSGE.git
   ou
   gh repo clone Giorgioeab/ProjetoSGE - usando o GitHub CLI
   cd ProjetoSGE
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv .venv
   
   # Windows
   .\.venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python tela.py
   ```

## 📸 Screenshots

> *Em breve: capturas de tela da aplicação*

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 👤 Autor

**Giorgioeab**

---

<p align="center">
  Feito para fins educacionais
</p>
