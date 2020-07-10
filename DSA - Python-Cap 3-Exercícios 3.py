# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento
#da tupla por 2 e guarde os resultados em uma lista.

elemento = 0

for t in range(0,4):
    tupla = int(input('Digite 4 numeros:'))
    elemento += tupla * 2
    
lista = []

lista.append(elemento)

print(lista)
    
