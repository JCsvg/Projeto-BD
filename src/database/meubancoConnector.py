import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host="SEU_HOST",        # Ex: "localhost" ou "127.0.0.1"
        database="NOME_BANCO",  # Ex: "loja"
        user="SEU_USUARIO",     # Ex: "root"
        passwd="SUA_SENHA"      # Ex: "senha_segura"
    )