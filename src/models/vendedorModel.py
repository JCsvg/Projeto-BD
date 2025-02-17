from database.meubancoConnector import getConnection

class VendedorModel:

    @staticmethod
    def cadastrar_vendedor(nome_vendedor):
        con = getConnection()
        cursor = con.cursor()
        sql = "INSERT INTO VENDEDOR (nome) VALUES (%s)"
        cursor.execute(sql, (nome_vendedor,))
        con.commit()
        cursor.close()
        con.close()
        print(f"{nome_vendedor} cadastrado com sucesso!")

    @staticmethod
    def listar_vendedores():
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM VENDEDOR"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def procurar_vendedor(vendedor_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM VENDEDOR WHERE vendedor_id = %s"
        cursor.execute(sql, (vendedor_id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def deletar_vendedor(vendedor_id):
        con = getConnection()
        cursor = con.cursor()
        vendedor = VendedorModel.procurar_vendedor(vendedor_id)
        sql = "DELETE FROM VENDEDOR WHERE vendedor_id = %s"
        cursor.execute(sql, (vendedor_id,))
        con.commit()
        cursor.close()
        con.close()
        print(f"{vendedor[1]} demitido com sucesso :(")

    @staticmethod
    def alterar_dados(nome, vendedor_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "UPDATE VENDEDOR SET nome = %s WHERE vendedor_id = %s"
        cursor.execute(sql, (nome, vendedor_id,))
        con.commit()
        cursor.close()
        con.close()
        print(f"Dados de {nome} alterado com sucesso!")

    @staticmethod
    def filtro_vendas(vendedor_id):
        con = getConnection()
        cursor = con.cursor()
        sql = """
        SELECT COMPRA.compra_id, CLIENTE.nome, PRODUTO.nome, COMPRA.valor_pago, PAGAMENTO.data_pagamento, VENDEDOR.nome 
        FROM COMPRA
        JOIN CLIENTE ON CLIENTE.cliente_id = COMPRA.cliente_id
        JOIN PRODUTO ON PRODUTO.produto_id = COMPRA.produto_id
        JOIN PAGAMENTO ON PAGAMENTO.compra_id = COMPRA.compra_id
        JOIN VENDEDOR ON VENDEDOR.vendedor_id = COMPRA.vendedor_id
        WHERE COMPRA.vendedor_id = %s
        """
        cursor.execute(sql, (vendedor_id,))
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado