lista = {
    'corrdor1':["geleia", "leite", "ovo", "alface"],
    'corrdor2':["picles", "chantili", "requeijao", "tomate"],
    'corrdor3':["molho de tomate", "iogurte", "carne", "banana"],
}
   
lista = (["geleia", "leite", "ovo", "alface"],
    ["picles", "chantili", "requeijao", "tomate"],
    ["molho de tomate", "iogurte", "carne", "banana"]
)
a = lista[0]

def search (lista, valor):
    return [
       (lista.index(x), x.index(valor))
            for x in lista
                if valor in x
 ]   

    
a = str(input("Digite o alimento desejado: "))
print(search(lista, a))

print(a)