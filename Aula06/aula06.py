'''

1. Verifique se o usuário do sistema é maior de idade ou não.
2. Peça ao usuário um número e verifique se ele é ímpar ou par.
3. Peça ao usuário a nota de um aluno e se for maior que 7, mostre aprovado se não mostre recuperação.

5. sistema de saque/depósito (simulação de caixa eletrônico)
Você está desenvolvendo um sistema simples de caixa eletrônico.
O sistema deve iniciar com um saldo fictício de R$ 1000.
Mostre o seguinte menu:

1 - Consultar saldo
2 - Sacar dinheiro
3 - Depositar dinheiro

Utilize if/elif para controlar o fluxo do sistema.
Regras:
1 (Consultar saldo):
	exibir o saldo atual
2 (Sacar dinheiro):
	pedir o valor do saque
	verificar:
	se o valor é menor ou igual ao saldo → realizar saque
	senão → exibir "Saldo insuficiente"
		atualizar o saldo
	exibir novo saldo
3 (Depositar dinheiro):
	pedir o valor do depósito
	adicionar ao saldo
	exibir novo saldo
'''

# 1. Verifique se o usuário do sistema é maior de idade ou não.
# idade = int(input('Digite sua idade'))
# print(idade)
# if idade >= 18:
#     print('É maior de idade')
# else:
#     print('Não é maior de idade')

# 2. Peça ao usuário um número e verifique se ele é ímpar ou par.

# numero = int(input('Digite um número: '))
# if numero % 2 == 0:
#     print('O número é par')
# else:
#     print('Impar')

# 3. Peça ao usuário 3 notas de um aluno, calcule a média e se a média for maior que 7, mostre aprovado se não mostre recuperação.

# nota1 = float(input('Digite a nota: '))
# nota2 = float(input('Digite a nota: '))
# nota3 = float(input('Digite a nota: '))

# media = (nota1 + nota2 + nota3)/3

# if media >= 7:
#     print('Aprovado')
# else:
#     print('Recuperação')
'''
4. Peça para um usuário digitar um número e print se ele for positivo positivo.

5. Peça para o usuário digitar o preço de um produto e diga se ele é caro se custar mais de 100 reais e barato se custar menos que 100.

'''

# saldo = 1000
# opcao = int(input('1 - Consultar Salado\n2 - Sacar\n3 - Depositar\nResposta: '))
# if opcao == 1:
#     print(f'Saldo atual = {saldo}')
# elif opcao == 2:
#     saque = float(input('Quanto você deseja sacar? '))
#     if saque > saldo:
#         print('Saldo insuficiente')
#     else:
#         saldo = saldo - saque
#         print(f'Saque realizado com sucesso!\nSaldo atual = {saldo}')
# elif opcao == 3:
#     deposito = float(input('Quanto você deseja depositar?'))
#     saldo = saldo + deposito
#     print(f'Depósito realizado com sucesso!!\nSaldo atual = {saldo}')
# else:
#     print('Opção inválida')

'''
4. sistema de atendimento com fluxo (menu interativo)
Você está desenvolvendo um sistema de atendimento para um aplicativo.
O usuário deve escolher uma opção:
1 - Criar conta
2 - Fazer login 
3 - Recuperar senha
Dependendo da escolha, o sistema deve:
1 (Criar conta):
	pedir nome
	pedir email
	pedir senha
	exibir: "Conta criada com sucesso para [nome]"
2 (Login):
	pedir email
	pedir senha
	exibir: "Login realizado com sucesso"
3 (Recuperar senha):
	pedir email
	perguntar "Deseja receber código por email ou SMS?"
	exibir: "Instruções enviadas"
Caso a opção seja inválida, exibir "Opção inválida"
'''

'''
1. Você está desenvolvendo um sistema simples de menu para um aplicativo.
Solicite ao usuário uma opção digitando:
1 - Cadastrar usuário
2 - Listar usuários
3 - Sair do sistema

Utilize if/elif para exibir a ação correspondente a cada opção. Caso o valor seja inválido, exiba "Opção inválida".
Repita a solicitação até que a pessoa selecione a opção 3 para sair do sistema.'''

# opcao = ''
# while(opcao != 3):
#     opcao = int(input('1 - Cadastrar usuário\n2 - Listar usuários\n3 - Sair do sistema\n'))
#     if opcao == 1:
#         nome = input('Digite o nome')
#         telefone = input('Digite o seu telefone')
#         print('Cadastro realizado com sucesso!')
#     elif opcao == 2:
#         print('Maria - 85985858585\nJoão - 85999999999')
#     elif opcao == 3:
#         print('Saindo...')
#     else:
#         print('Opção inválida')


# 1. Crie um programa que seria uma lista de desejos, onde o usuário pode pedir 3 coisas e você mostra cada um dos desejos na tela.

# for i in range (3):
#     desejo = input(f'Desejo {i+1}: ')


# 2. Crie um programa que receba um valor de compra e depois um número de parcelas, e depois mostre na tela o valor de cada parcela utilizando um for

# valor = float(input('Digite o valor da compra: '))

# nparcelas = int(input('Digite o número de parcelas desejado: '))

# while not (nparcelas <= 12 and nparcelas > 0):
#     nparcelas = int(input('Digite o número de parcelas desejado: '))

# # while (nparcelas > 12 or nparcelas <= 0):
# #     nparcelas = int(input('Digite o número de parcelas desejado: '))

# valorParcela = valor/nparcelas

# for i in range(nparcelas):
#     print(f'Parcela {i+1} = {valorParcela}')

# Crie um programa que tenha o seguinte menu
'''
1 - Adicionar produto ao carrinho
2 - Listar os produtos
3 - Sair
'''
# Se o usuário selecionar adicionar produtos ao carrinho você deve pedir para ele inserir o nome do produto e colocar esse produto em uma lista de produtos.
# Se o usuário selecionar listar produtos, você deve exibir todos os produtos que estão dentro da lista

#                0         1         2
# produtos = ['Notebook', 'Tablet', 'Mouse']
# opcao = ''
# while (opcao != 3):
#     opcao = int(input('1 - Adicionar produtos ao carrinho\n2 - Listar os produtos\n3 - Sair\n'))
#     if opcao == 1:
#         produto = input('Nome do produto: ')
#         produtos.append(produto)
#     elif opcao == 2:

#         for produto in produtos:
#             print(produto)

#     elif opcao == 3:
#         print('Saindo...')




#               0           1        2
# produtos = ['Notebook', 'Tablet', 'Mouse']
# lista.append(item) ->  adiciona um elemento no final da lista
# lista.insert(posicao,item) -> adiciona um elemento num posição específica
# lista.pop() -> Remover o último elemento da lista
# lista.pop(posicao) -> Remove um elemento de uma posição específica
# lista.index(item) -> a posição em que o item está 

# produtos.append('Carregador')
# produtos.insert(0,'fone')
# produtos.pop()
# produtos.pop(1)

# print('Mouse' in produtos)

# print(produtos)


'''
Sistema de Lista de Tarefas

Você deve criar um sistema simples de gerenciamento de tarefas.

O sistema começa com a lista:

tarefas = ['Estudar Python', 'Fazer exercício', 'Ler livro']

O programa deve exibir um menu:

1 - Adicionar nova tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair

Regras:

Se escolher 1, o usuário digita uma tarefa e ela é adicionada à lista.
Se escolher 2, listar todas as tarefas.
Se escolher 3, pedir o nome da tarefa e remover da lista (se existir).
Se escolher 4, encerrar o programa.
'''