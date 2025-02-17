
def validar_cliente_dados(nome=None, telefone=None):
    while not nome or not telefone:
        print("Um dos dados não foi preenchido")
        if not nome:
            nome = input("Digite o nome: ").strip()
            nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not telefone:
            telefone = input("Digite o telefone: ").strip()
    return nome, telefone

def validar_produto_dados(nome=None, vr=None, vv=None, qntd=None):
    while not nome or not vr or not vv or not qntd or qntd < 0:
        if not nome:
            nome = input("Digite o nome do Produto: ").strip()
            nome = " ".join([parte.capitalize() for parte in nome.split()])
        if not vr:
            vr = float(input("Digite o valor pago no produto: "))
        if not vv:
            vv = float(input("Digite o valor que o produto sera vendido: "))
        if not qntd or qntd < 0:
            qntd = int(input("Digite a qunatidade disponível no estoque: "))
        return nome, vr, vv, qntd

def validar_operacao():
    while True:
        preco = float(input("Digite o preco de parametro"))
        if preco >= 0:
            break

    while True:
        print("Operações disponíveis")
        print(f"[0] -  Produtos com o preco maior ou igual a {preco}")
        print(f"[1]  -   Produtos com o preco maior que {preco}")
        print(f"[2]  -   Produtos com o preco igual a {preco}")
        print(f"[3]  -   Produtos com o preco menor que {preco}")
        print(f"[4] -  Produtos com o preco menor ou igual a {preco}")
        op = int(input("Digite a operação de comparação"))

        if op >= 0 or op <= 4:
            return preco, op
        print("Operação inválida")

