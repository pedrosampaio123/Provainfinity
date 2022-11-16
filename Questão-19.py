"""Questão 19
Crie uma função para cada operação básica (soma, subtração, multiplicação e divisão).
Os cálculos serão baseados em dois números que o usuário informar"""
"Resposta:"

num1 = int(input('Informe seu 1° numero:' ))
num2 = int(input('Informe seu 2° numero:' ))


def soma(num1,num2):
    soma = num1 + num2
    return soma


print(f'A soma desses numeros é {soma(num1,num2)}.')


def subtracao(num1,num2):
    subtracao = num1 - num2
    return subtracao


print(f'A subtração desses numeros é {subtracao(num1,num2)}.')


def multiplicacao(num1,num2):
    multiplicacao = num1 * num2
    return multiplicacao


print(f'A multiplicação desses numeros é {multiplicacao(num1,num2)}.')


def divisao(num1,num2):
    divisao = num1/num2
    return divisao


print(f'A divisão desses numeros é {divisao(num1,num2)}.')


