# Aula 05 - Revisão de listas
#               0       1      2
listaNome = ['Maria','João','Pedro']

print(listaNome[2])

listaNome[1] = 'Tiago'

print(listaNome)

for nome in listaNome:
    print(nome)

# Crie uma lista com 10 números e use o for para printar na tela cada um dos 10 números

listaNumeros = [1,2,3,4,5,6,7,8,9,10]

for numero in listaNumeros:
    print(numero)

# A partir da primeir lista, use um um for para percorrer a lista e printar os números maiores que 5.
for numero in listaNumeros:
    if numero > 5:
        print(numero)

# Funções internas de listas

# append() -> Acrescentar no final de uma lista
print(listaNome)
listaNome.append('João')
print(listaNome)

# insert(0,item) -> Acrescenta em uma posição
listaNome.insert(0,'Carla')
print(listaNome)
# pop() -> Deleta o último item da lista

listaNome.pop()

# pop(0) -> Deleta de uma posição
listaNome.pop(1)
print(listaNome)

listaNome.append('Maria')
listaNome.append('Eduardo')
listaNome.append('Eduarda')

# del(lista[x:y]) -> Deleta um intervalo de uma lista
del(listaNome[2:5])

print(listaNome)

for i in range(3):
    nome = input('Digite o nome: ')
    listaNome.append(nome)

print(listaNome)

lista = []

# 1. Crie uma lista vazia chamada aprovados. Peça para o usuário digitar 5 notas, e para cada nota:
# Se a nota for maior ou igual a 7. adicione na lista aprovados
# caso contrário, ignore

# 2. Dada a lista: Dada a lista: valores = [5, 12, 7, 20, 3, 15]
# Percorra a lista e remova todos os números menores que 10. Mostre a lista com o resultado final