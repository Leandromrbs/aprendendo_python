# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    print("Contato adicionado com sucesso!")

# Função para exibir todos os contatos
def exibir_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos, start=1):
            print(f"Contato {i}:")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("-" * 20)

# Função principal
def main():
    contatos = []
    while True:
        print("1. Adicionar contato")
        print("2. Exibir contatos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            exibir_contatos(contatos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
