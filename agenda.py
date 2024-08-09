class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        fav = " (Favorito)" if self.favorito else ""
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}{fav}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def visualizar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. {contato}")

    def editar_contato(self, indice, nome=None, telefone=None, email=None):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            contato.nome = nome if nome else contato.nome
            contato.telefone = telefone if telefone else contato.telefone
            contato.email = email if email else contato.email
            print("Contato editado com sucesso!")
        else:
            print("Índice inválido.")

    def marcar_favorito(self, indice):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].favorito = not self.contatos[indice].favorito
            status = "favorito" if self.contatos[indice].favorito else "não favorito"
            print(f"Contato marcado como {status}.")
        else:
            print("Índice inválido.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            for contato in favoritos:
                print(contato)

    def apagar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            removido = self.contatos.pop(indice)
            print(f"Contato '{removido.nome}' removido com sucesso!")
        else:
            print("Índice inválido.")

def menu():
    agenda = Agenda()
    
    while True:
        print("\n--- AGENDA ---")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Listar Contatos Favoritos")
        print("6. Apagar Contato")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(nome, telefone, email)

        elif escolha == '2':
            agenda.visualizar_contatos()

        elif escolha == '3':
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja editar: ")) - 1
            nome = input("Novo Nome (deixe vazio para manter o atual): ")
            telefone = input("Novo Telefone (deixe vazio para manter o atual): ")
            email = input("Novo Email (deixe vazio para manter o atual): ")
            agenda.editar_contato(indice, nome, telefone, email)

        elif escolha == '4':
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
            agenda.marcar_favorito(indice)

        elif escolha == '5':
            agenda.listar_favoritos()

        elif escolha == '6':
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
            agenda.apagar_contato(indice)

        elif escolha == '7':
            print("Saindo da agenda...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
