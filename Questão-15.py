"""Questão 15
Solicite a idade de 5 pessoas e ao final conte quantas pessoas são maiores de idade,
a soma de todas as idades, a média das idades, o valor máximo, o valor mínimo,
ordene de forma crescente e decrescente."""
"Resposta: "

listaidade = []
listamaioridade = []
for i in range(1,6):
    idade = int(input('Digite sua idade: '))
    listaidade.append(idade)
    if idade >= 18:
        listamaioridade.append(idade)

print(f'O numero de pessoas que são de maior idade são {len(listamaioridade)} pessoas.')
print(f'A soma de todas as idades é {sum(listaidade)} anos.')
media = sum(listaidade)/len(listaidade)
print(f'A média de todas as idades é {media}')
print(f'Esse é o valor mais alto das idades {max(listaidade)}')
print(f'Esse é o valor mais baixo das idades {min(listaidade)}')
print(sorted(listaidade))
print(sorted(listaidade , reverse=True))
