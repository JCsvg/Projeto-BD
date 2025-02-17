from src.models.clienteModel import ClienteModel
from src.models.compraModel import CompraModel
from src.models.estoqueModel import EstoqueModel
from src.models.pagamentoModel import PagamentoModel
from src.models.produtoModel import ProdutoModel
from src.models.vendedorModel import VendedorModel
from src.utils.view import View

class CompraMenu():

    @staticmethod
    def menu():
        print("Menu das Vendas")
        print("1 - Listar Vendas")
        print("2 - Cadastrar uma nova Venda")
        print("3 - Excluir o registro de uma Venda")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def init():
        while True:
            op = CompraMenu.menu()

            if op == 1:
                CompraMenu.listar_vendas()
            elif op == 2:
                CompraMenu.cadastrar_compra()
            elif op == 3:
                CompraMenu.remover_compra()
            elif op == 0:
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def listar_vendas():
        vendas = CompraModel.listar_compras()
        View.compra(vendas)
        input("Pressione Enter para continuar...")

    @staticmethod
    def cadastrar_compra():
        ls_vendedores = VendedorModel.listar_vendedores()
        ls_clientes = ClienteModel.listar_clientes()
        ls_produtos = ProdutoModel.listar_produtos()

        View.vendedor(ls_vendedores)
        id_vendedor = int(input("Digite o ID do Vendedor: "))
        vendedor = VendedorModel.procurar_vendedor(id_vendedor)
        if vendedor is None:
            print("Vendedor não existe")
            input("Pressione Enter para continuar...")
            return

        View.cliente(ls_clientes)
        id_cliente = int(input("Digite o ID do Cliente: "))
        cliente = ClienteModel.procurar_cliente_id(id_cliente)
        if cliente is None:
            print("Cliente inexistente")
            input("Pressione Enter para continuar...")
            return

        View.produto(ls_produtos)
        id_produto = int(input("Digite o ID do Produto: "))
        produto = ProdutoModel.procurar_por_id(id_produto)
        if produto is None:
            print("Produto não cadastrado")
            input("Pressione Enter para continuar...")
            return

        quantidade = int(input("Digite a quantidade: "))
        q_estoque = EstoqueModel.pesquisar_produto(id_produto)
        if quantidade <= 0 or quantidade > q_estoque[0]:
            print("Compra inválida")
            input("Pressione Enter para continuar...")
            return
        from datetime import datetime

        nova_qntd = q_estoque[0] - quantidade
        data = datetime.strptime(input("Digite a data da compra (dd/mm/aaaa): "), "%d/%m/%Y")
        valor_pago = quantidade * produto[3]
        CompraModel.cadastrar_compra(id_vendedor, id_cliente, id_produto, quantidade,valor_pago,data)
        EstoqueModel.alterar_quantidade(id_produto, nova_qntd)
        input("Pressione Enter para continuar...")

    @staticmethod
    def remover_compra():
        CompraMenu.listar_vendas()
        id = int(input("Digite o ID da venda: "))
        venda = CompraModel.pesquisar_compra(id)
        if venda is None:
            print("Venda não registrada")
            input("Pressione Enter para continuar...")
            return
        CompraModel.remover_compra(id)
        input("Pressione Enter para continuar...")