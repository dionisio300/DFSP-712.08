def alertaPagemento(pagou):
    if(pagou == True):
        return 'O cliente já pagou'
    else:
        return 'O cliente ainda não pagou'

def alertaEstoque(qtd):
    if (qtd < 10):
        return 'Baixo estoque'
    elif (qtd <50):
        return 'Estoque ok'
    else:
        return 'Estoque suficiente, não comprar mais ainda'