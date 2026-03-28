# Aula 05 - Revisão de listas
#               0       1      2
# listaNome = ['Maria','João','Pedro']

# print(listaNome[2])

# listaNome[1] = 'Tiago'

# print(listaNome)

# for nome in listaNome:
#     print(nome)

# # Crie uma lista com 10 números e use o for para printar na tela cada um dos 10 números

# listaNumeros = [1,2,3,4,5,6,7,8,9,10]

# for numero in listaNumeros:
#     print(numero)

# # A partir da primeir lista, use um um for para percorrer a lista e printar os números maiores que 5.
# for numero in listaNumeros:
#     if numero > 5:
#         print(numero)

# # Funções internas de listas

# # append() -> Acrescentar no final de uma lista
# print(listaNome)
# listaNome.append('João')
# print(listaNome)

# # insert(0,item) -> Acrescenta em uma posição
# listaNome.insert(0,'Carla')
# print(listaNome)
# # pop() -> Deleta o último item da lista

# listaNome.pop()

# # pop(0) -> Deleta de uma posição
# listaNome.pop(1)
# print(listaNome)

# listaNome.append('Maria')
# listaNome.append('Eduardo')
# listaNome.append('Eduarda')

# # del(lista[x:y]) -> Deleta um intervalo de uma lista
# del(listaNome[2:5])

# print(listaNome)

# for i in range(3):
#     nome = input('Digite o nome: ')
#     listaNome.append(nome)

# print(listaNome)

# lista = []

# 1. Crie uma lista vazia chamada aprovados. Peça para o usuário digitar 5 notas, e para cada nota:
# Se a nota for maior ou igual a 7. adicione na lista aprovados
# caso contrário, ignore
# aprovados = []
# for i in range(5):
#     nota = float(input('Digite a nota: ')) #str
#     if nota >= 7:
#         aprovados.append(nota)

# print(aprovados)

# 2. Dada a lista: Dada a lista: valores = [5, 12, 7, 20, 3, 15]
# Percorra a lista e remova todos os números menores que 10. Mostre a lista com o resultado final

# valores = [5, 12, 7, 20, 3, 15,10,20]
# valoresMaiores = []

# for valor in valores:
#     if valor >= 10:
#         valoresMaiores.append(valor)

# valores = valoresMaiores

# print(valores)

# print(len(valores))
# # valores = [5, 12, 7, 20, 3, 15,10,20]
# len(valores)
# for i in range(len(valores) - 1,-1,-1):
#     print(f'Valores: {valores[i]}')
#     if valores[i] < 10:
#         del(valores[i])

# print(valores)

# Dicionários

# pessoa = {
#     "nome":"Maria",
#     "idade":20,
#     "cidade":"Fortaleza"
# }
# print(pessoa)
# print(pessoa["nome"])
# print(pessoa["idade"])
# print(pessoa["cidade"])

# pessoa["profissao"] = 'Professora'
# print(pessoa)

# Crie um dicionário chamado aluno e salve o nome, o curso e a média desse aluno recebendo esses dados do teclado (usando o input)

# nome = input('Digite seu nome: ')
# curso = input('Digite sua curso: ')
# cidade = input('Digite sua cidade: ')

# aluno = {
#     'nome': nome,
#     'curso': curso,
#     'cidade':cidade
# }

# print(f'Olá {aluno["nome"]} seja bom-vindo ao curso de {aluno["curso"]} na cidade de {aluno["cidade"]}')

carro = {}
print(carro)

carro['marca'] = input('Digite a marca do carro: ')
carro['cor'] = input('Digite a cor do carro: ')
carro['ano'] = input('Digite o ano do carro: ')

print(carro)