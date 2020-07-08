# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

nome_idade = {"Sara":11, "Claudia":43, "Jefferson":45}

nome_idade["Antunes"] = 19

print(nome_idade)

#ou de forma dificil 

a = {"Antunes":19}

nome_idade.update(a)

nome_idade.update({"Lorenzo":18})

print(nome_idade)