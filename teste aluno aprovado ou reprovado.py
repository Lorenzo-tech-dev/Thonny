disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %disciplina com média final %nota_final no semestr %semestre!' %(disciplina, nota_final,semestre))
else:
    print('Lamento, acho que você precisa estudar mais!')