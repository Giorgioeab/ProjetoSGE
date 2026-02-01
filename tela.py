import tkinter as tk
from tkinter import ttk
from funcoes import *

def tela_cadastro(root):
    width=400
    heigth=400
    tela_cadastro = tk.Toplevel(root)
    tela_cadastro.title("Cadastro Genérico - Escola")
    tela_cadastro.geometry(f"{width}x{heigth}")

    abas = ttk.Notebook(tela_cadastro)
    abas.pack(fill="both", expand=True)

    aba_pessoas = ttk.Frame(abas)
    aba_cursos = ttk.Frame(abas)
    aba_turmas = ttk.Frame(abas)
    aba_aluno_turma = ttk.Frame(abas)

    abas.add(aba_pessoas, text="Cadastro de Pessoas")
    abas.add(aba_cursos, text="Cadastro de Cursos")
    abas.add(aba_turmas, text="Cadastro de Turmas")
    abas.add(aba_aluno_turma, text="Cadastro de Aluno em Turma")

    # Cadastrar Pessoas
    lbl_titulo_pessoas = tk.Label(aba_pessoas, text="Cadastro de Pessoas")
    lbl_titulo_pessoas.pack()

    # Label para mostrar status da verificação do CPF
    lbl_status_cpf = tk.Label(aba_pessoas, text="", font=("Arial", 9))
    
    def verificar_cpf():
        cpf = entry_cpf.get()
        if not cpf:
            lbl_status_cpf.config(text="Digite um CPF para verificar", fg="orange")
            return
        
        existe, msg = verificar_cpf_existe(cpf)
        if existe:
            lbl_status_cpf.config(text=f"✗ {msg}", fg="red")
        else:
            lbl_status_cpf.config(text=f"✓ {msg}", fg="green")

    # Implemente os campos para cadastrar pessoas
    lbl_cpf = tk.Label(aba_pessoas, text="CPF:")
    lbl_cpf.pack()
    
    frame_cpf = tk.Frame(aba_pessoas)
    frame_cpf.pack()
    entry_cpf = tk.Entry(frame_cpf, width=20)
    entry_cpf.pack(side=tk.LEFT, padx=(0, 5))
    btn_verificar_cpf = tk.Button(frame_cpf, text="Verificar", command=verificar_cpf)
    btn_verificar_cpf.pack(side=tk.LEFT)
    
    lbl_status_cpf.pack()
    
    lbl_nome = tk.Label(aba_pessoas, text="Nome:")
    lbl_nome.pack()
    entry_nome = tk.Entry(aba_pessoas)
    entry_nome.pack()

    lbl_data_nascimento = tk.Label(aba_pessoas, text="Data de Nascimento:")
    lbl_data_nascimento.pack()
    entry_data_nascimento = tk.Entry(aba_pessoas)
    entry_data_nascimento.pack()

    lbl_nome_mae = tk.Label(aba_pessoas, text="Nome da Mãe:")
    lbl_nome_mae.pack()
    entry_nome_mae = tk.Entry(aba_pessoas)
    entry_nome_mae.pack()

    lbl_email = tk.Label(aba_pessoas, text="Email:")
    lbl_email.pack()
    entry_email = tk.Entry(aba_pessoas)
    entry_email.pack()
    
    lbl_telefone = tk.Label(aba_pessoas, text="Telefone:")
    lbl_telefone.pack()
    entry_telefone = tk.Entry(aba_pessoas)
    entry_telefone.pack()

    def mostrar_janela_confirmacao(tipo, dados):
        """Mostra janela com os dados do cadastro realizado."""
        janela_info = tk.Toplevel(tela_cadastro)
        janela_info.title(f"Cadastro de {tipo} Realizado")
        janela_info.geometry("400x300")
        janela_info.grab_set()  # Torna a janela modal
        
        lbl_titulo = tk.Label(janela_info, text=f"✓ {tipo} cadastrado(a) com sucesso!", 
                              font=("Arial", 12, "bold"), fg="green")
        lbl_titulo.pack(pady=10)
        
        frame_dados = tk.Frame(janela_info)
        frame_dados.pack(pady=10, padx=20, fill="both", expand=True)
        
        labels = ["CPF:", "Nome:", "Data de Nascimento:", "Nome da Mãe:", "Email:", "Telefone:"]
        for i, (label, valor) in enumerate(zip(labels, dados)):
            tk.Label(frame_dados, text=label, font=("Arial", 10, "bold"), anchor="w").grid(row=i, column=0, sticky="w", pady=2)
            tk.Label(frame_dados, text=valor, anchor="w").grid(row=i, column=1, sticky="w", padx=10, pady=2)
        
        btn_ok = tk.Button(janela_info, text="OK", width=10, command=janela_info.destroy)
        btn_ok.pack(pady=20)

    def limpar_campos_pessoa():
        """Limpa todos os campos do formulário de pessoa."""
        entry_cpf.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_data_nascimento.delete(0, tk.END)
        entry_nome_mae.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        lbl_status_cpf.config(text="")

    def executar_cadastro_aluno():
        dados = (
            entry_cpf.get(),
            entry_nome.get(),
            entry_data_nascimento.get(),
            entry_nome_mae.get(),
            entry_email.get(),
            entry_telefone.get()
        )
        sucesso, msg = cadastrar_aluno(
            entry_nome.get(), 
            entry_cpf.get(), 
            entry_data_nascimento.get(), 
            entry_nome_mae.get(), 
            entry_email.get(), 
            entry_telefone.get()
        )
        if sucesso:
            limpar_campos_pessoa()
            mostrar_janela_confirmacao("Aluno", dados)
        else:
            from tkinter import messagebox
            messagebox.showerror("Erro", msg)

    def executar_cadastro_professor():
        dados = (
            entry_cpf.get(),
            entry_nome.get(),
            entry_data_nascimento.get(),
            entry_nome_mae.get(),
            entry_email.get(),
            entry_telefone.get()
        )
        sucesso, msg = cadastrar_professor(
            entry_nome.get(), 
            entry_cpf.get(), 
            entry_data_nascimento.get(), 
            entry_nome_mae.get(), 
            entry_email.get(), 
            entry_telefone.get()
        )
        if sucesso:
            limpar_campos_pessoa()
            mostrar_janela_confirmacao("Professor", dados)
        else:
            from tkinter import messagebox
            messagebox.showerror("Erro", msg)

    # Botões de cadastro de aluno e professor
    btn_cadastrar_aluno = tk.Button(
        aba_pessoas,
        text="Cadastrar Aluno", 
        command=executar_cadastro_aluno
        )
    btn_cadastrar_aluno.pack(padx=10)

    btn_cadastrar_professor = tk.Button(
        aba_pessoas, 
        text="Cadastrar Professor", 
        command=executar_cadastro_professor)
    btn_cadastrar_professor.pack(pady=10)

    # Cadastrar Cursos
    lbl_titulo_cursos = tk.Label(aba_cursos, text="Cadastro de Cursos")
    lbl_titulo_cursos.pack(pady=10)

    # Campos para cadastrar cursos
    lbl_nome_curso = tk.Label(aba_cursos, text="Nome do Curso:")
    lbl_nome_curso.pack()
    entry_nome_curso = tk.Entry(aba_cursos)
    entry_nome_curso.pack()

    lbl_duracao = tk.Label(aba_cursos, text="Duração:")
    lbl_duracao.pack()
    entry_duracao = tk.Entry(aba_cursos)
    entry_duracao.pack()

    lbl_turno = tk.Label(aba_cursos, text="Turno:")
    lbl_turno.pack()
    entry_turno = tk.Entry(aba_cursos)
    entry_turno.pack()

    # Botão de cadastro de curso
    btn_cadastrar_curso = tk.Button(aba_cursos,
                                    text="Cadastrar Curso", 
                                    command= lambda:cadastrar_curso(
                                        entry_nome_curso.get(),
                                        entry_turno.get(),
                                        entry_duracao.get()
                                    ))
    btn_cadastrar_curso.pack()

    # Cadastrar Turmas
    lbl_titulo_turmas = tk.Label(aba_turmas, text="Cadastro de Turmas",)
    lbl_titulo_turmas.pack()

    # Campos para cadastrar turmas
    lbl_nome_turma = tk.Label(aba_turmas, text="Nome do Curso:")
    lbl_nome_turma.pack()
    entry_nome_turma = tk.Entry(aba_turmas)
    entry_nome_turma.pack()

    lbl_professor_turma = tk.Label(aba_turmas, text="CPF do professor:")
    lbl_professor_turma.pack()
    entry_professor_turma = tk.Entry(aba_turmas)
    entry_professor_turma.pack()

    # Botão de cadastro de turma
    btn_cadastrar_turma = tk.Button(aba_turmas,
                                    text="Cadastrar Turma",
                                    command=lambda: cadastrar_turma(
                                        entry_nome_turma.get(),
                                        entry_professor_turma.get()
                                    ))
    btn_cadastrar_turma.pack()
    
    lbl_titulo_aluno_turma = tk.Label(aba_aluno_turma, text="Cadastro de Aluno em Turma")
    lbl_titulo_aluno_turma.pack()

    lbl_aluno_turma = tk.Label(aba_aluno_turma, text="Escolha o Aluno e a Turma:")
    lbl_aluno_turma.pack()

    # Campos para cadastrar aluno em turma
    lbl_aluno = tk.Label(aba_aluno_turma, text="Aluno:")
    lbl_aluno.pack()
    entry_aluno = tk.Entry(aba_aluno_turma)
    entry_aluno.pack()

    lbl_turma = tk.Label(aba_aluno_turma, text="Turma:")
    lbl_turma.pack()
    entry_turma = tk.Entry(aba_aluno_turma)
    entry_turma.pack()

    # Botão de cadastro de aluno em turma
    btn_cadastrar_aluno_turma = tk.Button(
        aba_aluno_turma, 
        text="Cadastrar Aluno em Turma",
        command=lambda: cadastrar_aluno_turma(
            entry_aluno.get(),
            entry_turma.get()
        ))
    btn_cadastrar_aluno_turma.pack()
    
    
    tela_cadastro.mainloop()

def tela_listagem(root, tipo_listagem):
    janela_listagem = tk.Toplevel(root)

    if tipo_listagem == "alunos":
        janela_listagem.title("Listagem de Alunos - Escola")
        dados = listar_alunos()
        
    elif tipo_listagem == "professores":
        janela_listagem.title("Listagem de Professores - Escola")
        dados = listar_professores()

    janela_listagem.geometry("800x400")

    tree = ttk.Treeview(janela_listagem)
    tree["columns"] = ("CPF", "Nome", "Data de Nascimento", "Nome da Mãe", "E-mail", "Telefone")

    # Definindo as colunas e seus títulos
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("CPF", anchor=tk.W, width=150)
    tree.column("Nome", anchor=tk.W, width=100)
    tree.column("Data de Nascimento", anchor=tk.W, width=150)
    tree.column("Nome da Mãe", anchor=tk.W, width=150)
    tree.column("E-mail", anchor=tk.W, width=200)
    tree.column("Telefone", anchor=tk.W, width=100)


    # Definindo os títulos das colunas
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("CPF", text="CPF", anchor=tk.W)
    tree.heading("Nome", text="Nome", anchor=tk.W)
    tree.heading("Data de Nascimento", text="Data de Nascimento", anchor=tk.W)
    tree.heading("Nome da Mãe", text="Nome da Mãe", anchor=tk.W)
    tree.heading("E-mail", text="E-mail", anchor=tk.W)
    tree.heading("Telefone", text="Telefone", anchor=tk.W)


    for pessoa in dados:
        tree.insert('', "end", values=pessoa)

    tree.pack(fill="both", expand=True)

def tela_listagem_cursos(root):
    janela_listagem = tk.Toplevel(root)
    janela_listagem.title("Listagem de Cursos - Escola")
    janela_listagem.geometry("800x400")

    tree = ttk.Treeview(janela_listagem)
    tree["columns"] = ("IdCurso", "NomeCurso", "Turno", "Duracao")

    # Definindo as colunas e seus títulos
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("IdCurso", anchor=tk.W, width=100)
    tree.column("NomeCurso", anchor=tk.W, width=200)
    tree.column("Turno", anchor=tk.W, width=100)
    tree.column("Duracao", anchor=tk.W, width=100)

    # Definindo os títulos das colunas
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("IdCurso", text="ID Curso", anchor=tk.W)
    tree.heading("NomeCurso", text="Nome do Curso", anchor=tk.W)
    tree.heading("Turno", text="Turno", anchor=tk.W)
    tree.heading("Duracao", text="Duração", anchor=tk.W)

    dados = listar_cursos()

    for curso in dados:
        tree.insert('', 'end', values=curso)
    
    tree.pack(fill="both", expand=True)

def tela_listagem_turmas(root):
    janela_listagem = tk.Toplevel(root)
    janela_listagem.title("Listagem de Turmas - Escola")
    janela_listagem.geometry("800x400")


    tree = ttk.Treeview(janela_listagem)
    tree["columns"] = ("ID Turma","ID Curso", "CPF Professor")

    # Definindo as colunas 
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("ID Turma", anchor=tk.W, width=150)
    tree.column("ID Curso", anchor=tk.W, width=150)
    tree.column("CPF Professor", anchor=tk.W, width=150)

    # Definindo os títulos das colunas
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("ID Turma", text="ID Turma", anchor=tk.W)
    tree.heading("ID Curso", text="ID Curso", anchor=tk.W)
    tree.heading("CPF Professor", text="CPF Professor", anchor=tk.W)
        
    dados = listar_turmas()

    for turma in dados:
        tree.insert('', 'end', values=turma)

    tree.pack(fill="both", expand=True)

def tela_alteracao(root):
    tela_alteracao = tk.Toplevel(root)
    tela_alteracao.title("Alteração de Pessoas - Escola")
    tela_alteracao.geometry("600x700")

    abas = ttk.Notebook(tela_alteracao)
    abas.pack(fill="both", expand=True)

    aba_pessoas = ttk.Frame(abas)

    abas.add(aba_pessoas, text="Alterar Pessoas")

    # Alterar Pessoas
    lbl_titulo_alteracao_pessoas = tk.Label(aba_pessoas, text="Alteração de Pessoas")
    lbl_titulo_alteracao_pessoas.pack()

    lbl_alteracao_pessoas = tk.Label(aba_pessoas, text="Escolha a pessoa que deseja alterar:")
    lbl_alteracao_pessoas.pack()

    # Implemente os campos para escolher a pessoa a ser alterada
    lbl_nome_pessoa = tk.Label(aba_pessoas, text="Nome da Pessoa:")
    lbl_nome_pessoa.pack()
    entry_nome_pessoa = tk.Entry(aba_pessoas)
    entry_nome_pessoa.pack()

    lbl_cpf_pessoa = tk.Label(aba_pessoas, text="CPF da Pessoa:")
    lbl_cpf_pessoa.pack()
    entry_cpf_pessoa = tk.Entry(aba_pessoas)
    entry_cpf_pessoa.pack()

    lbl_data_nascimento = tk.Label(aba_pessoas, text="Data de Nascimento:")
    lbl_data_nascimento.pack()
    entry_data_nascimento = tk.Entry(aba_pessoas)
    entry_data_nascimento.pack()

    lbl_nome_mae = tk.Label(aba_pessoas, text="Nome da Mãe:")
    lbl_nome_mae.pack()
    entry_nome_mae = tk.Entry(aba_pessoas)
    entry_nome_mae.pack()

    lbl_email = tk.Label(aba_pessoas, text="Email:")
    lbl_email.pack()
    entry_email = tk.Entry(aba_pessoas)
    entry_email.pack()
    
    lbl_telefone = tk.Label(aba_pessoas, text="Telefone:")
    lbl_telefone.pack()
    entry_telefone = tk.Entry(aba_pessoas)
    entry_telefone.pack()

    lbl_rg_pessoa = tk.Label(aba_pessoas, text="RG da Pessoa:")
    lbl_rg_pessoa.pack()
    entry_rg_pessoa = tk.Entry(aba_pessoas)
    entry_rg_pessoa.pack()

    # Botão de alterar pessoa
    btn_alterar_pessoa = tk.Button(aba_pessoas, 
                                   text="Alterar Pessoa",
                                   command=lambda:atualizar_pessoa(
                                    entry_nome_pessoa.get(), 
                                    entry_cpf_pessoa.get(), 
                                    entry_data_nascimento.get(), 
                                    entry_nome_mae.get(), 
                                    entry_email.get(), 
                                    entry_telefone.get()
                                   ))
    btn_alterar_pessoa.pack()

    tela_alteracao.mainloop()
     
def tela_exclusao(root):
    tela_exclusao = tk.Toplevel(root)
    tela_exclusao.title("Exclusão de Pessoas - Escola")
    tela_exclusao.geometry("400x200")

    lbl_titulo = tk.Label(tela_exclusao, text="Exclusão de Pessoa")
    lbl_titulo.pack()

    lbl_escolha_pessoa = tk.Label(tela_exclusao, text="Escolha a pessoa a ser excluída:")
    lbl_escolha_pessoa.pack()

    # Campos para escolher a pessoa a ser excluída
    lbl_nome_pessoa = tk.Label(tela_exclusao, text="Nome da Pessoa:")
    lbl_nome_pessoa.pack()
    entry_nome_pessoa = tk.Entry(tela_exclusao)
    entry_nome_pessoa.pack()

    lbl_cpf_pessoa = tk.Label(tela_exclusao, text="CPF da Pessoa:")
    lbl_cpf_pessoa.pack()
    entry_cpf_pessoa = tk.Entry(tela_exclusao)
    entry_cpf_pessoa.pack()

    # Label para mostrar resultado da exclusão
    lbl_resultado = tk.Label(tela_exclusao, text="", fg="green")
    lbl_resultado.pack(pady=10)

    def executar_exclusao():
        cpf = entry_cpf_pessoa.get()
        if not cpf:
            lbl_resultado.config(text="Por favor, informe o CPF.", fg="red")
            return
        
        sucesso, mensagem = excluir_pessoa(cpf)
        if sucesso:
            lbl_resultado.config(text=mensagem, fg="green")
            entry_nome_pessoa.delete(0, tk.END)
            entry_cpf_pessoa.delete(0, tk.END)
        else:
            lbl_resultado.config(text=mensagem, fg="red")

    # Botão para executar a exclusão da pessoa
    btn_excluir_pessoa = tk.Button(
        tela_exclusao, 
        text="Excluir Pessoa",
        command=executar_exclusao
    )
    btn_excluir_pessoa.pack()    

def tela_principal():
    
    root = tk.Tk()
    root.title("Escola - Tela Principal")
    root.geometry("400x400")

    lbl_titulo = tk.Label(root, text="Escola - Sistema de Cadastro")
    lbl_titulo.pack()

    btn_cadastro = tk.Button(root, text="Cadastro", command=lambda: tela_cadastro(root))
    btn_cadastro.pack()

    btn_listar_alunos = tk.Button(root, text="Listar Alunos", command=lambda: tela_listagem(root, "alunos"))
    btn_listar_alunos.pack()

    btn_listar_professores = tk.Button(root, text="Listar Professores", command=lambda: tela_listagem(root, "professores"))
    btn_listar_professores.pack()

    btn_listar_cursos = tk.Button(root, text="Listar Cursos", command=lambda: tela_listagem_cursos(root))
    btn_listar_cursos.pack()

    btn_listar_turmas = tk.Button(root, text="Listar Turmas", command=lambda: tela_listagem_turmas(root))
    btn_listar_turmas.pack()

    btn_atualizacao = tk.Button(root, text="Atualização", command=lambda: tela_alteracao(root))
    btn_atualizacao.pack()

    btn_exclusao = tk.Button(root, text="Exclusão", command=lambda: tela_exclusao(root))
    btn_exclusao.pack()

    root.mainloop()
    
if __name__ == "__main__":
    tela_principal()