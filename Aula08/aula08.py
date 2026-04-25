# import meus_calculos

# areaQuadrado = meus_calculos.areaQuadrado(3)
# print(f'A área do quadrado é {areaQuadrado}')

# areaT = meus_calculos.areaTriangulo(10,5)
# print(f'A área do triangulo é {areaT}')

# from meus_calculos import areaTrapezio, areaRetangulo

# trapezio = areaTrapezio(10,8,5)
# retangulo = areaRetangulo(3,7)

# print(f'A área do trapezio é {trapezio}')
# print(f'A área do retangulo é {retangulo}')

# from meus_calculos import *

# triangulo = areaTriangulo(3,8)
# print(f'A área do triangulo é {triangulo}')

# import meus_calculos as areas
# import meus_alertas as alert

# triangulo = areas.areaTriangulo(10,5)
# print(f'A área do triangulo é {triangulo}')

# alerta = alert.alertaEstoque(60)
# print(alerta)

# import estoque 
# opcao = input('1 - Adicionar Produto\n2 - Listar Produtos\n3 - Sair\n')
# produtos = [
#     {
#         "nome": "Mouse",
#         "preco": 50,
#         "quantidade": 10
#     },
#     {
#         "nome": "Teclado",
#         "preco": 100,
#         "quantidade": 80
#     }
# ]
# while (opcao != '3'):
#     if opcao == '1':

#         nome = input('Digite o nome do produto: ')
#         preco = float(input('Digite o preço do produto: '))
#         quantidade = int(input('Digite a quantidade do produto: '))

#         estoque.adicionarProduto(produtos,nome, preco, quantidade)

#     if opcao == '2':
#         estoque.listarProdutos(produtos)


#     opcao = input('1 - Adicionar Produto\n2 - Listar Produtos\n3 - Sair\n')


# import pyttsx3

# robo = pyttsx3.init()

# voices = robo.getProperty('voices')
# robo.setProperty('voice', voices[0].id)
# robo.say("Olá mundo")

# robo.runAndWait()

import pyqrcode

link = 'https://api.whatsapp.com/send/?phone=5585985421274&text&type=phone_number&app_absent=0'
qr = pyqrcode.create(link)
qr.png('qrcodeWhatsapp.png',scale=6)
print('QRcode gerado com sucesso')





