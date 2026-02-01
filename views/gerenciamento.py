# views/gerenciamento.py - Telas de gerenciamento (atualização e exclusão)
import tkinter as tk
from tkinter import ttk
from views.base import TelaBase
from styles import configurar_responsividade
from funcoes import atualizar_pessoa, excluir_pessoa


class TelaAtualizacao(TelaBase):
    """Tela de atualização de pessoas."""
    
    def __init__(self, parent):
        super().__init__(parent, "Atualização de Pessoas", 550, 550)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("✏️ Atualizar Pessoa")
        form_frame = self.criar_form_frame()
        
        self.entry_cpf = self.criar_campo(form_frame, "CPF (para busca):", 0)
        self.entry_nome = self.criar_campo(form_frame, "Novo Nome:", 1)
        self.entry_data_nascimento = self.criar_campo(form_frame, "Nova Data de Nascimento:", 2)
        self.entry_nome_mae = self.criar_campo(form_frame, "Novo Nome da Mãe:", 3)
        self.entry_email = self.criar_campo(form_frame, "Novo Email:", 4)
        self.entry_telefone = self.criar_campo(form_frame, "Novo Telefone:", 5)
        
        btn_frame = self.criar_botao_frame(form_frame, 6)
        ttk.Button(btn_frame, text="Atualizar",
                  command=self._atualizar,
                  style='Primary.TButton').pack(fill='x')
    
    def _atualizar(self):
        sucesso, msg = atualizar_pessoa(
            self.entry_nome.get(),
            self.entry_cpf.get(),
            self.entry_data_nascimento.get(),
            self.entry_nome_mae.get(),
            self.entry_email.get(),
            self.entry_telefone.get()
        )
        if sucesso:
            self.mostrar_sucesso(msg)
        else:
            self.mostrar_erro(msg)


class TelaExclusao(TelaBase):
    """Tela de exclusão de pessoas."""
    
    def __init__(self, parent):
        super().__init__(parent, "Exclusão de Pessoas", 450, 300)
        self._criar_interface()
    
    def _criar_interface(self):
        self.criar_titulo("🗑️ Excluir Pessoa")
        form_frame = self.criar_form_frame()
        
        self.entry_cpf = self.criar_campo(form_frame, "CPF da Pessoa:", 0)
        
        self.lbl_resultado = ttk.Label(form_frame, text="")
        self.lbl_resultado.grid(row=1, column=0, sticky='w', pady=10)
        
        btn_frame = self.criar_botao_frame(form_frame, 2)
        ttk.Button(btn_frame, text="Excluir",
                  command=self._excluir,
                  style='Danger.TButton').pack(fill='x')
    
    def _excluir(self):
        cpf = self.entry_cpf.get()
        
        if not cpf:
            self._mostrar_feedback("⚠️ Informe o CPF", 'Warning.TLabel')
            return
        
        if not self.confirmar_acao("Confirmar Exclusão",
                                   f"Tem certeza que deseja excluir a pessoa com CPF {cpf}?"):
            return
        
        sucesso, msg = excluir_pessoa(cpf)
        
        if sucesso:
            self._mostrar_feedback(f"✓ {msg}", 'Success.TLabel')
            self.entry_cpf.delete(0, tk.END)
        else:
            self._mostrar_feedback(f"✗ {msg}", 'Error.TLabel')
    
    def _mostrar_feedback(self, texto, style):
        """Mostra feedback visual."""
        self.lbl_resultado.configure(text=texto, style=style)
