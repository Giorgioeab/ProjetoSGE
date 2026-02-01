from conexao_db import obter_sessao, Aluno


def verificar_cpf_existe(cpf):
    """Verifica se um CPF já está cadastrado (aluno ou professor)."""
    from conexao_db import Professor
    session = obter_sessao()
    
    aluno = session.query(Aluno).filter_by(cpf=cpf).first()
    professor = session.query(Professor).filter_by(cpf=cpf).first()
    session.close()
    
    if aluno:
        return True, "CPF já cadastrado como Aluno"
    elif professor:
        return True, "CPF já cadastrado como Professor"
    else:
        return False, "CPF disponível para cadastro"


def cadastrar_aluno(nome, cpf, data_nascimento, nome_mae, email, telefone):
    """Cadastra um novo aluno no banco de dados."""
    session = obter_sessao()

    try:
        aluno_cadastrado = session.query(Aluno).filter_by(cpf=cpf).first()
        
        if aluno_cadastrado:
            session.close()
            return False, "O aluno já é cadastrado"
        
        novo_aluno = Aluno(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento,
            nome_mae=nome_mae,
            email=email,
            telefone=telefone
        )
        session.add(novo_aluno)
        session.commit()
        session.close()
        return True, "O aluno foi cadastrado com sucesso."

    except Exception as e:
        session.close()
        return False, f'ERRO AO CADASTRAR ALUNO. ERRO: {str(e)}'


def listar_alunos():
    """Retorna todos os alunos cadastrados."""
    session = obter_sessao()
    alunos = session.query(Aluno).all()
    resultado = [(a.cpf, a.nome, a.data_nascimento, a.nome_mae, a.email, a.telefone) for a in alunos]
    session.close()
    return resultado


def atualizar_aluno(nome, cpf, data_nascimento, nome_mae, email, telefone):
    """Atualiza os dados de um aluno existente."""
    session = obter_sessao()

    try:
        aluno = session.query(Aluno).filter_by(cpf=cpf).first()

        if not aluno:
            session.close()
            return False, "Aluno não encontrado"
        
        aluno.nome = nome
        aluno.data_nascimento = data_nascimento
        aluno.nome_mae = nome_mae
        aluno.email = email
        aluno.telefone = telefone
        
        session.commit()
        session.close()
        return True, f'{nome} atualizado(a) com sucesso!'
        
    except Exception as e:
        session.close()
        return False, f'Erro ao atualizar aluno. {str(e)}'


def excluir_aluno(cpf):
    """Exclui um aluno do banco de dados."""
    session = obter_sessao()

    try:
        aluno = session.query(Aluno).filter_by(cpf=cpf).first()

        if not aluno:
            session.close()
            return False, "Aluno não encontrado"
        
        session.delete(aluno)
        session.commit()
        session.close()
        return True, 'Aluno excluído com sucesso!'
    
    except Exception as e:
        session.close()
        return False, f'Erro ao excluir aluno. {str(e)}'
