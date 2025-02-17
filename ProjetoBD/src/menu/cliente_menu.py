from src.models.clienteModel import ClienteModel
from src.utils.validation import validar_cliente_dados
from src.utils.view import View


class ClienteMenu():

    @staticmethod
    def init():
        while True:
            op = ClienteMenu.menu()

            if op == 1:
                ClienteMenu.cadastrar_cliente()
            elif op == 2:
                ClienteMenu.remover_cliente()
            elif op == 3:
                ClienteMenu.listar_clientes()
            elif op == 4:
                ClienteMenu.pesquisar_cliente()
            elif op == 5:
                ClienteMenu.compras_de_um_cliente()
            elif op == 6:
                ClienteMenu.alterar_dados()
            elif op == 0:
                break
            else:
                print("Opção Invalida!")


    @staticmethod
    def menu():
        print("Menu de clientes")
        print("1 - Cadastrar novo cliente")
        print("2 - Remover cliente")
        print("3 - Lista de clientes")
        print("4 - Pesquisar um cliente")
        print("5 - Listar todas as compras de um Cliente Expecífico")
        print("6 - Alterar dados de um Cliente")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao


    @staticmethod
    def listar_clientes():
        lista_clientes = ClienteModel.listar_clientes()
        View.cliente(lista_clientes)
        input("Pressione Enter para continuar...")

    @staticmethod
    def cadastrar_cliente():
        nome, telefone = validar_cliente_dados()
        ClienteModel.criar_cliente(nome, telefone)
        input("Pressione Enter para continuar...")

    @staticmethod
    def remover_cliente():
        ClienteMenu.listar_clientes()
        id = int(input("Digite o id do cliente que queira remover: "))
        ClienteModel.deletar_cliente(id)
        input("Pressione Enter para continuar...")

    @staticmethod
    def pesquisar_cliente():
        nome = input("Digite o nome do cliente: ")
        c = ClienteModel.procurar_cliente_nome(nome)
        View.cliente(c)
        input("Pressione Enter para continuar...")

    @staticmethod
    def compras_de_um_cliente():
        ClienteMenu.listar_clientes()
        id = int(input("Digite o ID do cliente: "))
        c = ClienteModel.procurar_cliente_id(id)
        if c:
            compras = ClienteModel.filtro_compras(id)
            View.filtro_compras_cliente(compras)
        else:
            print("Cliente n existe")
        input("Pressione Enter para continuar...")

    @staticmethod
    def alterar_dados():
        ClienteMenu.listar_clientes()
        id = int(input("Digite o ID do cliente: "))
        clinte = ClienteModel.procurar_cliente_id(id)
        if clinte:
            bool_nome = input("Deseja alterar o nome? (s/n): ").strip().lower() == "s"
            bool_telefone = input("Deseja alterar o telefone? (s/n): ").strip().lower() == "s"
            if bool_nome:
                nome = input("Digite o novo nome do cliente: ")
            else:
                nome = clinte[1]
            if bool_telefone:
                telefone = input("Digite o novo telefone do cliente: ")
            else:
                telefone = clinte[2]
            ClienteModel.alterar_dados(id, nome, telefone)
        else:
            print("Cliente não existe")
        input("Pressione Enter para continuar...")
