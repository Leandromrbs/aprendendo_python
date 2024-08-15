import flet as ft
import sqlite3

# Função para criar a tabela de contatos no banco de dados
def criar_tabela():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um novo contato ao banco de dados
def adicionar_contato(nome, telefone, email):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, telefone, email)
        VALUES (?, ?, ?)
    ''', (nome, telefone, email))
    conn.commit()
    conn.close()

# Função para buscar todos os contatos do banco de dados
def buscar_contatos():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, telefone, email FROM contatos')
    contatos = cursor.fetchall()
    conn.close()
    return contatos

def main(page: ft.Page):
    criar_tabela()

    # Função para adicionar um novo contato e atualizar a lista
    def adicionar_contato_click(e):
        nome = nome_input.value
        telefone = telefone_input.value
        email = email_input.value
        adicionar_contato(nome, telefone, email)
        nome_input.value = ""
        telefone_input.value = ""
        email_input.value = ""
        exibir_contatos()

    # Função para exibir todos os contatos
    def exibir_contatos():
        contatos_list.controls.clear()
        contatos = buscar_contatos()
        for contato in contatos:
            contatos_list.controls.append(
                ft.Text(f"Nome: {contato[0]}, Telefone: {contato[1]}, Email: {contato[2]}")
            )
        page.update()

    # Componentes da interface
    nome_input = ft.TextField(label="Nome")
    telefone_input = ft.TextField(label="Telefone")
    email_input = ft.TextField(label="Email")
    adicionar_button = ft.ElevatedButton(text="Adicionar Contato", on_click=adicionar_contato_click)
    contatos_list = ft.Column()

    # Adicionando componentes à página
    page.add(
        nome_input,
        telefone_input,
        email_input,
        adicionar_button,
        contatos_list
    )

    # Exibir contatos ao iniciar o aplicativo
    exibir_contatos()

# Executando o aplicativo
ft.app(target=main)
