# pip install pyqrcode
# import pyqrcode
# from pyqrcode import create

import pyqrcode as qr

print('Sistema para gerar QRCode Whatsapp')
telefone = input('Digite o seu número: ')
mensagem = input('Digite a mensagem: ')

link = f'https://api.whatsapp.com/send/?phone=55{telefone}&text={mensagem}&type=phone_number&app_absent=0'

qrcode = qr.create(link)
qrcode.png('meuQRCODE.png',scale=5)

print(link)