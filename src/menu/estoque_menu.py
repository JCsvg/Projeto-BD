from src.models.estoqueModel import EstoqueModel
from src.utils.view import View


class EstoqueMenu():

    @staticmethod
    def menu():
        print("Menu do Estoque")
        print("1 - Listar produtos no estoque")
        print("2 - Alterar estoque de um produto")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def init():
        while True:
            op = EstoqueMenu.menu()

            if op == 1:
                EstoqueMenu.listar_estoque()
            elif op == 2:
                EstoqueMenu.alterar_estoque()
            elif op == 0:
                break
            else:
                print("Opcao invalida")

    @staticmethod
    def listar_estoque():
        ls_estoque = EstoqueModel.listarProdutos()
        View.estoque(ls_estoque)
        input("Pressione Enter para continuar...")

    @staticmethod
    def alterar_estoque():
        EstoqueMenu.listar_estoque()
        id = int(input("Informe o id do Produto: "))
        estoque = EstoqueModel.pesquisar_produto(id)

        if estoque is None:
            print("Produto não cadastrado")
            input("Pressione Enter para continuar...")
            return
        quantidade = int(input("Informe a quantidade do produto: "))
        if quantidade < 0:
            print("Quantidade inválida")
            input("Pressione Enter para continuar...")
            return
        EstoqueModel.alterar_quantidade(id, quantidade)
        input("Pressione Enter para continuar...")
