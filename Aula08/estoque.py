def adicionarProduto(listaProdutos, nome, preco, quantidade):
    produto = {
        "nome":nome,
        "preco":preco,
        "quantidade":quantidade
    }
    listaProdutos.append(produto)
    print(f'Produto adicionado com sucesso')

def listarProdutos(listaProdutos):
    for produto in listaProdutos:
        print('##################')
        print(f'Nome: {produto['nome']}')
        print(f'Preço: {produto['preco']}')
        print('##################')