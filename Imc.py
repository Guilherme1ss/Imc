import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [ [sg.Text('Digite o seu peso em Kg:'), sg.InputText(key='peso', enable_events=True)],
           [sg.Text('Digite a sua altura em metros:'), sg.InputText(key='altura', enable_events=True)],
           [sg.Button('Calcular', bind_return_key=True)],
           [sg.Text('IMC: ', key='resultado'), sg.Text('Status: ',key='status')] ]

window = sg.Window('Calculadora de IMC', layout, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calcular':
        try:
            peso = float(values['peso'].replace(",", '.'))
            altura = float(values['altura'].replace(',', '.'))
            imc = peso / (altura ** 2)
            if imc <= 18.5:
                nivelImc = ("Abaixo do peso")
            elif imc > 18.5 and imc <= 24.9:
                nivelImc = ("Normal")
            elif imc > 24.9 and imc <= 29.9:
                nivelImc = ("Sobrepeso")
            elif imc > 29.9 and imc <= 34.9:
                nivelImc = ("Obesidade grau 1")
            elif imc > 34.9 and imc <= 39.9:
                nivelImc = ("Obesidade grau 2")
            elif imc >= 40:
                nivelImc = ("Obesidade mórbida.")
            window['resultado'].update(f'IMC: {imc:.2f}')
            window['status'].update(f'Status: {nivelImc}')
        except ValueError:
            sg.popup_error('Entrada inválida. Certifique-se de que os campos de entrada contenham números válidos.')
    elif event == 'peso' or event == 'altura':
        if values[event] and values[event][-1] == '\n':
            window['Calcular'].click()

window.close()