# Calculadora (com While)

import os
import time

while True:
    print('Calculadora')
    num1 = input('Digite um número: ') # Solicita ao usuário um número
    num2 = input('Digite outro número: ') # Solicita ao usuário um outro número
    operador = input('Escolha o operador (+-*/): ') # Solicita ao usuário o operador

    numeros_validos = None # Variavel que vai verificar se foi digitado número no input

    try:
        numero1 = float(num1) # Vai transformar o str em float
        numero2 = float(num2) # Vai transformar o str em float
        numeros_validos = True # Vai validar a variavel que verifica se foi digitado números
    except:
        numeros_validos = None # Ela ficará None caso não seja digitado um número

    if numeros_validos is None:
        print('Número digitado inválido!')
        time.sleep(2)
        os.system('cls') # Limpa a Tela
        continue # Voltará para o início do código

    os.system('cls') # Limpa a Tela

    if operador == '+':
        print(f'{num1} {operador} {num2} = {numero1 + numero2}') # Realiza a soma
    elif operador == '-':
        print(f'{num1} {operador} {num2} = {numero1 - numero2}') # Realiza a subtração
    elif operador == '*':
        print(f'{num1} {operador} {num2} = {numero1 * numero2}') # Realiza a multiplicação
    elif operador == '/':
        print(f'{num1} {operador} {num2} = {numero1 / numero2:.2f}') # Realiza a divisão
    else:
        print('Operador inválido') # Caso nenhum operador válido tenha sido digitado

    sair = input('Quer sair?\n[s] Sim [n] Não\n')
    sair = sair.lower() # Vai tornar a String em minuscula
    sair = sair.startswith('s') # Vai verificar se a str 'sair' começa com 's'
    os.system('cls') # Limpa a Tela

    if sair is True:
        break