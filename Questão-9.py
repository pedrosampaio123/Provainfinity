"""Questão 09
Crie um algoritmo que indique se um número é par ou impar"""
"Resposta:"

num = int(input('Digite um numero e veja se o mesmo é par ou impar: '))
if num % 2 == 0:
    print(f'O numero {num} é par!')
elif num % 2 != 0:
    print(f'O numero {num} é impar!')

