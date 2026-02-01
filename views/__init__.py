# views/__init__.py - Exporta todas as views
from views.base import TelaBase
from views.cadastros import (
    TelaCadastro,
    TelaCadastroCurso,
    TelaCadastroTurma,
    TelaMatricula
)
from views.listagens import (
    TelaListagem,
    TelaListagemCursos,
    TelaListagemTurmas
)
from views.gerenciamento import (
    TelaAtualizacao,
    TelaExclusao
)

__all__ = [
    'TelaBase',
    'TelaCadastro',
    'TelaCadastroCurso',
    'TelaCadastroTurma',
    'TelaMatricula',
    'TelaListagem',
    'TelaListagemCursos',
    'TelaListagemTurmas',
    'TelaAtualizacao',
    'TelaExclusao',
]
