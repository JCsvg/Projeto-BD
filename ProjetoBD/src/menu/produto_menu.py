from src.models.estoqueModel import EstoqueModel
from src.models.produtoModel import ProdutoModel
from src.utils.validation import validar_produto_dados
from src.utils.view import View

class ProdutoMenu:

    @staticmethod
    def init():
        while True:
            op = ProdutoMenu.menu()
            if op == 1:
                ProdutoMenu.listar_produtos()
            elif op == 2:
                ProdutoMenu.cadastrar_produto()
            elif op == 3:
                ProdutoMenu.remover_produto()
            elif op == 4:
                ProdutoMenu.filtrar_recibos()
            elif op == 5:
                ProdutoMenu.alterar_dados()
            elif op == 6:
                ProdutoMenu.pesquisar_preco_venda()
            elif op == 7:
                ProdutoMenu.pesquisar_preco_real()
            elif op == 0:
                break
            else:
                print("Opção inválida")


    @staticmethod
    def menu():
        print("Menu dos Produtos")
        print("1 - Listar Produtos cadastrados no sistema")
        print("2 - Cadastrar novo Produto")
        print("3 - Remover produto do Sistema")
        print("4 - Listar todas os recibos de um produto")
        print("5 - Alterar dados")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def listar_produtos():
        produtos = ProdutoModel.listar_produtos()
        View.produto(produtos)
        input("Pressione Enter para continuar...")

    @staticmethod
    def cadastrar_produto():
        nome, valor_real, valor_venda, qntd = validar_produto_dados()
        ProdutoModel.criar_produtos(nome, valor_real, valor_venda, qntd)
        input("Pressione Enter para continuar...")

    @staticmethod
    def remover_produto():
        produtos = ProdutoModel.listar_produtos()
        View.produto(produtos)
        id = int(input("Digite o ID do produto: "))
        ProdutoModel.remover_produto(id)
        input("Pressione Enter para continuar...")

    @staticmethod
    def filtrar_recibos():
        produtos = ProdutoModel.listar_produtos()
        View.produto(produtos)
        id = int(input("Digite o ID do produto: "))
        recibos = ProdutoModel.filtro_recibos_produto(id)
        if recibos:
            View.filtro_produto_pagamento(recibos)
        else:
            print("Não há compras com esse produto")
        input("Pressione Enter para continuar...")

    @staticmethod
    def alterar_dados():
        produtos = ProdutoModel.listar_produtos()
        View.produto(produtos)
        id = int(input("Digite o ID do produto: "))
        produto = ProdutoModel.procurar_por_id(id)
        if produto:
            bool_nome = input("Deseja alterar o nome? (s/n): ").strip().lower() == "s"
            bool_valor_real = input("Deseja alterar o valor pago nele? (s/n): ").strip().lower() == "s"
            bool_valor_venda = input("Deseja alterar o valor venda? (s/n): ").strip().lower() == "s"
            bool_qntd = input("Deseja alterar a quantidade disponivel? (s/n): ").strip().lower() == "s"
            produto_estoque = EstoqueModel.pesquisar_produto(id)
            if bool_nome:
                nome = input(f"Digite o novo nome do {produto[1]}: ")
            else:
                nome = produto[1]
            if bool_valor_real:
                valor_real = float(input(f"Digite o novo valor pago em : {nome}"))
            else:
                valor_real = produto[2]
            if bool_valor_venda:
                valor_venda = float(input(f"Digite o novo valor de venda do {nome}: "))
            else:
                valor_venda = produto[3]
            if bool_qntd:
                quantidade = int(input(f"Digite o quantidade do {nome}: "))
            else:
                quantidade = produto_estoque
            ProdutoModel.alterar_dados(id, nome, valor_real, valor_venda, quantidade)
        else:
            print("Produto não existe")
        input("Pressione Enter para continuar...")