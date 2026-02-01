# views/listagens.py - Telas de listagem
from tkinter import ttk
from threading import Thread
from views.base import TelaBase
from styles import configurar_responsividade
from funcoes import listar_alunos, listar_professores, listar_cursos, listar_turmas


class TelaListagemBase(TelaBase):
    """Classe base para telas de listagem com Treeview."""
    
    __slots__ = ('colunas', 'tree')
    
    def __init__(self, parent, titulo, largura, altura, colunas):
        self.colunas = colunas
        super().__init__(parent, titulo, largura, altura)
    
    def criar_treeview(self, row=1):
        """Cria e configura o Treeview com scrollbar."""
        tree_frame = ttk.Frame(self.main_frame)
        tree_frame.grid(row=row, column=0, sticky='nsew')
        self.main_frame.rowconfigure(row, weight=1)
        configurar_responsividade(tree_frame)
        tree_frame.rowconfigure(0, weight=1)
        
        self.tree = ttk.Treeview(tree_frame, columns=self.colunas, show='headings')
        
        for col in self.colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        return self.tree
    
    def carregar_dados(self, dados):
        """Carrega os dados no Treeview."""
        # Limpeza em lote é mais rápida
        children = self.tree.get_children()
        if children:
            self.tree.delete(*children)
        
        # Inserção em lote
        for item in dados:
            self.tree.insert('', 'end', values=item)
    
    def carregar_dados_async(self, func_dados):
        """Carrega dados de forma assíncrona para não travar a UI."""
        def _carregar():
            dados = func_dados()
            # Atualiza UI na thread principal
            self.after(0, lambda: self.carregar_dados(dados))
        
        Thread(target=_carregar, daemon=True).start()


class TelaListagem(TelaListagemBase):
    """Tela de listagem de pessoas (alunos/professores)."""
    
    COLUNAS = ("CPF", "Nome", "Data Nasc.", "Nome da Mãe", "Email", "Telefone")
    __slots__ = ('tipo',)
    
    def __init__(self, parent, tipo):
        self.tipo = tipo
        titulo = f"Listagem de {'Alunos' if tipo == 'alunos' else 'Professores'}"
        super().__init__(parent, titulo, 900, 500, self.COLUNAS)
        self._criar_interface()
    
    def _criar_interface(self):
        emoji = "👨‍🎓" if self.tipo == "alunos" else "👨‍🏫"
        nome = "Alunos" if self.tipo == "alunos" else "Professores"
        
        self.criar_titulo(f"{emoji} {nome} Cadastrados")
        self.criar_treeview()
        # Carrega dados de forma assíncrona
        func = listar_alunos if self.tipo == "alunos" else listar_professores
        self.carregar_dados_async(func)


class TelaListagemCursos(TelaListagemBase):
    """Tela de listagem de cursos."""
    
    COLUNAS = ("ID", "Nome do Curso", "Turno", "Duração")
    __slots__ = ()
    
    def __init__(self, parent):
        super().__init__(parent, "Listagem de Cursos", 700, 400, self.COLUNAS)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("📚 Cursos Cadastrados")
        self.criar_treeview()
        self.carregar_dados_async(listar_cursos)


class TelaListagemTurmas(TelaListagemBase):
    """Tela de listagem de turmas."""
    
    COLUNAS = ("ID Turma", "ID Curso", "CPF Professor")
    __slots__ = ()
    
    def __init__(self, parent):
        super().__init__(parent, "Listagem de Turmas", 600, 400, self.COLUNAS)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("🏫 Turmas Cadastradas")
        self.criar_treeview()
        self.carregar_dados_async(listar_turmas)
