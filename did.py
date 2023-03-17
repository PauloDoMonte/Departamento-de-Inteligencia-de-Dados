'''
Departamento de Inteligência de Dados (DID) -
    Um departamento focado na coleta, análise e interpretação de dados para fornecer inteligência estratégica.
'''

import PySimpleGUI as sg
import csv
from cryptography.fernet import Fernet
import os

chave = b'_Zzvy_C7ejhK-bHtoYFb1GdS6T7MclIlzJ6UVEZ6UvI='
fernet = Fernet(chave)

filename = 'database.csv'

# Verificando se o arquivo já existe
if not os.path.isfile(filename):
    # Se o arquivo não existir, cria ele
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([fernet.encrypt('Data de criacao'.encode()),
                         fernet.encrypt('Nome'.encode()), fernet.encrypt('Sexo'.encode()),
                         fernet.encrypt('Data de Nascimento'.encode()), fernet.encrypt('Nacionalidade'.encode()),
                         fernet.encrypt('Endereço'.encode()),fernet.encrypt('Telefone'.encode()),
                         fernet.encrypt('Email'.encode()),fernet.encrypt('Historico Profissional'.encode()),
                         fernet.encrypt('Historico Educacional'.encode()),fernet.encrypt('Antecedentes Criminais'.encode()),
                         fernet.encrypt('Comportamento'.encode()),fernet.encrypt('Rotina'.encode()),
                         fernet.encrypt('Personalidade'.encode()),fernet.encrypt('Associacoes'.encode()),
                         fernet.encrypt('Financas'.encode())])


# Define a função para criar a página de Novo Registro
def criar_pagina_novo_registro():
    layout = [
        [sg.Text('Novo Registro')],
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('Sexo'), sg.Combo(['Masculino', 'Feminino'], key='sexo')],
        [sg.Text('Data de Nascimento'), sg.Input(key='data_nascimento')],
        [sg.Text('Nacionalidade'), sg.Input(key='nacionalidade')],
        [sg.Text('Endereço'), sg.Input(key='endereco')],
        [sg.Text('Telefone'), sg.Input(key='telefone')],
        [sg.Text('E-mail'), sg.Input(key='email')],
        [sg.Text('Histórico Profissional'), sg.Input(key='historico_profissional')],
        [sg.Text('Histórico Educacional'), sg.Input(key='historico_educacional')],
        [sg.Text('Antecedentes Criminais'), sg.Input(key='antecedentes_criminais')],
        [sg.Text('Comportamento'), sg.Input(key='comportamento')],
        [sg.Text('Rotina'), sg.Input(key='rotina')],
        [sg.Text('Personalidade'), sg.Input(key='personalidade')],
        [sg.Text('Associais'), sg.Input(key='associacoes')],
        [sg.Text('Finanças'), sg.Input(key='financas')],
        [sg.Button('Salvar'), sg.Button('Cancelar')],
    ]
    return sg.Window('Novo Registro', layout)

# Define a função para criar a página de Buscar Registros
def criar_pagina_buscar_registros():
    layout = [
        [sg.Text('Buscar Registros')],
        # Adicione aqui os elementos para buscar registros
    ]
    return sg.Window('Buscar Registros', layout)

# Define a função para criar a página de Atualizar Registros
def criar_pagina_atualizar_registros():
    layout = [
        [sg.Text('Atualizar Registros')],
        # Adicione aqui os elementos para atualizar registros
    ]
    return sg.Window('Atualizar Registros', layout)

# Define a função para criar a página de Reconhecimento Webcam
def criar_pagina_reconhecimento_webcam():
    layout = [
        [sg.Text('Reconhecimento Webcam')],
        # Adicione aqui os elementos para reconhecimento por webcam
    ]
    return sg.Window('Reconhecimento Webcam', layout)

# Define o layout da janela principal
layout = [
    [sg.Text('Departamento de Inteligência de Dados')],
    [sg.HorizontalSeparator()],
    [sg.Button('Novo Registro'), sg.Button('Buscar Registros'), sg.Button('Atualizar Registros'), sg.Button('Reconhecimento Webcam')],
    [sg.HorizontalSeparator()],
    [sg.Text('Página Atual')],
    [sg.Frame('', layout=[], key='pagina')],
]

# Cria a janela principal com o layout definido
janela = sg.Window('Minha Aplicação', layout)

# Loop principal do programa
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Novo Registro':
        nova_janela = criar_pagina_novo_registro()
        while True:
            evento_nova_janela, valores_nova_janela = nova_janela.read()
            if evento_nova_janela == sg.WINDOW_CLOSED:
                break
            if evento_nova_janela == "Salvar":
                nome = fernet.encrypt(valores_nova_janela['nome'].encode())
                sexo = fernet.encrypt(valores_nova_janela['sexo'].encode())
                data_nascimento = fernet.encrypt(valores_nova_janela['data_nascimento'].encode())
                nacionalidade = fernet.encrypt(valores_nova_janela['nacionalidade'].encode())
                endereco = fernet.encrypt(valores_nova_janela['endereco'].encode())
                telefone = fernet.encrypt(valores_nova_janela['telefone'].encode())
                email = fernet.encrypt(valores_nova_janela['email'].encode())
                historico_profissional = fernet.encrypt(valores_nova_janela['historico_profissional'].encode())
                historico_educacional = fernet.encrypt(valores_nova_janela['historico_educacional'].encode())
                antecedentes_criminais = fernet.encrypt(valores_nova_janela['antecedentes_criminais'].encode())
                comportamento = fernet.encrypt(valores_nova_janela['comportamento'].encode())
                rotina = fernet.encrypt(valores_nova_janela['rotina'].encode())
                personalidade = fernet.encrypt(valores_nova_janela['personalidade'].encode())
                associacoes = fernet.encrypt(valores_nova_janela['associacoes'].encode())
                financas = fernet.encrypt(valores_nova_janela['financas'].encode())

                # Abrindo o arquivo no modo de adição de novas linhas
                with open(filename, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([nome,sexo,data_nascimento,nacionalidade,endereco,telefone,
                                     email,historico_profissional,historico_educacional,
                                     antecedentes_criminais,comportamento,rotina,personalidade,
                                     associacoes,financas])

            # Adicione aqui o código para processar os eventos da página de Novo Registro
        nova_janela.close()

    elif evento == 'Buscar Registros':
        nova_janela = criar_pagina_buscar_registros()
        while True:
            evento_nova_janela, valores_nova_janela = nova_janela.read()
            if evento_nova_janela == sg.WINDOW_CLOSED:
                break
            # Adicione aqui o código para processar os eventos da página de Buscar Registros
        nova_janela.close()

    elif evento == 'Atualizar Registros':
        nova_janela = criar_pagina_atualizar_registros()
        while True:
            evento_nova_janela, valores_nova_janela = nova_janela.read()
            if evento_nova_janela == sg.WINDOW_CLOSED:
                break
            # Adicione aqui o código para processar os eventos da página de Atualizar Registros
        nova_janela.close()

    elif evento == 'Reconhecimento Webcam':
        nova_janela = criar_pagina_reconhecimento_webcam()
        while True:
            evento_nova_janela, valores_nova_janela = nova_janela.read()
            if evento_nova_janela == sg.WINDOW_CLOSED:
                break
            # Adicione aqui o código para processar os
        nova_janela.close()

janela.close()
