"""Questão 20
Crie uma função que vai informar se o número é positivo ou negativo."""
"Resposta:"

def positivo_negativo(num):
    if num > 0:
        print(f'O número {num} é positivo!')
    elif num < 0:
        print(f'O número {num} é negativo!')
    else:
        print(f'O número {num} é positivo!')


positivo_negativo(-4)