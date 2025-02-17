from database.meubancoConnector import getConnection




class EstoqueModel:

    @staticmethod
    def adicionarProduto(produto_id, qntd):
        from src.models.produtoModel import ProdutoModel
        # Verifica se o produto existe
        produto = ProdutoModel.procurar_por_id(produto_id)
        if produto:
            # Se o produto existir, adiciona ao estoque
            con = getConnection()
            cursor = con.cursor()
            sql = "INSERT INTO ESTOQUE (produto_id, quantidade) VALUES (%s, %s)"
            cursor.execute(sql, (produto_id, qntd))
            con.commit()
            cursor.close()
            con.close()
            print("Produto adicionado ao estoque com sucesso!")
        else:
            print("Produto não encontrado. Não foi possível adicionar ao estoque.")

    @staticmethod
    def listarProdutos():
        con = getConnection()
        cursor = con.cursor()
        sql = """
        SELECT PRODUTO.produto_id, PRODUTO.NOME, QUANTIDADE, PRODUTO.preco_real, PRODUTO.preco_venda 
        FROM ESTOQUE 
        JOIN PRODUTO ON ESTOQUE.produto_id = PRODUTO.produto_id
        """
        cursor.execute(sql)
        estoque = cursor.fetchall()
        cursor.close()
        con.close()
        return estoque

    @staticmethod
    def alterar_quantidade(produto_id, quantidade):
        con = getConnection()
        cursor = con.cursor()
        sql = "UPDATE ESTOQUE SET quantidade = %s WHERE produto_id = %s"
        cursor.execute(sql, (quantidade, produto_id))
        con.commit()

        # Verificando a nova quantidade após a alteração
        sql = "SELECT quantidade FROM ESTOQUE WHERE produto_id = %s"
        cursor.execute(sql, (produto_id,))
        qnt_nova = cursor.fetchone()[0]
        print("Nova quantidade após update:", qnt_nova)

    @staticmethod
    def pesquisar_produto(produto_id):
        con = getConnection()
        cursor = con.cursor()
        sql = "SELECT quantidade FROM ESTOQUE WHERE produto_id = %s"
        cursor.execute(sql, (produto_id,))
        quantidade = cursor.fetchone()
        con.close()
        cursor.close()
        return quantidade
