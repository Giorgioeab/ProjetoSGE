import sqlite3
from tkinter import messagebox



# ---------------------conexão banco ----------------------------
def conectar_banco():
    conexao = sqlite3.connect('SGE.db')
    return conexao


# ---------------------cadastros --------------------------------

def cadastrar_aluno(nome, cpf, data_nascimento, nome_mae, email, telefone):
    conexao = conectar_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''SELECT cpf FROM Alunos
                           WHERE cpf = ? ''',(cpf,))
        aluno_cadastrado = db_conexao.fetchone()
        
        if aluno_cadastrado:
            conexao.close()
            return False, "O aluno já é cadastrado"
        
        db_conexao.execute(''' INSERT INTO Alunos (cpf, nome, data_nascimento, nome_mae, email, telefone)
                           VALUES(?,?,?,?,?,?)''',(cpf, nome, data_nascimento, nome_mae, email, telefone))

        conexao.commit()
        conexao.close()
        return True, "O aluno foi cadastrado com sucesso."

    except Exception as e:
        conexao.close()
        return False, f'ERRO AO CADASTRAR ALUNO. ERRO: {str(e)}'
        
def cadastrar_professor(nome, cpf, data_nascimento, nome_mae, email, telefone):
    conexao = conectar_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''SELECT cpf FROM Professores
                           WHERE cpf = ? ''',(cpf,))
        professor_cadastrado = db_conexao.fetchone()
        
        if professor_cadastrado:
            conexao.close()
            return False, "O Professor já é cadastrado"
        
        db_conexao.execute(''' INSERT INTO Professores (cpf, nome, data_nascimento, nome_mae, email, telefone)
                           VALUES(?,?,?,?,?,?)''',(cpf, nome, data_nascimento, nome_mae, email, telefone))

        conexao.commit()
        conexao.close()
        return True, "O Professor foi cadastrado com sucesso."

    except Exception as e:
        conexao.close()
        return False, f'ERRO AO CADASTRAR PROFESSOR. ERRO: {str(e)}'
    
def cadastrar_curso(nome_curso, turno, duracao):
    conexao = conectar_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute(''' INSERT INTO Cursos (nome_curso, turno, duracao)
                           VALUES (?,?,?) ''',(nome_curso, turno, duracao))
        conexao.commit()
        conexao.close()
        return True, "Curso cadastrado com sucesso"
    
    except Exception as e:
        conexao.close()
        return False, f"Erro ao cadastrar curso. ERRO: {str(e)}"

def cadastar_turma(id_curso, cpf_professor):
    conexao = conectar_banco()
    db_conexao = conexao.cursor()

    try:
        db_conexao.execute('''SELECT id FROM Cursos WHERE id=?''', (id_curso))
        curso_existe = db_conexao.fetchone()

        db_conexao.execute('''SELECT cpf FROM Professores WHERE cpf=?''', (cpf_professor))
        professor_existe = db_conexao.fetchone()


        if not( curso_existe and professor_existe):
            conexao.close()
            return False, "Curso ou professor não exite"
        
        db_conexao.execute(''' INSERT INTO Turmas (id_curso, cpf_professor) 
                           VALUES (?,?) ''', (id_curso, cpf_professor))
        conexao.commit()
        conexao.close()
        return True, "Turma cadastrada com sucesso"


        
    except Exception as e :
        conexao.close()
        return False, f'Erro ao cadastrar turma. ERRO:{str(e)}'

def cadastrar_aluno_turma(id_aluno, id_turma):
    conexao = conectar_banco()
    db_conexao = conexao.cursor()

    try:
        # Verificar se o aluno e a turma existem no banco de dados
        db_conexao.execute("SELECT cpf FROM Alunos WHERE cpf = ?", (id_aluno,))
        aluno_existe = db_conexao.fetchone()

        db_conexao.execute("SELECT id FROM Turmas WHERE id = ?", (id_turma,))
        turma_existe = db_conexao.fetchone()

        if not (aluno_existe and turma_existe):
            return False, "Aluno ou turma não encontrado."

        # Inserir o aluno na turma na tabela Alunos_Turmas
        db_conexao.execute('''
            INSERT INTO Alunos_Turmas (id_aluno, id_turma)
            VALUES (?, ?)''',
           (id_aluno, id_turma))
        conexao.commit()
        
        return True, "Aluno cadastrado na turma com sucesso."

    except Exception as e:
        return False, f"Erro ao cadastrar aluno na turma: {str(e)}"
    finally:
        conexao.close()


  
        
#--------------------------- LISTAGEM----------------------------

def listar_alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Alunos')
    alunos = cursor.fetchall()
    conexao.close()
    return alunos


def listar_professores():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Professores')
    professores = cursor.fetchall()
    conexao.close()
    return professores

def listar_cursos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Cursos')
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

def listar_turmas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Turmas')
    turmas = cursor.fetchall()
    conexao.close()
    return turmas

#----------------------------ATUALIZAÇÃO------------------------

def atualizar_pessoa(nome, cpf, data_nascimento, nome_mae, email, telefone):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute('SELECT cpf FROM Alunos WHERE cpf = ?',(cpf,))
        aluno_existe = cursor.fetchone()

        cursor.execute('SELECT cpf FROM Professores WHERE cpf = ?',(cpf,))
        professor_existe = cursor.fetchone()


        if not (aluno_existe or professor_existe):
            return False, "CPF NÃO ENCONTRADO"
        
        if(aluno_existe):
            cursor.execute( ''' UPDATE Alunos
                           SET nome = ?, cpf =?, data_nascimento =?, nome_mae=?, email=?, telefone=? WHERE cpf =?''',
                           (nome, cpf, data_nascimento, nome_mae, email, telefone, cpf))
        elif(professor_existe):
            cursor.execute( ''' UPDATE Professores
                           SET nome = ?, cpf =?, data_nascimento =?, nome_mae=?, email=?, telefone=? WHERE cpf =?''',
                           (nome, cpf, data_nascimento, nome_mae, email, telefone, cpf))
        
        conexao.commit()
        
        return True, f'{nome} atualizado(a) com sucesso!'
        
    except Exception as e:
        return False, f' Erro ao atualizar pessoa. {str(e)} '
    
    finally:
        conexao.close()


#----------------------------EXCLUSÃO----------------------------

def excluir_pessoa(cpf):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute('SELECT cpf FROM Alunos WHERE cpf = ?',(cpf,))
        aluno_existe = cursor.fetchone()

        cursor.execute('SELECT cpf FROM Professores WHERE cpf = ?',(cpf,))
        professor_existe = cursor.fetchone()

        if not (aluno_existe or professor_existe):
            return False, "CPF NÃO ENCONTRADO"
        
        if(aluno_existe):
            cursor.execute('DELETE FROM Alunos WHERE cpf = ?',(cpf,))

        elif (professor_existe):
            cursor.execute('DELETE FROM Professores WHERE cpf = ?',(cpf,))

        conexao.commit()
        
        return True, 'Pessoa excluída com sucesso!'    
    
    except Exception as e:
        return False, f'Erro ao excluir pessoa.{str(e)}'
    
    finally:
        conexao.close()




        
cadastrar_aluno("Claudio", "10010010010", "18/06/1965", "Terezinha", "claudio@gmail", "85 99999-9999")   

print(listar_alunos())