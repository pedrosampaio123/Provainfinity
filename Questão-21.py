"""Questão 21
Crie uma função que peça duas notas e retorne a média.
Chame a função para dois alunos e, ao final, some as duas médias."""
"Resposta:"

def nota():
    nota1 = int(input('Informe sua primeira nota: '))
    nota2 = int(input('Informe sua segunda nota:'))
    soma = nota1 + nota2
    media = soma / 2
    return media

aluno1 = nota()
aluno2 = nota()

print(f'A media do aluno 1 foi {aluno1}')
print(f'A media do aluno 2 foi {aluno2}')
soma = aluno1 + aluno2
print(f'A soma das medias foi {soma}')
