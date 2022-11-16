"""Questão 18
Crie uma tupla com a latitude e longitude de uma cidade e depois imprima em tela.
Edite a tupla anterior com os valores de outra cidade e imprima novamente."""
"Resposta:"
tupla = (-23.588254,-46.632477)
print(tupla)
lista = list(tupla)
lista2 = [-46.632477,-23.588254]
tupla = lista2
print(tuple(tupla))