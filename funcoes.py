# Arquivo de compatibilidade - importa todas as funções dos módulos services
from services.alunos import cadastrar_aluno, listar_alunos, atualizar_aluno, excluir_aluno, verificar_cpf_existe
from services.professores import cadastrar_professor, listar_professores, atualizar_professor, excluir_professor
from services.cursos import cadastrar_curso, listar_cursos
from services.turmas import cadastrar_turma, listar_turmas, cadastrar_aluno_turma

# Funções de compatibilidade para código legado
def atualizar_pessoa(nome, cpf, data_nascimento, nome_mae, email, telefone):
    """Atualiza aluno ou professor (busca em ambas as tabelas)."""
    sucesso, msg = atualizar_aluno(nome, cpf, data_nascimento, nome_mae, email, telefone)
    if sucesso:
        return sucesso, msg
    return atualizar_professor(nome, cpf, data_nascimento, nome_mae, email, telefone)


def excluir_pessoa(cpf):
    """Exclui aluno ou professor (busca em ambas as tabelas)."""
    sucesso, msg = excluir_aluno(cpf)
    if sucesso:
        return sucesso, msg
    return excluir_professor(cpf)

if __name__ == "__main__":
    cadastrar_aluno("Claudio", "10010010010", "18/06/1965", "Terezinha", "claudio@gmail", "85 99999-9999")   
    print(listar_alunos())