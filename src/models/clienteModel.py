from database.meubancoConnector import getConnection

class ClienteModel:

    @staticmethod
    def criar_cliente(nome,telefone):
        con = getConnection()
        cursor = con.cursor()
        sql = "INSERT INTO CLIENTE (nome, telefone) VALUES (%s, %s)"
        val = (nome, telefone)
        cursor.execute(sql, val)
        con.commit()
        cursor.close()
        con.close()
        print(f"{nome} cadastrado com sucesso!")

    @staticmethod
    def listar_clientes():
        con = getConnection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM CLIENTE")
        resultados = cursor.fetchall()
        cursor.close()
        con.close()
        return resultados

    @staticmethod
    def procurar_cliente_nome(nome):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM CLIENTE WHERE nome LIKE %s"
        val = (f"%{nome}%",)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def procurar_cliente_id(id_cliente):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM CLIENTE WHERE cliente_id = %s"
        val = (str(id_cliente),)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def alterar_dados(id, nome, telefone):
        con = getConnection()
        cursor = con.cursor()
        sql = "UPDATE CLIENTE SET nome = %s, telefone = %s WHERE cliente_id = %s"
        val = (nome, telefone, id)
        cursor.execute(sql, val)
        con.commit()
        cursor.close()
        con.close()

    @staticmethod
    def deletar_cliente(cliente_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "DELETE FROM CLIENTE WHERE cliente_id = %s"
        val = (str(cliente_id),)
        cursor.execute(sql, val)
        con.commit()
        cursor.close()
        con.close()

    @staticmethod
    def filtro_compras(cliente_id):
        con = getConnection()
        cursor = con.cursor()
        sql = """
        SELECT COMPRA.compra_id, PRODUTO.nome, COMPRA.valor_pago, PAGAMENTO.data_pagamento, CLIENTE.nome
        FROM COMPRA
        JOIN PRODUTO ON PRODUTO.produto_id = COMPRA.produto_id
        JOIN PAGAMENTO ON PAGAMENTO.compra_id = COMPRA.compra_id
        JOIN CLIENTE ON CLIENTE.cliente_id = COMPRA.cliente_id
        WHERE COMPRA.cliente_id = %s
        """
        val = (str(cliente_id),)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado