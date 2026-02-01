# views/base.py - Classe base para todas as telas
import tkinter as tk
from tkinter import ttk, messagebox
from styles import COLORS, FONTS, centralizar_janela, configurar_responsividade


class TelaBase(tk.Toplevel):
    """Classe base abstrata para todas as telas secundárias."""
    
    __slots__ = ('main_frame',)
    
    def __init__(self, parent, titulo, largura=600, altura=500):
        super().__init__(parent)
        self.title(titulo)
        self.configure(bg=COLORS['background'])
        self.minsize(largura, altura)
        centralizar_janela(self, largura, altura)
        
        self._configurar_layout()
        self._criar_container_principal()
    
    def _configurar_layout(self):
        """Configura o layout responsivo da janela."""
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    
    def _criar_container_principal(self):
        """Cria o container principal da tela."""
        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.grid(row=0, column=0, sticky='nsew')
        configurar_responsividade(self.main_frame)
    
    def criar_titulo(self, texto):
        """Cria o título da tela."""
        titulo = ttk.Label(self.main_frame, text=texto, style='Title.TLabel')
        titulo.grid(row=0, column=0, sticky='w', pady=(0, 20))
        return titulo
    
    def criar_form_frame(self, row=1):
        """Cria um frame para formulário."""
        form_frame = ttk.Frame(self.main_frame)
        form_frame.grid(row=row, column=0, sticky='nsew')
        configurar_responsividade(form_frame)
        return form_frame
    
    def criar_campo(self, parent, label_text, row):
        """Cria um campo de entrada com label."""
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=0, sticky='ew', pady=8)
        configurar_responsividade(frame)
        
        lbl = ttk.Label(frame, text=label_text, style='Heading.TLabel')
        lbl.grid(row=0, column=0, sticky='w')
        
        entry = ttk.Entry(frame, font=FONTS['body'])
        entry.grid(row=1, column=0, sticky='ew', pady=(5, 0), ipady=5)
        
        return entry
    
    def criar_botao_frame(self, parent, row):
        """Cria frame para botões."""
        btn_frame = ttk.Frame(parent)
        btn_frame.grid(row=row, column=0, sticky='ew', pady=(20, 0))
        return btn_frame
    
    def limpar_campos(self, *entries):
        """Limpa os campos de entrada."""
        for entry in entries:
            entry.delete(0, tk.END)
    
    def mostrar_sucesso(self, mensagem):
        """Mostra mensagem de sucesso."""
        messagebox.showinfo("Sucesso", mensagem)
    
    def mostrar_erro(self, mensagem):
        """Mostra mensagem de erro."""
        messagebox.showerror("Erro", mensagem)
    
    def confirmar_acao(self, titulo, mensagem):
        """Solicita confirmação do usuário."""
        return messagebox.askyesno(titulo, mensagem)
