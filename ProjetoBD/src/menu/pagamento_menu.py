from src.models.pagamentoModel import PagamentoModel
from src.utils.view import View

class PagamentoMenu():

    @staticmethod
    def menu():
        print("Menu de Recibos")
        print("1 - Listar Recibos")
        print("0 - Voltar")
        opcao = int(input("Digite uma opção\n[ ]:"))
        return opcao

    @staticmethod
    def init():
        while True:
            op = PagamentoMenu.menu()

            if op == 1:
                PagamentoMenu.listar()
            elif op == 0:
                break
            else:
                print("Opção invalida")

    @staticmethod
    def listar():
        ls = PagamentoModel.listar_pagamentos()
        View.pagamento(ls)
        input("Pressione Enter para continuar...")
