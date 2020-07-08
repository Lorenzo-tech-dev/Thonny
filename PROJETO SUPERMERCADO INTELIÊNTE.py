'''08/07/2020 13:24 Criar uma matriz e as chaves serão os produtos de uma prateleira(5 linhas) com (5 produtos).
Criar uma variável de pesquisa e a pessoa pesquisa sabonete, para saber se existe o sabonete e em qual corredor ele está!'''

lista = [
     ["geleia", "leite", "ovo", "alface"],
    ["picles", "chantili", "requeijao", "tomate"],
    ["molho de tomate", "iogurte", "carne", "banana"]
]
a = lista[0]
'''
def search (lista, valor):
    return [
       (lista.index(x), x.index(valor))
            for x in lista
                if valor in x
    ]
a = str(input("Digite o alimento desejado: "))
print(search(lista, a))
'''
print(a)