from conexao_db import obter_sessao, Professor


def cadastrar_professor(nome, cpf, data_nascimento, nome_mae, email, telefone):
    """Cadastra um novo professor no banco de dados."""
    session = obter_sessao()

    try:
        professor_cadastrado = session.query(Professor).filter_by(cpf=cpf).first()
        
        if professor_cadastrado:
            session.close()
            return False, "O Professor já é cadastrado"
        
        novo_professor = Professor(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento,
            nome_mae=nome_mae,
            email=email,
            telefone=telefone
        )
        session.add(novo_professor)
        session.commit()
        session.close()
        return True, "O Professor foi cadastrado com sucesso."

    except Exception as e:
        session.close()
        return False, f'Erro ao cadastrar professor. Erro: {str(e)}'


def listar_professores():
    """Retorna todos os professores cadastrados."""
    session = obter_sessao()
    professores = session.query(Professor).all()
    resultado = [(p.cpf, p.nome, p.data_nascimento, p.nome_mae, p.email, p.telefone) for p in professores]
    session.close()
    return resultado


def atualizar_professor(nome, cpf, data_nascimento, nome_mae, email, telefone):
    """Atualiza os dados de um professor existente."""
    session = obter_sessao()

    try:
        professor = session.query(Professor).filter_by(cpf=cpf).first()

        if not professor:
            session.close()
            return False, "Professor não encontrado"
        
        professor.nome = nome
        professor.data_nascimento = data_nascimento
        professor.nome_mae = nome_mae
        professor.email = email
        professor.telefone = telefone
        
        session.commit()
        session.close()
        return True, f'{nome} atualizado(a) com sucesso!'
        
    except Exception as e:
        session.close()
        return False, f'Erro ao atualizar professor. {str(e)}'


def excluir_professor(cpf):
    """Exclui um professor do banco de dados."""
    session = obter_sessao()

    try:
        professor = session.query(Professor).filter_by(cpf=cpf).first()

        if not professor:
            session.close()
            return False, "Professor não encontrado"
        
        session.delete(professor)
        session.commit()
        session.close()
        return True, 'Professor excluído com sucesso!'
    
    except Exception as e:
        session.close()
        return False, f'Erro ao excluir professor. {str(e)}'
