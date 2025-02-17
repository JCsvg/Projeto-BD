from database.meubancoConnector import getConnection

from src.models.estoqueModel import EstoqueModel


class ProdutoModel:

    @staticmethod
    def criar_produtos(nome, preco_real, preco_venda, quantidade):
        con = getConnection()
        cursor = con.cursor()
        sql = "INSERT INTO PRODUTO (nome, preco_real, preco_venda) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, float(preco_real), float(preco_venda)))  # Converte para float
        con.commit()
        cursor.execute("SELECT MAX(produto_id) FROM PRODUTO")
        produto_id = cursor.fetchone()[0]
        EstoqueModel.adicionarProduto(produto_id, quantidade)
        cursor.close()
        con.close()
        print(f"{nome} cadastrado com sucesso!")

    @staticmethod
    def listar_produtos():
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM PRODUTO"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        con.close()
        return resultados

    @staticmethod
    def procurar_por_nome(nome):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM PRODUTO WHERE nome LIKE %s"  # Mantemos o LIKE para busca parcial
        val = (f"%{nome}%",)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def procurar_por_id(produto_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM PRODUTO WHERE produto_id = %s"
        cursor.execute(sql, (produto_id,))
        produto = cursor.fetchone()
        cursor.close()
        con.close()
        return produto

    @staticmethod
    def alterar_dados(produto_id, nome, preco_real, preco_venda, qntd):
        con = getConnection()
        cursor = con.cursor()
        produto = ProdutoModel.procurar_por_id(produto_id)
        if produto:
            sql = "UPDATE PRODUTO SET nome = %s, preco_real = %s, preco_venda = %s WHERE produto_id = %s"
            cursor.execute(sql, (nome, preco_real, preco_venda, produto_id))
            con.commit()
            EstoqueModel.alterar_quantidade(produto_id, qntd)
            cursor.close()
            con.close()
            print(f"Dados de {nome} alterado com sucesso!")

    @staticmethod
    def remover_produto(produto_id):
        con = getConnection()
        cursor = con.cursor()
        produto = ProdutoModel.procurar_por_id(produto_id)
        if produto:
            sql = "DELETE FROM PRODUTO WHERE produto_id = %s"
            cursor.execute(sql, (produto_id,))
            con.commit()
            cursor.close()
            con.close()
            print(f"{produto[1]} removido com sucesso!")
        else:
            print("Produto não existe")

    @staticmethod
    def filtro_recibos_produto(produto_id):
        con = getConnection()
        cursor = con.cursor()
        produto = ProdutoModel.procurar_por_id(produto_id)
        if produto:
            sql = """
            SELECT PRODUTO.nome, COMPRA.compra_id, PAGAMENTO.valor_pago, PAGAMENTO.data_pagamento
            FROM PRODUTO
            JOIN COMPRA ON PRODUTO.produto_id = COMPRA.produto_id
            JOIN PAGAMENTO ON COMPRA.compra_id = PAGAMENTO.compra_id
            WHERE PRODUTO.produto_id = %s
            """
            cursor.execute(sql, (produto_id,))
            resultados = cursor.fetchall()
            cursor.close()
            con.close()
            return resultados
        else:
            print("Produto não existe")