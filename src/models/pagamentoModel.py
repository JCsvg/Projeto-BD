from database.meubancoConnector import getConnection

class PagamentoModel:

    @staticmethod
    def listar_pagamentos():
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT * FROM PAGAMENTO"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado

    @staticmethod
    def get_valor_compra(compra_id):
        """
        Retorna o valor da compra com base no compra_id.
        """
        con = getConnection()
        cursor = con.cursor()
        cursor.execute("SELECT valor_pago FROM COMPRA WHERE compra_id = %s", (compra_id,))
        resultado = cursor.fetchone()
        cursor.close()
        con.close()
        return resultado[0] if resultado else None

    @staticmethod
    def criar_pagamento(compra_id, data_pagamento):
        """
        Cria um pagamento com valor_pago auto-completado.
        """
        valor_pago = PagamentoModel.get_valor_compra(compra_id)
        if valor_pago is None:
            raise ValueError("Compra não encontrada!")

        con = getConnection()
        cursor = con.cursor()
        sql = "INSERT INTO PAGAMENTO (compra_id, valor_pago, data_pagamento) VALUES (%s, %s, %s)"
        valores = (compra_id, valor_pago, data_pagamento)
        cursor.execute(sql, valores)
        con.commit()
        cursor.close()
        con.close()
        print("Pagamento criado com sucesso!")