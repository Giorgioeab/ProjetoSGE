import sqlite3 as sql

def conexao_banco():
    conexao = sql.connect('SGE.db')
    return conexao

# criando tabelas

def criar_tabela_alunos(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos (
    cpf INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    nome_mae TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL)
    ''')

def criar_tabela_professores(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Professores(
    cpf INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    nome_mae TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL)
    ''')

def criar_tabela_cursos(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cursos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso TEXT NOT NULL,
    turno TEXT NOT NULL,
    duracao TEXT NOT NULL)
    ''')

def criar_tabela_turmas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Turmas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_curso INTEGER,
    cpf_professor INTEGER,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id),
    FOREIGN KEY (cpf_professor) REFERENCES Professores (cpf))
    ''')

def criar_tabela_alunos_turmas(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos_Turmas(
    id_aluno INTEGER,
    id_turma INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Alunos(cpf),
    FOREIGN KEY (id_turma) REFERENCES Turmas(id))
    ''')

if __name__ == "__main__":
    conexao=conexao_banco()
    criar_tabela_alunos(conexao)
    criar_tabela_professores(conexao)
    criar_tabela_cursos(conexao)
    criar_tabela_turmas(conexao)
    criar_tabela_alunos_turmas(conexao)

    # conexao.close()

def testInsert(conexao, curso, turno, duracao):
    cursor=conexao.cursor()
    cursor.execute (f'''
    INSERT INTO Cursos (nome_curso, turno, duracao) VALUES
    ('{curso}', '{turno}', '{duracao}')''')

def testSelect(conexao):
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM Cursos''')
    linhasRetornadas = cursor.fetchall()

    for linha in linhasRetornadas:
        print(linha)

testInsert(conexao, 'Juan','Manhã','12 Meses')
testSelect(conexao)