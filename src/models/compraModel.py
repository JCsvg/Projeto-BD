from database.meubancoConnector import getConnection

from src.models.pagamentoModel import PagamentoModel


class CompraModel:

    @staticmethod
    def listar_compras():
        con = getConnection()
        cursor = con.cursor()
        sql = """
        SELECT compra_id, VENDEDOR.nome, CLIENTE.nome, PRODUTO.nome, quantidade, valor_pago 
        FROM COMPRA 
        JOIN VENDEDOR ON VENDEDOR.vendedor_id = COMPRA.vendedor_id 
        JOIN CLIENTE ON CLIENTE.cliente_id = COMPRA.cliente_id 
        JOIN PRODUTO ON PRODUTO.produto_id = COMPRA.produto_id

        """
        cursor.execute(sql)
        compras = cursor.fetchall()
        return compras

    @staticmethod
    def cadastrar_compra(vendedor_id, cliente_id, produto_id, quantidade, valor_pago, data):
        con = getConnection()
        cursor = con.cursor()
        sql = """
            INSERT INTO COMPRA (vendedor_id, cliente_id, produto_id, quantidade, valor_pago) 
            VALUES (%s, %s, %s, %s, %s)
        """
        val = (vendedor_id, cliente_id, produto_id, quantidade, valor_pago)
        cursor.execute(sql, val)
        con.commit()
        sql = "SELECT MAX(compra_id) FROM COMPRA"
        cursor.execute(sql)
        compras = cursor.fetchall()
        PagamentoModel.criar_pagamento(compras[0][0], data)

        cursor.close()
        con.close()
        print("Venda cadastrada com sucesso!")

    @staticmethod
    def pesquisar_compra(compra_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM COMPRA WHERE compra_id = %s"
        cursor.execute(sql, (compra_id,))
        compra = cursor.fetchone()
        cursor.close()
        con.close()
        return compra

    @staticmethod
    def remover_compra(compra_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "DELETE FROM COMPRA WHERE compra_id = %s"
        cursor.execute(sql, (compra_id,))
        con.commit()
        cursor.close()
        con.close()
        print("Venda removida com sucesso!")

