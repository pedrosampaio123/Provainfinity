"""Questão 05
Crie um algoritmo que informe o tipo de um valor informado pelo usuário"""
"Resposta:"

nome = int(input('Informe o que você deseja colocar:\n[1] - int'
             '\n[2] - float'
             '\n[3] - str'
                '\n[4] - bool\n'))
if nome == 1:
    numero = int(input('Informe seu numero inteiro: '))
    print(f'O seu numero inteiro é {numero}, da classe {type(numero)}')
elif nome == 2:
    numero_real = float(input('Digite seu numero real: '))
    print(f'O seu numero real é {numero_real}, da classe {type(numero_real)}')
elif nome == 3:
    palavra = input('Digite sua palavra ou frase: ')
    print(f'Sua palavra ou frase foi {palavra}, da classe {type(palavra)}')

elif nome == 4:
    palavra = input('Informe o seu booleano: ').capitalize()
    if palavra == 'True' or palavra == 'False':
        print('O valor informado é booleano')
    else:
        print('O valor informado não é booleano')