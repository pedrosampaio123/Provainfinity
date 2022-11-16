"""Questão 07
07. Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em graus Fahrenheit.
07.1 Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius."""
"Resposta 7: "

temp = float(input('Digite sua temperatura em celsius:'))
fahrenheit = (1.8 * temp) + 32
print(f'Sua temperatura em graus Fahrenheit é {fahrenheit}')


"Resposta 7.1:"

temp = float(input('Digite sua temperatura em Fahrenheit: '))
celsius = (temp - 32) / 1.8
print(f'Sua temperatura em graus celsius é {celsius}')