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
saldo = 1000
opcao = int(input('1 - Consultar Salado\n2 - Sacar\n3 - Depositar\nResposta: '))
if opcao == 1:
    print(f'Saldo atual = {saldo}')
elif opcao == 2:
    saque = float(input('Quanto você deseja sacar? '))
    if saque > saldo:
        print('Saldo insuficiente')
    else:
        saldo = saldo - saque
        print(f'Saque realizado com sucesso!\nSaldo atual = {saldo}')
elif opcao == 3:
    deposito = float(input('Quanto você deseja depositar?'))
    saldo = saldo + deposito
    print(f'Depósito realizado com sucesso!!\nSaldo atual = {saldo}')
else:
    print('Opção inválida')

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