# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
#frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

frase = "Cientista de Dados é o profissional mais sexy do século XXI"

print(frase[0:18])

#COMO CONTAR QUANTAS LETRAS TEM NA FRASE?

'''Obs: Antes de achar que o resultado acima está errado, reflita junto comigo:
Em uma corrida ou maratona quem sobre ao podium? Aqueles que ficam nas posições 1, 2 e 3, certo? Existe posição zero? Não! Pois bem!
O exercício acima pede os caracteres nas posições de 1 a 18 (não existe posição zero).
Em Python, a indexação (que representa o índice) começa por zero.
Logo, posições de 1 a 18 estão nos índices de 0 a 18 (pois 18 é exclusivo e portanto temos de 0 a 17, logo 18 posições).'''