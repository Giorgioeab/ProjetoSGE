import sqlite3 as sql
from tkinter import messagebox

# conexao banco

def conexao_banco():
    conexao = sql.connect('SGE.db')
    return conexao

# Cadastros

def cadastrar_aluno(nome, cpf, data_nascimento, nome_mae, email, telefone):
    conexao = conexao_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''
        SELECT cpf FROM Alunos WHERE cpf = ?''', (cpf,))
        aluno_cadastrado = db_conexao.fetchone()
        
        if aluno_cadastrado:
            conexao.close()
            return False, 'O aluno já está cadastrado no sistema.'
        
        db_conexao.execute('''INSERT INTO Alunos (cpf, nome, data_nascimento, nome_mae, email, telefone)
        VALUES(?,?,?,?,?,?)''', (nome, cpf, data_nascimento, nome_mae, email, telefone))
        conexao.commit()
        conexao.close()
        return True, 'O aluno foi cadastrado com sucesso.'

    except Exception as e:
        conexao.close()
        return False, f'Erro ao cadastrar o aluno. Erro {str(e)}'
    
def cadastrar_professor(nome, cpf, data_nascimento, nome_mae, email, telefone):
    conexao = conexao_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''
        SELECT cpf FROM Alunos WHERE cpf = ?''', (cpf,))
        professor_cadastrado = db_conexao.fetchone()
        
        if professor_cadastrado:
            conexao.close()
            return False, 'O professor já está cadastrado no sistema.'
        
        db_conexao.execute('''INSERT INTO Professores (cpf, nome, data_nascimento, nome_mae, email, telefone)
        VALUES(?,?,?,?,?,?)''', (nome, cpf, data_nascimento, nome_mae, email, telefone))
        conexao.commit()
        conexao.close()
        return True, 'O professor foi cadastrado com sucesso.'

    except Exception as e:
        conexao.close()
        return False, f'Erro ao cadastrar o professor. Erro: {str(e)}'
    
def cadastrar_curso(nome_curso, turno, duracao):
    conexao = conexao_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''INSERT INTO Cursos(nome_curso, turno, duracao) 
        VALUES(?,?,?)''', (nome_curso, turno, duracao))
        conexao.commit()
        conexao.close()
        return True, 'Curso foi cadastrado com sucesso.'
    
    except Exception as e:
        conexao.close()
        return False, f'Erro ao cadastrar o curso. Erro: {str(e)}'
    
def cadastrar_turma(id_curso, cpf_professor):
    conexao = conexao_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''SELECT id FROM Cursos WHERE id=?''',(id_curso)) 
        curso_existe = db_conexao.fetchone()
        db_conexao.execute('''SELECT cpf FROM Professores WHERE cpf=?''',(cpf_professor)) 
        professor_existe = db_conexao.fetchone()
        if not (curso_existe and professor_existe):
            conexao.close()
            return False, 'Curso ou Professor não existe.'
        
        db_conexao.execute('''INSERT INTO Turmas (id_curso, cpf_professor) 
        VALUES (?,?)''', (id_curso,cpf_professor))
        conexao.commit()
        conexao.close()
        return True, 'Turma cadastrada com sucesso.'
    
    except Exception as e:
        conexao.close()
        return False, f'Erro ao cadastrar a turma. Erro: {str(e)}'