# Se clonar o repositório usar esses comandos:
# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install -r requirements.txt - instala as dependências do projeto

# pip install supabase
# pip install python-dotenv
# pip install fastapi - para criar a API
# pip install uvicorn - para rodar a API

# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env
# Executar o fastapi com o uvicorn
# uvicorn aula15:app --reload -> para rodar a API

import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta, timezone
from supabase import create_client #
from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.security import APIKeyHeader
from fastapi.security import OAuth2PasswordBearer

import requests
load_dotenv()

jwt_secret = os.getenv('JWT_SECRET')
algoritmo = 'HS256'


supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
api_key_correta = os.getenv('API_KEY')

app = FastAPI()
api_key_header = APIKeyHeader(name='api_key')
auth = OAuth2PasswordBearer(tokenUrl='login')


# Função para gerar o token
def criar_token(dados_usuario):
    dados_token = dados_usuario.copy()
    expiracao = datetime.now() + timedelta(minutes=30)
    dados_token.update({
        'exp':expiracao
    })
    token = jwt.encode(dados_token, jwt_secret, algorithm=algoritmo)
    return token


# selecao = input('Digite o produto que deseja buscar: ')
# produtos = requests.get(f'https://fakestoreapi.com/products/{selecao}').json()

# print(produtos['image'])

# Criação das primeiras rotas da API

@app.post('/login')
def login(dados: dict = Body()):
    cpf = dados.get('cpf')
    senha = dados.get('senha')
    try:
        resposta = supabase.table('biblioteca_usuarios').select('nome, ativo, tipo').eq('cpf',cpf).eq('senha',senha).execute()

        print(len(resposta.data))

        if len(resposta.data) == 0:
            print('entrou no if')
            return {
                "erro":"O usuário errou a senha ou o cpf"
            }
            

        print(f'resposta do banco {resposta.data[0]}')
        token = criar_token(resposta.data[0])
        print(token)

        return {
            'access_token':token,
            'token_type':'bearer'
        }
    except Exception:
        HTTPException(status_code=501, detail='erro ao acessar o banco')


def verificar_token(token: str = Depends(auth)):
    print('função verificar token')
    try:
        dados_token = jwt.decode(
            token,
            jwt_secret,
            algorithms=algoritmo
        )
        cpf = dados_token.get('cpf')
        if cpf is None:
            raise HTTPException(status_code=401, detail='token inválido')

    except Exception:
        pass


def verificar_api_key(api_key_recebida: str = Depends(api_key_header)):
    if api_key_recebida != api_key_correta:
        raise HTTPException(status_code=401, detail='Chave API está errada')
    return api_key_recebida

@app.get('/livros')
def get_livros(api_key: str = Depends(verificar_token)):
    resposta = supabase.table('biblioteca_livro').select('*').execute()
    livros = resposta.data
    return livros

# path parameter
@app.get('/livros/{id}')
def get_livros_id(id: int):
    resposta = supabase.table('biblioteca_livro').select('*').eq('id',id).execute()
    livros = resposta.data
    if len(livros) == 0:
        return {"Mensagem: Livro não encontrado"}
    return livros

@app.get('/livros/{id}/{ano}')
def get_livros_id_ano(id: int, ano: int):
    
    return {
        "id":f'Você digitou {id}',
        "ano": f'Você digitou o ano {ano}'
    }
# Query strings
# www.google.com/search?q=teste&nome=Dionizio&idade=29

@app.get('/busca')
def busca(titulo: str = None, quantidade: int = None, genero: str = None, ano: int = None):
    resposta = supabase.table('biblioteca_livro').select('*')
    if titulo:
        resposta = resposta.ilike('titulo', f'%{titulo}%')
    if quantidade:
        resposta = resposta.eq('quantidade', quantidade)
    if genero:
        resposta = resposta.ilike('genero', f'%{genero}%')
    if ano:
        resposta = resposta.eq('ano', ano)
    resposta = resposta.execute()
    livros = resposta.data
    if len(livros) == 0:
        return {"Mensagem: Livro não encontrado"}
    return livros

# http://127.0.0.1:8000/busca?titulo=Dom casmurro&quantidade=10&genero=romance&ano=1990
# POST


@app.post('/livros')
def cadastrar_livro(dados: dict = Body(), api_key: str = Depends(verificar_api_key)):
    resposta = supabase.table('biblioteca_livro').insert(dados).execute()
    resposta = resposta.data
    return resposta


# Delete
@app.delete('/deletarlivro/{id}')
def deletarLivro(id: int = None):
    resposta = supabase.table('biblioteca_livro').delete().eq('id',id).execute()
    return {
        "msg":"Livro deletado com sucesso",
        "resposta":resposta.data
    }
# UPDATE / put
@app.put('/atualizarlivro/{id}')
def atualizarlivro(id: int, dados: dict = Body()):
    resposta = supabase.table('biblioteca_livro').update(dados).eq('id',id).execute()
    return {
        "msg":'Livro atualizado',
        "dados":resposta.data
    }

#192.168.1.230:8000/livros,


# Verifique no seu supabase se você ja tem o banco de dados do sistema financeiro que desenvolvemos em sala.
# Crie 4 APIs para o sistema financeiro:

# 1 Listar os usuário
# 2 Cadastrar uma transação 
# 3 Listar todas as transações de um usuário por meio do ID
# 4 Atualizar os dados de um usuário

# Crie uma chave de API para autenticar os acessos a essas 4 APIs


