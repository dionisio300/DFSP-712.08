# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install supabase
# pip install python-dotenv
# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env
import os
from dotenv import load_dotenv
from supabase import create_client #

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
# CRUD
# Inserir os dados nas tabelas
def inserirUsuario():
    nome = input('Digite o nome: ')
    cpf = input('Digite o cpf: ')
    telefone = input('Digite o Telefone: ')
    endereco = input('Digite o endereço: ')
    novoUsuario = {
        "nome":nome,
        "cpf":cpf,
        "telefone":telefone,
        "endereco":endereco
    }
    resposta = supabase.table('biblioteca_usuarios').insert(novoUsuario).execute()
    print(resposta)

# inserirUsuario()

def inserirDadosTabelas(tabela,dados):
    try:
        resposta = supabase.table(tabela).insert(dados).execute()
        print('Dados inseridos com sucesso')
    except Exception as erro:
        print(f'Erro ao inserir os dados: {erro}')
    

def coletarDadosInserir():
    opcao = input('Selecione uma opção:\n1 - Inserir Usuario\n2 - Inserir Perfil\n3 - Inserir Autor\n4 - Inserir Livro\n5 - Inserir Empréstimo\n')
    if opcao == '1':
        tabela = 'biblioteca_usuarios'
        nome = input('Digite o nome: ')
        cpf = input('Digite o cpf: ')
        telefone = input('Digite o Telefone: ')
        endereco = input('Digite o endereço: ')
        novoUsuario = {
            "nome":nome,
            "cpf":cpf,
            "telefone":telefone,
            "endereco":endereco
        }
        inserirDadosTabelas(tabela,novoUsuario)
    if opcao =='2':
        tabela = 'biblioteca_perfil'
        foto = input('Digite a url da foto: ')
        bio = input('Digite a bio: ')
        preferencias = input('Digite as preferencias: ')
        id_usuario = input('Digite o id do usuário: ')
        novoPerfil = {
            "foto":foto,
            "bio":bio,
            "preferencias":preferencias,
            "id_usuario":id_usuario
        }
        inserirDadosTabelas(tabela,novoPerfil)

    if opcao =='3':
        tabela = 'biblioteca_autor'
        nome = input('Digite o nome: ')
        genero = input('Digite gênero textual: ')
        nacionalidade = input('Digite a nacionalidade: ')
        
        novoAutor = {
            "nome":nome,
            "genero":genero,
            "nacionalidade":nacionalidade,
        }
        inserirDadosTabelas(tabela,novoAutor)
    if opcao =='4':
        tabela = 'biblioteca_livro'
        titulo = input('Digite o título: ')
        quantidade = int(input('Digite a quantidade: '))
        genero = input('Digite gênero textual: ')
        ano = int(input('Digite o ano: '))
        id_autor = input('Digite o ID do autor')

        novoLivro = {
            "titulo":titulo,
            "quantidade":quantidade,
            "genero":genero,
            "ano":ano,
            "id_autor":id_autor
        }
        inserirDadosTabelas(tabela,novoLivro)
    if opcao =='5':
        tabela = 'biblioteca_emprestimo'
        id_livro = input('Digite o id do livro: ')
        id_usuario = int(input('Digite o id do usuario: '))
        data_entrega = input('Digite a data de entrega: ')


        novoEmprestimo = {
            "id_livro":id_livro,
            "id_usuario":id_usuario,
            "data_entrega":data_entrega,
        }
        inserirDadosTabelas(tabela,novoEmprestimo)





coletarDadosInserir()