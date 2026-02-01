# styles.py - Configurações de estilo e tema para o sistema SGE
import tkinter as tk
from tkinter import ttk

# Paleta de cores
COLORS = {
    'primary': '#2563eb',       # Azul principal
    'primary_dark': '#1d4ed8',  # Azul escuro (hover)
    'primary_light': '#3b82f6', # Azul claro
    'secondary': '#64748b',     # Cinza
    'success': '#22c55e',       # Verde
    'danger': '#ef4444',        # Vermelho
    'warning': '#f59e0b',       # Amarelo/Laranja
    'background': '#f8fafc',    # Fundo claro
    'surface': '#ffffff',       # Superfície branca
    'text_primary': '#1e293b',  # Texto principal
    'text_secondary': '#64748b', # Texto secundário
    'border': '#e2e8f0',        # Borda
}

# Fontes
FONTS = {
    'title': ('Segoe UI', 18, 'bold'),
    'subtitle': ('Segoe UI', 14, 'bold'),
    'heading': ('Segoe UI', 12, 'bold'),
    'body': ('Segoe UI', 10),
    'body_bold': ('Segoe UI', 10, 'bold'),
    'small': ('Segoe UI', 9),
    'button': ('Segoe UI', 10, 'bold'),
}

# Cache para evitar reconfiguração de estilos
_estilos_configurados = False

def configurar_estilos():
    """Configura os estilos ttk para toda a aplicação. Usa cache."""
    global _estilos_configurados
    
    if _estilos_configurados:
        return ttk.Style()
    
    style = ttk.Style()
    
    # Tentar usar tema mais moderno
    try:
        style.theme_use('clam')
    except:
        pass
    
    # Configurar fundo geral
    style.configure('.', 
                    background=COLORS['background'],
                    foreground=COLORS['text_primary'],
                    font=FONTS['body'])
    
    # Frame
    style.configure('TFrame', background=COLORS['background'])
    style.configure('Card.TFrame', background=COLORS['surface'], relief='flat')
    
    # Labels
    style.configure('TLabel', 
                    background=COLORS['background'],
                    foreground=COLORS['text_primary'],
                    font=FONTS['body'])
    
    style.configure('Title.TLabel',
                    font=FONTS['title'],
                    foreground=COLORS['primary'])
    
    style.configure('Subtitle.TLabel',
                    font=FONTS['subtitle'],
                    foreground=COLORS['text_primary'])
    
    style.configure('Heading.TLabel',
                    font=FONTS['heading'],
                    foreground=COLORS['text_primary'])
    
    style.configure('Success.TLabel',
                    foreground=COLORS['success'],
                    font=FONTS['body_bold'])
    
    style.configure('Error.TLabel',
                    foreground=COLORS['danger'],
                    font=FONTS['body_bold'])
    
    style.configure('Warning.TLabel',
                    foreground=COLORS['warning'],
                    font=FONTS['body_bold'])
    
    # Botões
    style.configure('TButton',
                    font=FONTS['button'],
                    padding=(20, 10))
    
    style.configure('Primary.TButton',
                    background=COLORS['primary'],
                    foreground='white',
                    font=FONTS['button'],
                    padding=(20, 10))
    
    style.map('Primary.TButton',
              background=[('active', COLORS['primary_dark']),
                         ('pressed', COLORS['primary_dark'])])
    
    style.configure('Success.TButton',
                    background=COLORS['success'],
                    foreground='white',
                    font=FONTS['button'],
                    padding=(20, 10))
    
    style.configure('Danger.TButton',
                    background=COLORS['danger'],
                    foreground='white',
                    font=FONTS['button'],
                    padding=(20, 10))
    
    style.configure('Secondary.TButton',
                    background=COLORS['secondary'],
                    foreground='white',
                    font=FONTS['button'],
                    padding=(15, 8))
    
    # Entry
    style.configure('TEntry',
                    padding=(10, 8),
                    font=FONTS['body'])
    
    # Notebook (abas)
    style.configure('TNotebook',
                    background=COLORS['background'],
                    tabmargins=[5, 5, 5, 0])
    
    style.configure('TNotebook.Tab',
                    font=FONTS['body_bold'],
                    padding=(15, 8),
                    background=COLORS['surface'])
    
    style.map('TNotebook.Tab',
              background=[('selected', COLORS['primary'])],
              foreground=[('selected', 'white')])
    
    # Treeview
    style.configure('Treeview',
                    font=FONTS['body'],
                    rowheight=30,
                    background=COLORS['surface'],
                    fieldbackground=COLORS['surface'])
    
    style.configure('Treeview.Heading',
                    font=FONTS['body_bold'],
                    background=COLORS['primary'],
                    foreground='white',
                    padding=(10, 5))
    
    style.map('Treeview',
              background=[('selected', COLORS['primary_light'])],
              foreground=[('selected', 'white')])
    
    _estilos_configurados = True
    return style


def centralizar_janela(janela, largura, altura):
    """Centraliza uma janela na tela."""
    janela.update_idletasks()
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = (screen_width - largura) // 2
    y = (screen_height - altura) // 2
    janela.geometry(f'{largura}x{altura}+{x}+{y}')


def configurar_responsividade(container, colunas=1, linhas=None):
    """Configura grid para ser responsivo."""
    for i in range(colunas):
        container.columnconfigure(i, weight=1)
    if linhas:
        for i in range(linhas):
            container.rowconfigure(i, weight=1)


class EntryComPlaceholder(ttk.Entry):
    """Entry com texto placeholder."""
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = COLORS['text_secondary']
        self.default_color = COLORS['text_primary']
        
        self.bind('<FocusIn>', self._on_focus_in)
        self.bind('<FocusOut>', self._on_focus_out)
        
        self._mostrar_placeholder()
    
    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.configure(foreground=self.default_color)
    
    def _on_focus_out(self, event):
        if not self.get():
            self._mostrar_placeholder()
    
    def _mostrar_placeholder(self):
        self.insert(0, self.placeholder)
        self.configure(foreground=self.placeholder_color)
    
    def get_value(self):
        """Retorna o valor real (não o placeholder)."""
        valor = self.get()
        return "" if valor == self.placeholder else valor


class CardFrame(ttk.Frame):
    """Frame estilizado como um card."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, style='Card.TFrame', **kwargs)
        self.configure(padding=20)
