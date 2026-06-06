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
# 5. Liste os funcionários cujo firstname começa com a letra A.
# 6. Mostre os funcionários que possuem idade entre 30 e 50 anos.
# 7. Liste firstname, idade e baserate dos funcionários com salário (baserate) maior que 60.
# 8. Mostre os funcionários cujo emailaddress contém gmail.
# 9. Liste apenas os funcionários com currentflag = true.
# 10. Mostre os funcionários do gênero masculino (gender = 'M') ordenados da maior para a menor idade.


resposta = supabase.table('usuarios').select('*').execute()
usuarios = resposta.data
mostrarResultado(usuarios)

# nome = input('Digite o nome: ')
# email = input('Digite o email: ')
# telefone = input('Digite o telefone: ')

# novoUsuario = {
#     'nome':nome,
#     'email':email,
#     'telefone':telefone
# }

# resposta = supabase.table('usuarios').insert(novoUsuario).execute()
# print(resposta)

# print('Editando registros')
# id_user = input('Digite o ID a ser editado')

# telefone = input('Digite o novo telefone: ')

# atualizacao = {
#     'telefone':telefone
# }

# resp = supabase.table('usuarios').update(atualizacao).eq('id',id_user).execute()

print('Deletar Usuário')
id_user = input('Digite o ID a ser deletado: ')

resp = supabase.table('usuarios').delete().eq('id',id_user).execute()