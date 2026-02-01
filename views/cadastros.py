# views/cadastros.py - Telas de cadastro
import tkinter as tk
from tkinter import ttk
from views.base import TelaBase
from styles import COLORS, FONTS, centralizar_janela, configurar_responsividade
from funcoes import (
    cadastrar_aluno, cadastrar_professor, cadastrar_curso,
    cadastrar_turma, cadastrar_aluno_turma, verificar_cpf_existe
)


class TelaCadastro(TelaBase):
    """Tela de cadastro de pessoas (alunos/professores)."""
    
    def __init__(self, parent):
        super().__init__(parent, "Cadastro de Pessoas", 550, 600)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("👤 Cadastro de Pessoas")
        form_frame = self.criar_form_frame()
        
        self._criar_campo_cpf(form_frame)
        self._criar_campos_dados(form_frame)
        self._criar_botoes(form_frame)
    
    def _criar_campo_cpf(self, parent):
        """Cria campo CPF com botão de verificação."""
        cpf_frame = ttk.Frame(parent)
        cpf_frame.grid(row=0, column=0, sticky='ew', pady=8)
        configurar_responsividade(cpf_frame)
        
        ttk.Label(cpf_frame, text="CPF:", style='Heading.TLabel').grid(row=0, column=0, sticky='w')
        
        input_frame = ttk.Frame(cpf_frame)
        input_frame.grid(row=1, column=0, sticky='ew', pady=(5, 0))
        input_frame.columnconfigure(0, weight=1)
        
        self.entry_cpf = ttk.Entry(input_frame, font=FONTS['body'])
        self.entry_cpf.grid(row=0, column=0, sticky='ew', ipady=5, padx=(0, 10))
        
        btn_verificar = ttk.Button(input_frame, text="Verificar",
                                   command=self._verificar_cpf,
                                   style='Secondary.TButton')
        btn_verificar.grid(row=0, column=1)
        
        self.lbl_status_cpf = ttk.Label(cpf_frame, text="")
        self.lbl_status_cpf.grid(row=2, column=0, sticky='w', pady=(5, 0))
    
    def _criar_campos_dados(self, parent):
        """Cria os campos de dados pessoais."""
        self.entry_nome = self.criar_campo(parent, "Nome:", 1)
        self.entry_data_nascimento = self.criar_campo(parent, "Data de Nascimento:", 2)
        self.entry_nome_mae = self.criar_campo(parent, "Nome da Mãe:", 3)
        self.entry_email = self.criar_campo(parent, "Email:", 4)
        self.entry_telefone = self.criar_campo(parent, "Telefone:", 5)
    
    def _criar_botoes(self, parent):
        """Cria os botões de ação."""
        btn_frame = ttk.Frame(parent)
        btn_frame.grid(row=6, column=0, sticky='ew', pady=(20, 0))
        configurar_responsividade(btn_frame, colunas=2)
        
        ttk.Button(btn_frame, text="Cadastrar Aluno",
                  command=self._cadastrar_aluno,
                  style='Primary.TButton').grid(row=0, column=0, sticky='ew', padx=(0, 5))
        
        ttk.Button(btn_frame, text="Cadastrar Professor",
                  command=self._cadastrar_professor,
                  style='Success.TButton').grid(row=0, column=1, sticky='ew', padx=(5, 0))
    
    def _verificar_cpf(self):
        """Verifica se o CPF já existe."""
        cpf = self.entry_cpf.get()
        if not cpf:
            self.lbl_status_cpf.configure(text="⚠️ Digite um CPF", style='Warning.TLabel')
            return
        
        existe, msg = verificar_cpf_existe(cpf)
        style = 'Error.TLabel' if existe else 'Success.TLabel'
        simbolo = "✗" if existe else "✓"
        self.lbl_status_cpf.configure(text=f"{simbolo} {msg}", style=style)
    
    def _get_dados(self):
        """Retorna os dados do formulário."""
        return {
            'cpf': self.entry_cpf.get(),
            'nome': self.entry_nome.get(),
            'data_nascimento': self.entry_data_nascimento.get(),
            'nome_mae': self.entry_nome_mae.get(),
            'email': self.entry_email.get(),
            'telefone': self.entry_telefone.get()
        }
    
    def _limpar_formulario(self):
        """Limpa todos os campos."""
        self.limpar_campos(
            self.entry_cpf, self.entry_nome, self.entry_data_nascimento,
            self.entry_nome_mae, self.entry_email, self.entry_telefone
        )
        self.lbl_status_cpf.configure(text="")
    
    def _cadastrar_aluno(self):
        """Cadastra um aluno."""
        dados = self._get_dados()
        sucesso, msg = cadastrar_aluno(
            dados['nome'], dados['cpf'], dados['data_nascimento'],
            dados['nome_mae'], dados['email'], dados['telefone']
        )
        self._processar_resultado(sucesso, msg, "Aluno", dados)
    
    def _cadastrar_professor(self):
        """Cadastra um professor."""
        dados = self._get_dados()
        sucesso, msg = cadastrar_professor(
            dados['nome'], dados['cpf'], dados['data_nascimento'],
            dados['nome_mae'], dados['email'], dados['telefone']
        )
        self._processar_resultado(sucesso, msg, "Professor", dados)
    
    def _processar_resultado(self, sucesso, msg, tipo, dados):
        """Processa o resultado do cadastro."""
        if sucesso:
            self._limpar_formulario()
            JanelaConfirmacao(self, tipo, dados)
        else:
            self.mostrar_erro(msg)


class JanelaConfirmacao(tk.Toplevel):
    """Janela de confirmação de cadastro."""
    
    def __init__(self, parent, tipo, dados):
        super().__init__(parent)
        self.title(f"Cadastro de {tipo} Realizado")
        self.configure(bg=COLORS['background'])
        centralizar_janela(self, 400, 350)
        self.grab_set()
        
        self._criar_interface(tipo, dados)
    
    def _criar_interface(self, tipo, dados):
        frame = ttk.Frame(self, padding=30)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text=f"✓ {tipo} cadastrado(a) com sucesso!",
                 style='Title.TLabel', foreground=COLORS['success']).pack(pady=(0, 20))
        
        self._exibir_dados(frame, dados)
        
        ttk.Button(frame, text="OK", command=self.destroy,
                  style='Primary.TButton').pack(pady=(20, 0))
    
    def _exibir_dados(self, parent, dados):
        """Exibe os dados cadastrados."""
        dados_frame = ttk.Frame(parent)
        dados_frame.pack(fill='x')
        
        labels = ["CPF:", "Nome:", "Data Nasc.:", "Nome da Mãe:", "Email:", "Telefone:"]
        valores = [dados['cpf'], dados['nome'], dados['data_nascimento'],
                  dados['nome_mae'], dados['email'], dados['telefone']]
        
        for lbl, val in zip(labels, valores):
            row = ttk.Frame(dados_frame)
            row.pack(fill='x', pady=3)
            ttk.Label(row, text=lbl, style='Heading.TLabel', width=15).pack(side='left')
            ttk.Label(row, text=val).pack(side='left')


class TelaCadastroCurso(TelaBase):
    """Tela de cadastro de cursos."""
    
    def __init__(self, parent):
        super().__init__(parent, "Cadastro de Cursos", 500, 400)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("📚 Cadastro de Cursos")
        form_frame = self.criar_form_frame()
        
        self.entry_nome = self.criar_campo(form_frame, "Nome do Curso:", 0)
        self.entry_turno = self.criar_campo(form_frame, "Turno:", 1)
        self.entry_duracao = self.criar_campo(form_frame, "Duração:", 2)
        
        btn_frame = self.criar_botao_frame(form_frame, 3)
        ttk.Button(btn_frame, text="Cadastrar Curso",
                  command=self._cadastrar,
                  style='Primary.TButton').pack(fill='x')
    
    def _cadastrar(self):
        sucesso, msg = cadastrar_curso(
            self.entry_nome.get(),
            self.entry_turno.get(),
            self.entry_duracao.get()
        )
        if sucesso:
            self.mostrar_sucesso(msg)
            self.limpar_campos(self.entry_nome, self.entry_turno, self.entry_duracao)
        else:
            self.mostrar_erro(msg)


class TelaCadastroTurma(TelaBase):
    """Tela de cadastro de turmas."""
    
    def __init__(self, parent):
        super().__init__(parent, "Cadastro de Turmas", 500, 350)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("🏫 Cadastro de Turmas")
        form_frame = self.criar_form_frame()
        
        self.entry_curso = self.criar_campo(form_frame, "ID do Curso:", 0)
        self.entry_professor = self.criar_campo(form_frame, "CPF do Professor:", 1)
        
        btn_frame = self.criar_botao_frame(form_frame, 2)
        ttk.Button(btn_frame, text="Cadastrar Turma",
                  command=self._cadastrar,
                  style='Primary.TButton').pack(fill='x')
    
    def _cadastrar(self):
        sucesso, msg = cadastrar_turma(
            self.entry_curso.get(),
            self.entry_professor.get()
        )
        if sucesso:
            self.mostrar_sucesso(msg)
            self.limpar_campos(self.entry_curso, self.entry_professor)
        else:
            self.mostrar_erro(msg)


class TelaMatricula(TelaBase):
    """Tela de matrícula de alunos em turmas."""
    
    def __init__(self, parent):
        super().__init__(parent, "Matrícula de Alunos", 500, 350)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("📝 Matricular Aluno em Turma")
        form_frame = self.criar_form_frame()
        
        self.entry_aluno = self.criar_campo(form_frame, "CPF do Aluno:", 0)
        self.entry_turma = self.criar_campo(form_frame, "ID da Turma:", 1)
        
        btn_frame = self.criar_botao_frame(form_frame, 2)
        ttk.Button(btn_frame, text="Matricular",
                  command=self._matricular,
                  style='Primary.TButton').pack(fill='x')
    
    def _matricular(self):
        sucesso, msg = cadastrar_aluno_turma(
            self.entry_aluno.get(),
            self.entry_turma.get()
        )
        if sucesso:
            self.mostrar_sucesso(msg)
            self.limpar_campos(self.entry_aluno, self.entry_turma)
        else:
            self.mostrar_erro(msg)
