"""
Escreva uma função chamada calculadora que aceita três argumentos:

    número1 (um número)
    número2 (um número)
    operador (uma string que pode ser "+", "-", "*", ou "/")

Desafio Extra

Inclua tratamento de erros na sua função para lidar com:

    Divisão por zero.
    Operadores inválidos.
"""


def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2

    elif operador == '-':
        return num1 - num2

    elif operador == '*':
        return num1 * num2

    elif operador == '/':
        if num2 == 0:
            return 'Não é possivel fazer divisão por 0'

        else:
            return num1 / num2

    else:
        return 'Operador inválido'

print(calculadora(5, 6, '.'))
