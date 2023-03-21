'''
Departamento de Inteligência de Dados (DID) -
    Um departamento focado na coleta, análise e interpretação de dados para fornecer inteligência estratégica.
'''

import PySimpleGUI as sg
import csv, threading
import os,datetime,sys

filename = 'database.csv'

# Verificando se o arquivo já existe
if not os.path.isfile(filename):
    # Se o arquivo não existir, cria ele
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Data de criacao','Nome','Sexo','Data de Nascimento','Nacionalidade',
                         'Endereço','Telefone','Email','Historico Profissional','Historico Educacional',
                         'Antecedentes Criminais','Comportamento','Rotina','Personalidade','Associacoes','Financas'])

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

# Define a função para criar a pagina de Buscar Registro
def criar_pagina_buscar_registro():
    with open(filename, mode='r') as csv_file:
        # Lê o arquivo CSV como um dicionário
        csv_reader = csv.DictReader(csv_file)

        # Cria uma lista de nomes de registro
        nomes, linhas = [], []

        colunas = csv_reader.fieldnames

        # Decodifica e adiciona os nomes na lista
        for row in csv_reader:
            nome = row['Nome']
            nomes.append(nome)
            linhas.append(row)

        layout = [
            [
                sg.Column([
                    [sg.Listbox(values=nomes, size=(30, 20), key='-LISTA-')],
                ]),
                sg.Column(layout=[[sg.Text(size=(50, 20), key='-DADOS-')]], element_justification='center')
            ], [sg.Button('Buscar', key='-BUSCAR-')]
        ]

        window = sg.Window('Buscar Registros', layout, finalize=True)
        window.make_modal()

    # Loop principal da janela
    while True:
        print('hi')
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == '-BUSCAR-':
            # Obtém o registro selecionado
            nome = values['-LISTA-'][0]

            # Procura o registro no arquivo CSV
            with open('database.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row['Nome'] == nome:
                        # Decodifica os dados do registro
                        sexo = (row['Sexo'])
                        data_nascimento = (row['Data de Nascimento'])
                        nacionalidade = (row['Nacionalidade'])
                        endereco = (row['Endereço'])
                        telefone = (row['Telefone'])
                        email = (row['Email'])
                        historico_profissional = (row['Historico Profissional'])
                        historico_educacional = (row['Historico Educacional'])
                        antecedentes_criminais = (row['Antecedentes Criminais'])
                        comportamento = (row['Comportamento'])
                        rotina = (row['Rotina'])
                        personalidade = (row['Personalidade'])
                        associacoes = (row['Associacoes'])
                        financas = (row['Financas'])

                dados = f'Nome: {nome}\nSexo: {sexo}\nData de Nascimento: {data_nascimento}\nNacionalidade: {nacionalidade}\nEndereço: {endereco}\nTelefone: {telefone}\nEmail: {email}\nHistórico Profissional: {historico_profissional}\nHistórico Educacional: {historico_educacional}\nAntecedentes Criminais: {antecedentes_criminais}\nComportamento: {comportamento}\nRotina: {rotina}\nPersonalidade: {personalidade}\nAssociais: {associacoes}\nFinanças: {financas}'
                print(dados)
                window['-DADOS-'].update(dados)

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
janela = sg.Window('Departamento de Inteligência de Dados', layout)

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
            elif evento_nova_janela == "Salvar":
                data_criacao    = datetime.date.today()
                nome            = (valores_nova_janela['nome'])
                sexo            = (valores_nova_janela['sexo'])
                data_nascimento = (valores_nova_janela['data_nascimento'])
                nacionalidade   = (valores_nova_janela['nacionalidade'])
                endereco        = (valores_nova_janela['endereco'])
                telefone        = (valores_nova_janela['telefone'])
                email           = (valores_nova_janela['email'])
                historico_profissional  = (valores_nova_janela['historico_profissional'])
                historico_educacional   = (valores_nova_janela['historico_educacional'])
                antecedentes_criminais  = (valores_nova_janela['antecedentes_criminais'])
                comportamento           = (valores_nova_janela['comportamento'])
                rotina                  = (valores_nova_janela['rotina'])
                personalidade           = (valores_nova_janela['personalidade'])
                associacoes             = (valores_nova_janela['associacoes'])
                financas                = (valores_nova_janela['financas'])

                # Abrindo o arquivo no modo de adição de novas linhas
                with open(filename, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([data_criacao,nome,sexo,data_nascimento,nacionalidade,endereco,telefone,
                                     email,historico_profissional,historico_educacional,
                                     antecedentes_criminais,comportamento,rotina,personalidade,
                                     associacoes,financas])

            elif evento_nova_janela == "Cancelar":
                break

            # Adicione aqui o código para processar os eventos da página de Novo Registro
        nova_janela.close()

    elif evento == 'Buscar Registros':
        criar_pagina_buscar_registro()

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
