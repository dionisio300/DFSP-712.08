# Lista de dicionários

#função
def saudar():
    print('Seja bem-vindo usuário!!!')


listaPosts = [
    {
        "nome":"Maria",
        "descricao":"Foto de hoje",
        "foto":"https://www.toureiffel.paris/sites/default/files/styles/400x700/public/2025-08/hp_400x700_fmichel.jpg",
        "qtdLike":50,
        "qtdComent":30,
        "qtdComp":10
    },{
        "nome":"João",
        "descricao":"Viagem",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":60,
        "qtdComent":10,
        "qtdComp":15
    },{
        "nome":"Jessica",
        "descricao":"Passeio",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":70,
        "qtdComent":50,
        "qtdComp":35
    }
]

# listaNomes = ['Carlos','Jessica']

# pessoa = {'nome':'Letícia', 'idade':28}
# print(pessoa["idade"])
# print(listaNomes[1])
# print(listaPosts[0]["nome"])

# post = {}

# post['nome'] = input('Digite seu nome: ')
# post['descricao'] = input('Digite a descrição: ')
# post['foto'] = input('Digite a url da foto: ')
# post['qtdLike'] = int(input('Digite a quantidad de like: '))
# post['qtdComent'] = int(input('Digite a quantidad de comentários: '))
# post['qtdComp'] = int(input('Digite a quantidade de compartilhamentos: '))

# listaPosts.append(post)

# print(listaPosts)

# listaNumeros = [1,2,3,5,12,312,31325,5643,5756,234]


# for numero in listaNumeros:
#     print(f'Número: {numero}')

# print('Pessoas que postaram:')
# for post in listaPosts:
#     if post["qtdLike"] > 50:
#         print(f'Nome: {post["nome"]}')
#         print(f'Foto: {post["foto"]}')
#         print(f'----------------------------------')

# 1. Crie um programa que percorra uma lista de dicionário que represanta as postagens em uma rede social e mostre o total de likes somando a quantidade de likes de todas as postagens.

# somaLikes = 0
# for post in listaPosts:
#     somaLikes = somaLikes + post['qtdLike']
# print(f'Total de likes = {somaLikes}')

# 2. Crie um programa que percorra a lista de posts e mostre o nome a descrição e a foto apenas das postagens que tiverem mais que 20 comentários

# for post in listaPosts:
#     if post['qtdComent'] > 20:
#         print(f'Nome: {post['nome']}\nDescrição: {post['descricao']}\nFoto: {post['foto']}')

# 3. crie um programa que analise as postagens dos usuários e calcule o engajamento, que é a soma de comentários, curtidas e compartilhamento. Mostre depois o post com maior engajamento.

# for post in listaPosts:
#     engajamento = post['qtdComent']+post["qtdLike"]+post["qtdComp"]
#     post['engajamento'] = engajamento

# maiorEngajamento = 0

# for post in listaPosts:
#     if post['engajamento'] > maiorEngajamento:
#         maiorEngajamento = post['engajamento']

# print(maiorEngajamento)

# maiorEngajamento = 0

# for post in listaPosts:
#     engajamento = post['qtdComent']+post["qtdLike"]+post["qtdComp"]
#     post['engajamento'] = engajamento
#     if post['engajamento'] > maiorEngajamento:
#         maiorEngajamento = post['engajamento']

# print(maiorEngajamento)


# Funções

listaPosts2 = [
    {
        "nome":"Ana",
        "descricao":"Foto de hoje",
        "foto":"https://www.toureiffel.paris/sites/default/files/styles/400x700/public/2025-08/hp_400x700_fmichel.jpg",
        "qtdLike":50,
        "qtdComent":30,
        "qtdComp":10
    },{
        "nome":"Caio",
        "descricao":"Viagem",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":60,
        "qtdComent":10,
        "qtdComp":15
    },{
        "nome":"Letícia",
        "descricao":"Passeio",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":100,
        "qtdComent":70,
        "qtdComp":50
    }
]

#função sem parâmetros e sem retorno
# def saudar():
#     print('Seja bem-vindo usuário!!!')
saudar()

# função com parâmetros
def saudarUsuario(nome):
    print(f'Seja bem-vindo(a) {nome}')

# for post in listaPosts:
#     saudarUsuario(post['nome'])

def somarNumeros(num1, num2):
    soma = num1 + num2
    print(soma)

somarNumeros(7,8)

def calculadora(operacao, num1, num2):
    if operacao == '+':
        print(num1 + num2)
    elif operacao == '-':
        print(num1 - num2)
    elif operacao == '*':
        print(num1 * num2)
    elif operacao == '/':
        print(num1/num2)
    else:
        print('Operação não encontrada')


resultado = calculadora('+',4,5)

print(resultado)

# Funções com retorno
def calculadora(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return (num1 - num2)
    elif operacao == '*':
        return (num1 * num2)
    elif operacao == '/':
        return (num1/num2)
    else:
        return ('Operação não encontrada')


print('Função com retorno')
resultado = calculadora('*',2,5) #10

bonus = 100 *  resultado
print(f'Seu bonus foi de {bonus}')


def maiorEngajamento(listaPosts):
    mEngajamento = 0
    for post in listaPosts:
        engajamento = post['qtdComent']+post["qtdLike"]+post["qtdComp"]
        post['engajamento'] = engajamento
        if post['engajamento'] > mEngajamento:
            mEngajamento = post['engajamento']
    return (mEngajamento)

maiorEng = maiorEngajamento(listaPosts)
print(maiorEng)

maiorEng = maiorEngajamento(listaPosts2)
print(maiorEng)