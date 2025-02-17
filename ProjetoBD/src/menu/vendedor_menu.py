from src.models.vendedorModel import VendedorModel
from src.utils.view import View

class VendedorMenu:

    @staticmethod
    def menu():
        print("Menu do Vendedor")
        print("1 - Listar Vendedores")
        print("2 - Cadastrar Vendedor")
        print("3 - Demitir Vendedor")
        print("4 - Alterar dados de um Vendedor")
        print("5 - Listar vendas de um Vendedor")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def init():
        while True:
            op = VendedorMenu.menu()
            if op == 1:
                VendedorMenu.listar_vendedores()
            elif op == 2:
                VendedorMenu.cadastrar_vendedor()
            elif op == 3:
                VendedorMenu.demitir_vendedor()
            elif op == 4:
                VendedorMenu.alterar_dados()
            elif op == 5:
                VendedorMenu.listar_vendas()
            elif op == 0:
                break
            else:
                print("Opção invalida")

    @staticmethod
    def listar_vendedores():
        vendedores = VendedorModel.listar_vendedores()
        View.vendedor(vendedores)
        input("Pressione Enter para continuar...")

    @staticmethod
    def cadastrar_vendedor():
        nome = input("Nome do Vendedor: ")
        VendedorModel.cadastrar_vendedor(nome)
        input("Pressione Enter para continuar...")

    @staticmethod
    def demitir_vendedor():
        VendedorMenu.listar_vendedores()
        id = int(input("Id do Vendedor: "))
        v = VendedorModel.procurar_vendedor(id)
        if v:
            VendedorModel.deletar_vendedor(id)
        else:
            print("Vendedor não existe")
        input("Pressione Enter para continuar...")

    @staticmethod
    def alterar_dados():
        VendedorMenu.listar_vendedores()
        id = int(input("Id do Vendedor: "))
        v = VendedorModel.procurar_vendedor(id)
        if v:
            nome = input("Digite o novo nome do Vendedor: ")
            VendedorModel.alterar_dados(nome, id)
        else:
            print("Vendedor não cadastrado")
        input("Pressione Enter para continuar...")

    @staticmethod
    def listar_vendas():
        VendedorMenu.listar_vendedores()
        id = int(input("Id do Vendedor: "))
        v = VendedorModel.procurar_vendedor(id)
        if v:
            vendas = VendedorModel.filtro_vendas(id)
            View.filtro_vendedor_vendas(vendas)
        else:
            print("Vendedor não existe")
        input("Pressione Enter para continuar...")