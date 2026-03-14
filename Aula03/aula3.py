# Variáveis

# nome = input('Digite o seu nome: ')
# idade = input('Digite sua idade: ')

# print('Seu nome ',nome,' sua idade é ',idade)

# x = int(input('Digite o primeiro número: '))
# y = int(input('Digite o segundo número: '))

# print(x,y)
# # Operadores Aritiméticos
# # + -> soma
# soma = x + y
# print(f'Soma: {soma}')
# # - -> subtração
# sub = x - y
# print(sub)
# # * -> multiplicação
# multiplicacao = x * y
# print(multiplicacao)
# # / -> divisão
# divisao = x/y
# print(divisao)
# # % -> Resto da divisão
# resto = x % y
# print(resto)
# # ** -> Exponenciação
# pot = x**y
# print(pot)
# # // -> Divisão por inteiro
# divInt = x//y
# print(divInt)


# print(f'Soma = {soma}, Subtração = {sub}, multiplicação = {multiplicacao}, divisão = {divisao}')

# print('soma ',soma,', subtração = ',sub, ', multiplicação = ',multiplicacao,', divisão = ',divisao)

# x = 4
# y = 4

# # Operadores Relacionais
# # > -> Maior que
# print(x > y)
# # < -> Menor que
# print(x < y)
# # >= -> Maior ou igual
# print(x >= y)
# # <= -> Menor ou igual
# print(x <= y)
# # == -> igual
# print(x == y)
# # != -> Diferente
# print(x != y)

# portência e raiz
# Multiplicação ou divisão
# soma e subtração

print( (3 + 5) * 2)

# 1. Escreva um programa em python que receba do teclado 4 notas e calcule a média aritimética dessas notas, mostrando na tela o resultado.

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))

# media = (n1 + n2 + n3 + n4)/4
# print(f'{media:.2f}')
      
# verifique se a média é maior ou igual a 7 e print aprovado, se a média estiver entre 4 e 7 print na tela recuperação e se a média for menor que 4 print na tela reprovado.

# if media >= 7:
#     print('Aprovado')
# if media >= 4:
#     print('Recuperação')
# else:
#     print('Reprovado')

# print(f'A média é {media}')

# # 2. Escreva um programa em python que receba 3 notas e 3 pesos e calcule a média ponderada notas.

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))

# p1 = float(input('Digite a primeiro peso: '))
# p2 = float(input('Digite a segundo peso: '))
# p3 = float(input('Digite a terceiro peso: '))

# mediaPonderada = (n1 * p1 + n2 * p2 + n3 * p3)/( p1 + p2 + p3)
# print(f'Sua média é {mediaPonderada}')

# if x > 3:
#   Bloco de código
# else:
#   Bloco de código

# x = 5
# y = 15

# if x > y:
#     print('X é maior que o Y')
# elif y > x:
#     print('Y é maior que o X')
# else:
#     print('X é igual a Y')


# Laços de repetição

# for variavel in range (valor)

# for i in range (10):
#     print(f'o valor de i é {i+1}')

# for i in range (1,11):
#     print(f'o valor de i é {i}')

# for i in range (1,100,3):
#     print(f'o valor de i é {i}')


# 1. Faça um laço de repetição que printe os número de 1
# até 20.

# 2. Faça um programa que print na tela a mensagem
# “olá mundo” 10 vezes.

# 3. Faça um laço de repetição que printe os números de
# 0 até 100 pulando de 2 em 2

# 4. Faça um laço de repetição que irá rodar 5 vezes e a
# cada volta ele terá que usar um input para pedir um
# número , mas somente print em tela os números
# maiores que 10

# while condição -> Não sabe o número de repetições
# for -> quando vc sabe o número de repetições

i = 0 # 10
while i < 10:
    i = int(input('Digite um valor maior que 9: '))

# loop infinito

while True:
    i = int(input('Digite um número maior que 9: '))
    if i > 9:
        print('Obrigado por ter digitado um número maior que 9! ;)')
        break



# 1. Faça um laço while que mostre os números de 1 até 10
# 2. Faça um laço while que peça o nome de 5 pessoas e mostre esse nome em tela.
# 3. Faça um programa que peça 5 números para o usuário, porém só exiba o número se ele for par

# 4. Escreva um programa que peça a senha do usuário se a senha for “PYTHON”, então você deve exibir uma mensagem de logado e encerrar o laço, caso contrário continue pedindo.