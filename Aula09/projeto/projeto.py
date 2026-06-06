# python -m venv venv
# venv\scripts\activate
# pip list
# deactivate
# pip freeze > requirements.txt
# pip install streamlit
# steamlit run projeto.py

import streamlit as st
import pyqrcode as qr
st.title('Gerador de qrcode')


# 1. Entrada de dados
nome = st.text_input('Qual o seu nome?')
telefone = st.text_input('Digite o seu telefone')
mensagem = st.text_area('Digite a mensagem')

import pyttsx3

robo = pyttsx3.init()
robo.say("Olá mundo")
robo.runAndWait()

if st.button("Enviar"):
    link = f'https://api.whatsapp.com/send/?phone=55{telefone}&text={mensagem}&type=phone_number&app_absent=0'

    qrcode = qr.create(link)
    qrcode.png('qrcode_aula.png',scale=3)

    st.write('QRCode gerado com sucesso!!')
    st.image('qrcode_aula.png')
    st.write(link)
