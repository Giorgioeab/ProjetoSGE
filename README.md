# ProjetoSGE - Sistema de Gestão Escolar

## Descrição

O ProjetoSGE é um Sistema de Gestão Escolar desktop desenvolvido em Python com a biblioteca Tkinter para a interface gráfica. O sistema permite o cadastro, listagem, atualização e exclusão de alunos, professores, cursos e turmas, utilizando um banco de dados SQLite para persistência dos dados.

## Funcionalidades

* **Cadastro de Pessoas:**
    * Cadastrar novos alunos.
    * Cadastrar novos professores.
* **Cadastro de Cursos:**
    * Registrar novos cursos oferecidos pela instituição.
* **Cadastro de Turmas:**
    * Criar turmas vinculando um curso a um professor.
* **Matrícula de Alunos:**
    * Matricular alunos em turmas existentes.
* **Listagem de Dados:**
    * Visualizar a lista de todos os alunos cadastrados.
    * Visualizar a lista de todos os professores cadastrados.
    * Visualizar a lista de todos os cursos.
    * Visualizar a lista de todas as turmas.
* **Atualização de Dados:**
    * Alterar informações de alunos e professores.
* **Exclusão de Dados:**
    * Remover registros de alunos e professores.

## Tecnologias Utilizadas

* **Linguagem de Programação:** Python
* **Interface Gráfica:** Tkinter
* **Banco de Dados:** SQLite 3

## Pré-requisitos

Para executar o projeto, você precisará ter o Python 3 instalado em seu sistema.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd ProjetoSGE
    ```
3.  **Execute o arquivo `tela.py`:**
    ```bash
    python tela.py
    ```
    Isso iniciará a aplicação e abrirá a tela principal do sistema.

## Estrutura de Arquivos

* **`tela.py`**: Contém o código da interface gráfica (GUI) do sistema, construída com Tkinter. É o ponto de entrada da aplicação.
* **`funcoes.py`**: Módulo que implementa todas as funções de interação com o banco de dados (CRUD - Create, Read, Update, Delete) para as entidades do sistema (alunos, professores, cursos, turmas).
* **`conexao_db.py`**: Responsável por estabelecer a conexão com o banco de dados SQLite e criar as tabelas, caso não existam.
* **`SGE.db`**: Arquivo do banco de dados SQLite onde todas as informações são armazenadas.
* **`README.md`**: Este arquivo, contendo a documentação do projeto.

## Estrutura do Banco de Dados

O banco de dados `SGE.db` é composto pelas seguintes tabelas:

* **`Alunos`**:
    * `cpf` (INTEGER, PRIMARY KEY)
    * `nome` (TEXT)
    * `data_nascimento` (TEXT)
    * `nome_mae` (TEXT)
    * `email` (TEXT)
    * `telefone` (TEXT)
* **`Professores`**:
    * `cpf` (INTEGER, PRIMARY KEY)
    * `nome` (TEXT)
    * `data_nascimento` (TEXT)
    * `nome_mae` (TEXT)
    * `email` (TEXT)
    * `telefone` (TEXT)
* **`Cursos`**:
    * `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
    * `nome_curso` (TEXT)
    * `turno` (TEXT)
    * `duracao` (TEXT)
* **`Turmas`**:
    * `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
    * `id_curso` (INTEGER, FOREIGN KEY para `Cursos`)
    * `cpf_professor` (INTEGER, FOREIGN KEY para `Professores`)
* **`Alunos_Turmas`**:
    * `id_aluno` (INTEGER, FOREIGN KEY para `Alunos`)
    * `id_turma` (INTEGER, FOREIGN KEY para `Turmas`)

## Autor

**Giorgio Eab**
