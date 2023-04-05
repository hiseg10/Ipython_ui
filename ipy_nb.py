import PySimpleGUI as sg
from IPython.terminal.embed import InteractiveShellEmbed
from IPython.utils import io


def run_code():
    ipshell = InteractiveShellEmbed()
    window = create_window()
    output_elem = window['-OUTPUT-']

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        elif event == 'Executar':
            # Captura a saída do IPython
            with io.capture_output() as captured:
                # Executa o código no console IPython
                ipshell.run_cell(values['-CODE-'])
            output = captured.stdout
            # Atualiza o elemento de saída com a saída do IPython
            output_elem.update(value=output)

    window.close()

def create_window():
    sg.theme('DarkGrey2')

    layout = [[sg.Text('Insira o código que deseja executar:')],
              [sg.Input(key='-CODE-')],
              [sg.Button('Executar'), sg.Button('Sair')],
              [sg.Text('Saída:')],
              [sg.Output(size=(80,20), key='-OUTPUT-')]]

    window = sg.Window('Executar código no IPython', layout)

    return window

run_code()

