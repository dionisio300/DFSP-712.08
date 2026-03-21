# # Definição de uma lista em python
# listaNomes = ['Dionizio','Davi','Letícia','Jessica','...',10,100,1000]

# print(listaNomes[3]) # Quarto elemento da lista
# print(listaNomes[0]) # Primeiro Elemento da lista
# print(listaNomes[-1]) # Último elemento da lista
# print(listaNomes[-2]) # penúltimo elemento da lista

# listaNomes[3] = 'Pedro'

# print(listaNomes)

# Questão 1
listaNumeros = [1,2,3,4,5,6]
print(listaNumeros[0])

# Questão 2
soma = listaNumeros[0] + listaNumeros[-1]
print(soma)

# Questão 3
listaNumeros[3] = 8
print(listaNumeros)

# Fatiamento de uma lista
#               0 1 2 3 4 5 6 7  8  9
listaNumeros = [3,4,5,6,7,8,9,10,11,12]

print(listaNumeros)

lista2Numeros = listaNumeros[0:7:2]

print(lista2Numeros)

listaNomes = ['João','Maria','Pedro','Tiago','Carla','Jessica']

listaCompleta = lista2Numeros + listaNomes

print(listaCompleta)

print(listaNomes * 3)

print(listaNomes[2:5])
# 1. Crie uma lista de 0 até 5 e outra lista de 6 até 10,
# depois some as duas

numerosParte1 = [0,1,2,3,4,5]
numerosParte2 = [6,7,8,9,10]

numerosCompletos = numerosParte1 + numerosParte2

print(numerosCompletos)

# 2. Crie uma lista com 5 valores numéricos e some os três
# últimos itens da lista.

soma = numerosParte2[-1]+numerosParte2[-2]+numerosParte2[-3]
print(f'A soma dos três últimos é {soma}')

# 3. Crie uma lista com 5 valores e multiplique ela por 2

listaDobrada = numerosParte2 * 2
print(listaDobrada)


#                               [0,1,2,3,4,5,6,7,8,9,10]
print(f'Lista Numeros completos {numerosCompletos}')

for item in numerosCompletos:
    print(item)


# listaNomes = ['João','Maria','Pedro','Tiago','Carla','Jessica']
# listaNomes[3] = 'Caio'
flagAchou = False

for nome in listaNomes:
    if 'Caio' == nome:
        print('O Caio faz parte da lista')
        flagAchou = True
        break
    
if flagAchou == False:
    print('O Caio não faz parte da lista')


# 1. Faça uma lista com 10 números e depois percorra
# cada elemento com um laço de repetição e mostre
# cada um na tela

listaNumeros = [7,8,9,1,2,3,5,5,5]

for numero in listaNumeros:
    print(numero)

# 2. Faça uma lista com 10 números e depois percorra
# cada elemento com um laço de repetição, porém
# exiba somente os números pares.
print('Questão 2\n')
for numero in listaNumeros:
    if numero % 2 == 0:
        print(f'O número {numero} é par')



print(listaNomes)

listaNomes.append('David') # Adiciona um elemento no final da lista
# listaNomes.append(10)
listaNomes.insert(0,'Aline') # Adiciona um elemento numa posição da lista
listaNomes.insert(3,'Gabriel')
print(listaNomes)
listaNomes.pop() # Remove um elemento do final da lista
listaNomes.pop(0) # Remove um elemento de uma posição da lista
print(listaNomes)
del(listaNomes[2:5])
print(listaNomes)

# 1. Faça uma lista de nomes inicialmente vazia e após isso, crie um for para adicionar 5 nomes dentro dessa lista vindos do input.

# 2. Crie uma lista com 5 elementos e remova os últimos 3
# elementos de dentro dela utilizando um for.



















