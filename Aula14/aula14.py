# Se clonar o repositório usar esses comandos:
# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install requirements.txt - instala as dependências do projeto

# pip install supabase
# pip install python-dotenv
# pip install fastapi - para criar a API
# pip install uvicorn - para rodar a API

# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env

# Executar o fastapi com o uvicorn
# uvicorn aula14:app --reload -> para rodar a API

import os
from dotenv import load_dotenv
from supabase import create_client #
from fastapi import FastAPI
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
# CRUD

app = FastAPI()

# selecao = input('Digite o produto que deseja buscar: ')
# produtos = requests.get(f'https://fakestoreapi.com/products/{selecao}').json()

# print(produtos['image'])

# Criação das primeiras rotas da API

@app.get('/livros')
def get_livros():
    resposta = supabase.table('biblioteca_livro').select('*').execute()
    livros = resposta.data
    return livros

@app.get('/livros/{id}')
def get_livros_id(id: int):
    resposta = supabase.table('biblioteca_livro').select('*').eq('id',id).execute()

    livros = resposta.data

    if len(livros) == 0:
        return {"Mensagem: Livro não encontrado"}

    return livros



