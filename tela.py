# tela_moderna.py - Aplicacao principal do SGE
"""
Sistema de Gestao Escolar - Interface Grafica Moderna
"""
import tkinter as tk
from tkinter import ttk
from styles import COLORS, FONTS, configurar_estilos, configurar_responsividade
from views import (
    TelaCadastro, TelaCadastroCurso, TelaCadastroTurma, TelaMatricula,
    TelaListagem, TelaListagemCursos, TelaListagemTurmas,
    TelaAtualizacao, TelaExclusao
)


class AplicacaoSGE:
    """Classe principal da aplicacao SGE."""
    
    def __init__(self):
        self.root = tk.Tk()
        self._configurar_janela()
        self._criar_interface()
    
    def _configurar_janela(self):
        """Configura a janela principal."""
        self.root.title("SGE - Sistema de Gestao Escolar")
        self.root.configure(bg=COLORS['background'])
        self.root.minsize(800, 600)
        self.root.state('zoomed')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        configurar_estilos()
    
    def _criar_interface(self):
        """Cria a interface principal."""
        main_container = ttk.Frame(self.root, padding=20)
        main_container.grid(row=0, column=0, sticky='nsew')
        configurar_responsividade(main_container)
        main_container.rowconfigure(1, weight=1)
        
        self._criar_header(main_container)
        self._criar_area_conteudo(main_container)
        self._criar_footer(main_container)
    
    def _criar_header(self, parent):
        """Cria o cabecalho."""
        header = ttk.Frame(parent)
        header.grid(row=0, column=0, sticky='ew')
        
        ttk.Label(header, text="Sistema de Gestao Escolar",
                 style='Title.TLabel').grid(row=0, column=0, sticky='w')
        
        ttk.Label(header, text="Gerencie alunos, professores, cursos e turmas",
                 foreground=COLORS['text_secondary']).grid(row=1, column=0, sticky='w', pady=(5, 0))
    
    def _criar_area_conteudo(self, parent):
        """Cria a area de conteudo com cards."""
        content = ttk.Frame(parent)
        content.grid(row=1, column=0, sticky='nsew', pady=(20, 0))
        configurar_responsividade(content, colunas=3)
        content.rowconfigure(0, weight=1)
        
        self._criar_card_cadastro(content, 0)
        self._criar_card_listagem(content, 1)
        self._criar_card_gerenciamento(content, 2)
    
    def _criar_card(self, parent, col, titulo, cor):
        """Cria um card generico."""
        frame = ttk.Frame(parent)
        frame.grid(row=0, column=col, sticky='nsew', padx=10, pady=10)
        configurar_responsividade(frame)
        frame.rowconfigure(1, weight=1)
        
        ttk.Label(frame, text=titulo, font=FONTS['subtitle'],
                 foreground=cor).grid(row=0, column=0, sticky='w', pady=(0, 10))
        
        inner = ttk.Frame(frame, padding=15)
        inner.grid(row=1, column=0, sticky='nsew')
        return inner
    
    def _criar_card_cadastro(self, parent, col):
        """Cria o card de cadastros."""
        card = self._criar_card(parent, col, "Cadastros", COLORS['primary'])
        
        botoes = [
            ("Cadastrar Pessoas", lambda: TelaCadastro(self.root), 'Primary.TButton'),
            ("Cadastrar Cursos", lambda: TelaCadastroCurso(self.root), 'Primary.TButton'),
            ("Cadastrar Turmas", lambda: TelaCadastroTurma(self.root), 'Primary.TButton'),
        ]
        self._adicionar_botoes(card, botoes)
    
    def _criar_card_listagem(self, parent, col):
        """Cria o card de listagens."""
        card = self._criar_card(parent, col, "Listagens", COLORS['success'])
        
        botoes = [
            ("Listar Alunos", lambda: TelaListagem(self.root, "alunos"), 'Success.TButton'),
            ("Listar Professores", lambda: TelaListagem(self.root, "professores"), 'Success.TButton'),
            ("Listar Cursos", lambda: TelaListagemCursos(self.root), 'Success.TButton'),
            ("Listar Turmas", lambda: TelaListagemTurmas(self.root), 'Success.TButton'),
        ]
        self._adicionar_botoes(card, botoes)
    
    def _criar_card_gerenciamento(self, parent, col):
        """Cria o card de gerenciamento."""
        card = self._criar_card(parent, col, "Gerenciamento", COLORS['warning'])
        
        botoes = [
            ("Atualizar Pessoa", lambda: TelaAtualizacao(self.root), 'TButton'),
            ("Excluir Pessoa", lambda: TelaExclusao(self.root), 'Danger.TButton'),
            ("Matricular Aluno", lambda: TelaMatricula(self.root), 'TButton'),
        ]
        self._adicionar_botoes(card, botoes)
    
    def _adicionar_botoes(self, parent, botoes):
        """Adiciona uma lista de botoes ao container."""
        for texto, comando, style in botoes:
            ttk.Button(parent, text=texto, command=comando,
                      style=style).pack(fill='x', pady=5)
    
    def _criar_footer(self, parent):
        """Cria o rodape."""
        footer = ttk.Frame(parent)
        footer.grid(row=2, column=0, sticky='ew', pady=(20, 0))
        
        ttk.Label(footer, text="SGE - Sistema de Gestao Escolar - 2026",
                 foreground=COLORS['text_secondary'],
                 font=FONTS['small']).pack()
    
    def executar(self):
        """Inicia a aplicacao."""
        self.root.mainloop()


def main():
    """Ponto de entrada da aplicacao."""
    app = AplicacaoSGE()
    app.executar()


if __name__ == "__main__":
    main()
