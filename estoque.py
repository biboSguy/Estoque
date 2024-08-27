def produtos():
    print("Estoque:")
    while True:
        try:        
            nomeProduto = (input("Qual o nome do produto?: "))
            if len(nomeProduto) == 0:
                print("Coloque valores validos.")
                continue
            valorProduto = (input("Qual o valor do produto?: "))
            if len(valorProduto) == 0:
                print("Coloque valores validos.")
                continue
            valorProduto = float(valorProduto)
            quantidadeProduto = (input("Qual a quantidade do produto?: "))
            if len(quantidadeProduto) == 0:
                print("Coloque valores validos.")
                continue
            quantidadeProduto = float(quantidadeProduto)
            valorEstoque = (valorProduto*quantidadeProduto)
            print("Nome:",nomeProduto,"| Valor:",valorProduto, "| Quantidade",quantidadeProduto)
            print("Valor de estoque total: ",valorEstoque)
            break
        except ValueError:
            break
produtos()