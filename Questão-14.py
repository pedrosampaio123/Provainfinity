"""Questão 14
Programa para cálculo
 de IMC e ao final informar em qual categoria o usuário se encontra."""
"Resposta: "
print('Calculo do Imc')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
print(f"O seu imc foi {imc}.")

if imc < 18.5:
    print('Baixo peso!')
elif imc > 18.5 and imc <= 24.9:
    print('Peso normal')
elif imc > 25 and imc <= 29.9:
    print('Excesso de peso!')
elif imc > 30 and  imc <= 35:
    print('Obesidade Classe 1')
elif imc > 35 and imc <= 35.9:
    print('Obesidade classe 2')
elif imc >= 40:
    print('Obesidade Classe 3')
