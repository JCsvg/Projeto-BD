import datetime


class View:

    @staticmethod
    def cliente(cliente):
        largura_total = 50
        titulo = "Clientes"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'NOME':^25}|{'TELEFONE':^15}|")
        for c in cliente:
            print(f"|{str(c[0]):^6}|{c[1]:^25}|{c[2]:^15}|")

    @staticmethod
    def compra(compra):
        largura_total = 110
        titulo = "Compras"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'Vendedor':^25}|{'Cliente':^26}|{'Produto':^15}|{'Quantidade':^15}|{'Valor Pago':^15}|")
        for c in compra:
            print(f"|{str(c[0]):^6}|{str(c[1]):^25}|{str(c[2]):^26}|{str(c[3]):^15}|{str(c[4]):^15}|{str(c[5]):^15}|")

    @staticmethod
    def vendedor(vendedor):
        largura_total = 34
        titulo = "Vendedores"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'NOME':^25}|")
        for v in vendedor:
            print(f"|{str(v[0]):^6}|{v[1]:^25}|")

    @staticmethod
    def produto(produto):
        largura_total = 72
        titulo = "Produtos"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'NOME':^25}|{'Preço Real':^16}|{'Preço de Venda':^20}|")
        for p in produto:
            print(f"|{str(p[0]):^6}|{p[1]:^25}|{p[2]:^16}|{p[3]:^20}|")

    @staticmethod
    def estoque(estoque):
        largura_total = 82
        titulo = "Estoque"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'Nome':^25}|{'Quantidade':^15}|{'Preço Real':^16}|{'Preço de Venda':^20}|")
        for e in estoque:
            print(f"|{e[0]:^6}|{e[1]:^25}|{e[2]:^15}|{e[3]:^16}|{e[4]:^20}|")

    @staticmethod
    def pagamento(pagamento):
        largura_total = 54
        titulo = "Recibo"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID':^6}|{'ID da Compra':^15}|{'valor':^12}|{'Data da Compra':^16}|")
        for p in pagamento:
            data_formatada = p[3].strftime("%d/%m/%Y") if isinstance(p[3], datetime.date) else str(p[3])
            print(f"|{p[0]:^6}|{p[1]:^15}|{float(p[2]):^12.2f}|{data_formatada:^16}|")

    @staticmethod
    def filtro_compras_cliente(fcc):
        largura_total = 54
        titulo = f"Compras do Cliente {fcc[0][4]}"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID da Compra':^15}|{'NOME':^25}|{'valor':^12}|{'Data da Compra':^16}|")
        for c in fcc:
            data_formatada = c[3].strftime("%d/%m/%Y") if isinstance(c[3], datetime.date) else str(c[3])
            print(f"|{c[0]:^15}|{c[1]:^25}|{float(c[2]):^12.2f}|{data_formatada:^16}|")

    @staticmethod
    def filtro_produto_pagamento(fpp):
        largura_total = 74
        titulo = f"Recibos"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'Nome':^25}|{'ID da Compra':^15}|{'valor':^12}|{'Data da Compra':^16}|")
        for p in fpp:
            data_formatada = p[3].strftime("%d/%m/%Y") if isinstance(p[3], datetime.date) else str(p[3])
            print(f"|{p[0]:^25}|{p[1]:^15}|{float(p[2]):^12.2f}|{data_formatada:^16}|")

    @staticmethod
    def filtro_vendedor_vendas(fvv):
        largura_total = 80
        titulo = f"Vendas de {fvv[0][5]}"
        linha = "=" * ((largura_total - len(titulo)) // 2)
        print(f"{linha}{titulo}{linha}")
        print(f"|{'ID da Compra':^15}|{'Cliente':^25}|{'Produto':^15}|{'valor':^12}|{'Data da Compra':^16}|")
        for p in fvv:
            data_formatada = p[4].strftime("%d/%m/%Y") if isinstance(p[4], datetime.date) else str(p[4])
            print(f"|{p[0]:^15}|{p[1]:^25}|{p[2]:^15}|{float(p[3]):^12.2f}|{data_formatada:^16}|")