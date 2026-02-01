from conexao_db import obter_sessao, Curso


def cadastrar_curso(nome_curso, turno, duracao):
    """Cadastra um novo curso no banco de dados."""
    session = obter_sessao()

    try:
        novo_curso = Curso(
            nome_curso=nome_curso,
            turno=turno,
            duracao=duracao
        )
        session.add(novo_curso)
        session.commit()
        session.close()
        return True, "Curso cadastrado com sucesso"
    
    except Exception as e:
        session.close()
        return False, f"Erro ao cadastrar curso. ERRO: {str(e)}"


def listar_cursos():
    """Retorna todos os cursos cadastrados."""
    session = obter_sessao()
    cursos = session.query(Curso).all()
    resultado = [(c.id, c.nome_curso, c.turno, c.duracao) for c in cursos]
    session.close()
    return resultado
