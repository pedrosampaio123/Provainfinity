"""Questão 13
Pedir 10 números, se o número for par, vai para uma lista,
se for impar, vai para outra lista.
Ao final, mostrar as duas listas, a soma dos pares,
a soma dos impares e a soma das duas listas"""
"Resposta:"

listapar = []
listaimpar = []

for i in range(1,11):
    num = int(input(f'Digite o seu {i}° numero: '))
    if num % 2 == 0:
        listapar.append(num)
    elif num % 2 != 0:
        listaimpar.append(num)
print(listapar)
print(listaimpar)
print(sum(listapar))
print(sum(listaimpar))
print(sum(listapar) + sum(listaimpar))
