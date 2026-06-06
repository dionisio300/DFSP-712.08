# pip install supabase

from supabase import create_client

supabase = create_client('','')

# resposta = supabase.table('employee').select('*').execute()
# resposta = resposta.data
# print(resposta)

def mostrarResultado(listaResultados):
   for resultado in listaResultados:
        for key, value in resultado.items():
            print(f'{key}: {value}')
        print('-'*30)
         

# Quetões
# 1. Liste todos os funcionário mostrando apenas o firstname, lastname e emailaddress.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 2. Mostrar os 10 funcionários mais jovens da empresa, ordenando por idade.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress,idade').order('idade').limit(10).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 3. Liste apneas os funcionário que possuem vacationhours maior = 40.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').eq('vacationhours',40).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

'''
.eq('coluna',valor) -> igual
.neq('coluna', valor) -> diferente (não igual)
.gt('coluna',valor) -> Maior que
.gte('coluna',valor) -> Maior ou igual
.lt('coluna',valor) -> Menor que
.lte('coluna',valor) -> Menor ou igual
.like('coluna','%texto%') -> link '%texto%'
.in_('coluna',[1,2,3,...valores]) -> se esses valores constam na coluna

'''

# 4. Mostre firstname, emailaddress e departmentname dos funcionários do departamento Production.

# resposta = supabase.table('employee').select('firstname,emailaddress,departmentname').eq('departmentname','Production').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 5. Liste os funcionários cujo firstname começa com a letra A.

# resposta = supabase.table('employee').select('firstname, emailaddress').like('firstname','A%').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 6. Mostre os funcionários que possuem idade entre 30 e 50 anos.

# resposta = supabase.table('employee').select('firstname','idade').gt('idade',30).lt('idade',65).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 7. Liste firstname, idade e baserate dos funcionários com salário (baserate) maior que 60.
# 8. Mostre os funcionários cujo emailaddress contém gmail.
# 9. Liste apenas os funcionários com currentflag = true.
# 10. Mostre os funcionários do gênero masculino (gender = 'M') ordenados da maior para a menor idade.

'''
C -> CREATE - inserir dados - INSERT
R -> READ - leitura de dados - SELECT
U -> UPDATE - Atualização dos dados - UPDATE
D -> DELETE - Apagar algum dado - DELETE
'''

# usuario = {
#     "nome":'João',
#     "email":'joao@gmail.com',
#     "idade":31,
#     "senha":'senha123'
# }
# try: 
#     resposta = supabase.table('usuarios').insert(usuario).execute()
#     print(resposta.data)
# except Exception as e:
#     print(e.message)

# usuario = {
#     "nome":"Maria Clara",
#     "idade":28
# }
# resposta = supabase.table('usuarios').update(usuario).eq('id',1).execute()
# print(resposta.data)

'''
C -> CREATE - inserir dados - INSERT
R -> READ - leitura de dados - SELECT
U -> UPDATE - Atualização dos dados - UPDATE
D -> DELETE - Apagar algum dado - DELETE
'''

# D -> DELETE - Apagar algum dado - DELETE
resposta = supabase.table('usuarios').delete().eq('id',6).execute()
print(resposta.data)

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

def cadastrarProduto(nome,preco,quantidade,descricao):
    print(nome, preco, quantidade,descricao)


#3 - Cria uma função para mostrar o nome o preço e a descrição dos produtos com preço maior que 100 reais
def mostrarProdutos():
    resposta = supabase.table('produtos').select("nome, preco, descricao").gt('preco',100).execute()
    resposta = resposta.data
    return resposta

# Utilize as funções criadas anteriormente para fazer um menu de opções com o while, fazendo:
# Opção 1: Cadastrar um novo Produto
# Opção 2: Listar os produtos e seus preços
# Opção 3: Atualizar o preço de um produto
# Opção 4: Deletar um produto 
# Opção 5: Sair
# lembre-se que para cadastrar é necessário que o usuário forneça os dados (nome, preço, a descrição...), para atualizar o usuário precisa fornecer o ID e o novo preço e para deletar o usuário precisa fornecer o id.