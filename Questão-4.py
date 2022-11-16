"""Questão 04
Faça um programa que solicite a nota das 4 provas de um aluno e responde a sua média."""
"Resposta:"
soma = 0
for i in range(1,5):
    nota = int(input(f'Digite a nota da sua {i}° prova: '))
    soma += nota

media = soma / 4
print(f'A sua média final é {media}.')

