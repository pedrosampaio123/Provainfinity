"""Questão 10
Peça 5 números e informe a soma e o maior número (OBS: sem utilizar listas)"""
"Resposta:"
soma = 0
maior = 0
for i in range(1,6):
    num = int(input(f'Digite o seu {i}° numero: '))
    if num > maior:
        maior = num
    soma += num
print(f"A soma dos seus numeros foi {soma}.")
print(f'O maior número digitado foi {maior}.')

