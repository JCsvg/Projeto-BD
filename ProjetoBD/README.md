# Loja de Software

## Descrição  
Sistema de gerenciamento de loja de software com funcionalidades para:  
- Cadastro, atualização, remoção e consulta de Clientes, Produtos, Vendedores, Compras, Pagamentos e Estoque.  
- Relatórios avançados utilizando JOINs para análise de compras e vendas.  

## Funcionalidades  
- Gerenciamento de Clientes: Cadastro, consulta por nome ou ID, atualização e exclusão.  
- Gerenciamento de Produtos: Cadastro, atualização de estoque, consulta e exclusão.  
- Controle de Vendas e Pagamentos: Registro de compras e pagamentos com relatórios detalhados.  
- Relatórios: Consultas avançadas para análise de vendas e estoque.  

## Estrutura do Projeto  
```md
  projetoBD/
  ├── src/
  │   ├── database/
  │   │   └── meubancoConnector.py  # Conexão com o banco MySQL
  │   ├── models/                   # Modelos das tabelas (Cliente, Produto, etc.)
  │   ├── menu/                     # Menus para navegação
  │   ├── utils/                    # Validações e visualizações
  │   └── main.py                   # Inicialização do sistema
  └── README.md                     # Documentação do projeto
  └── DATABASE.md                   # Documentação do Banco de Dados
  └── HELP.md                       # Instruções de uso do sistema
````

## Tecnologias Utilizadas

- Linguagem: Python
- Banco de Dados: MySQL
- Bibliotecas: `mysql.connector` para conexão com o banco de dados.

## Instalação e Execução

1. Instale as dependências com:
    
    ```bash
    pip install mysql-connector-python
    ```
    
2. Configure o banco de dados em `meubancoConnector.py`.
```python
import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host="SEU_HOST",        # Ex: "localhost" ou "127.0.0.1"
        database="NOME_BANCO",  # Ex: "loja"
        user="SEU_USUARIO",     # Ex: "root"
        passwd="SUA_SENHA"      # Ex: "senha_segura"
    )
```
3. Execute o sistema com:
    
    ```bash
    python src/main.py
    ```
    
