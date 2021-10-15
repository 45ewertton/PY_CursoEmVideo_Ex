#Sorteando um aluno "cadastrado" de maneira randomica

import random

aluno_1 = input('Aluno 1: ')
aluno_2 = input('Aluno 2: ')
aluno_3 = input('Aluno 3: ')
aluno_4 = input('Aluno 4: ')

aluno = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = random.choice(aluno)

print (f'O aluno sorteado foi : {sorteado}')