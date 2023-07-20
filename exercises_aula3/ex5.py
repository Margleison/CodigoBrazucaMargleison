#Agora, sorteie uma ordem aleatoria de 4 alunos. Leia o nome dos e
#mostre a ordem aleaotira
from random import choices, randint, sample, shuffle 

aluno1 = "Rodrigo"
aluno2 = "Pedro"
aluno3 = "Tony"
aluno4 = "Pri"

alunos = aluno1, aluno2, aluno3, aluno4
 

print(sample(alunos,4))
