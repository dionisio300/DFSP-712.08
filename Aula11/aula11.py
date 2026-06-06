# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install supabase
# pip install python-dotenv
# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env
'''
1 - Crie uma tabela chamada produtos no supabase que deve ter:
id
nome
preco
quantidade
criado_em
descriacao
2 - Insira manualmente 3 produtos diretamente pelo supabase
3 - Cria uma função para mostrar o nome o preço e a descrição dos produtos com preço maior que 100 reais
4 - Crie uma função que receba como parâmetros o nome, preço, quantidade e descrição, e faça o cadastro de um novo produto no banco de dados
5 - Crie uma função que receba como parâmetro o ID e o novo preço de um produto, e a função deve atualizar o preço desse produto
6 - Crie uma função que receba o ID de um produto e delete ele do banco de dados
'''

# def cadastrarProduto(nome,preco,quantidade,descricao):
#     print(nome, preco, quantidade,descricao)


#3 - Cria uma função para mostrar o nome o preço e a descrição dos produtos com preço maior que 100 reais
# def mostrarProdutos():
#     resposta = supabase.table('produtos').select("nome, preco, descricao").gt('preco',100).execute()
#     resposta = resposta.data
#     return resposta

# Utilize as funções criadas anteriormente para fazer um menu de opções com o while, fazendo:
# Opção 1: Cadastrar um novo Produto
# Opção 2: Listar os produtos e seus preços
# Opção 3: Atualizar o preço de um produto
# Opção 4: Deletar um produto
# Opção 5: Sair
# lembre-se que para cadastrar é necessário que o usuário forneça os dados (nome, preço, a descrição...), para atualizar o usuário precisa fornecer o ID e o novo preço e para deletar o usuário precisa fornecer o id.

import os
from dotenv import load_dotenv
from supabase import create_client #

load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #

resposta = (supabase.table('pedidos')
            .select("id, valor, forma_pagamento,usuarios(nome,idade)")
            .eq('id_usuario',1)
            .execute())
print(resposta.data)

# Cria uma tabela chamada itens_pedido, essa tabela deverá ter uma relação de 1:n com a tabela pedidos, ou seja 1 pedido por ter vários itens associados a eles, mas um item pedido só pode ter um pedido associado a ele. 
# itens_pedido

# id
# nome
# preco
# criado_em
# quantidade
# desconto
# id_pedido

# insira pelo menos 2 ou 3 itens para cada pedido, ou seja a Ana fez o pedido 1 com os itens teclado, mouse e fone
# Crie um código em python que busque no banco de dados todos os itens pedidos feito pelo usuario 2, trazendo: nome do usuario, valor do pedido, os nomes dos itens pedidos.
# Exemplo
# nome: joão, pedido: 1, valor: 300, itens= [fone, teclado, mouse]

resposta = (supabase.table('itens_pedido')
            .select('nome, pedidos(id,valor, usuarios(nome))')
            .execute())
print(resposta.data)

resposta = supabase.table('matricula').select('alunos(nome), curso(nome)').eq('id_aluno',1).execute()

for resp in resposta.data:
    print(f'{resp['alunos']['nome']} : {resp['curso']['nome']}')
    