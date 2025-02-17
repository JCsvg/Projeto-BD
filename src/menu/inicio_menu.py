from src.menu.cliente_menu import ClienteMenu
from src.menu.compra_menu import CompraMenu
from src.menu.estoque_menu import EstoqueMenu
from src.menu.pagamento_menu import PagamentoMenu
from src.menu.produto_menu import ProdutoMenu
from src.menu.vendedor_menu import VendedorMenu


class InicioMenu():

    @staticmethod
    def opcoes():
        print("Menu")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Vendedores")
        print("4 - Vendas")
        print("5 - Recibos")
        print("6 - Estoque")
        print("0 - Sair")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def init():
        while True:
            opcao = InicioMenu.opcoes()

            if opcao == 1:
                ClienteMenu.init()
            elif opcao == 2:
                ProdutoMenu.init()
            elif opcao == 3:
                VendedorMenu.init()
            elif opcao == 4:
                CompraMenu.init()
            elif opcao == 5:
                PagamentoMenu.init()
            elif opcao == 6:
                EstoqueMenu.init()
            elif opcao == 0:
                break
            else:
                print("Opção Invalida")
            input("Pressione Enter para continuar...")

