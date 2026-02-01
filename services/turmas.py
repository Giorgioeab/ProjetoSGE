from conexao_db import obter_sessao, Turma, Curso, Professor, Aluno, AlunoTurma


def cadastrar_turma(id_curso, cpf_professor):
    """Cadastra uma nova turma no banco de dados."""
    session = obter_sessao()

    try:
        curso_existe = session.query(Curso).filter_by(id=id_curso).first()
        professor_existe = session.query(Professor).filter_by(cpf=cpf_professor).first()

        if not (curso_existe and professor_existe):
            session.close()
            return False, "Curso ou professor não existe"
        
        nova_turma = Turma(
            id_curso=id_curso,
            cpf_professor=cpf_professor
        )
        session.add(nova_turma)
        session.commit()
        session.close()
        return True, "Turma cadastrada com sucesso"
        
    except Exception as e:
        session.close()
        return False, f'Erro ao cadastrar turma. ERRO: {str(e)}'


def listar_turmas():
    """Retorna todas as turmas cadastradas."""
    session = obter_sessao()
    turmas = session.query(Turma).all()
    resultado = [(t.id, t.id_curso, t.cpf_professor) for t in turmas]
    session.close()
    return resultado


def cadastrar_aluno_turma(id_aluno, id_turma):
    """Cadastra um aluno em uma turma."""
    session = obter_sessao()

    try:
        aluno_existe = session.query(Aluno).filter_by(cpf=id_aluno).first()
        turma_existe = session.query(Turma).filter_by(id=id_turma).first()

        if not (aluno_existe and turma_existe):
            session.close()
            return False, "Aluno ou turma não encontrado."

        novo_aluno_turma = AlunoTurma(
            id_aluno=id_aluno,
            id_turma=id_turma
        )
        session.add(novo_aluno_turma)
        session.commit()
        session.close()
        return True, "Aluno cadastrado na turma com sucesso."

    except Exception as e:
        session.close()
        return False, f"Erro ao cadastrar aluno na turma: {str(e)}"
