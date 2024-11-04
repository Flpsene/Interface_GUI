import PysimpleGUI  as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='Usuário')],
    [sg.Text('Senha'),sg.Input(key='Senha',password_char='*')],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]

]
#janela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read
    if eventos == sg.WINDOW_CLOSED: 
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'Sene' and valores ['Senha'] == '1234567890':
            print('Bem vindo ao meu código!')




