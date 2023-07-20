#Faça um programa que leia o nome de 4 alunos e escreva na tela o nome do
#aluno escolhido para apagar o quadro
from random import choice, randint, shuffle 

aluno1 = input("qual o aluno 1:  ")
aluno2 = input("qual o aluno 2:  ")
aluno3 = input("qual o aluno 3:  ")
aluno4 = input("qual o aluno 4:  ")

alunos = aluno1, aluno2, aluno3, aluno4
 

print(choice(alunos))