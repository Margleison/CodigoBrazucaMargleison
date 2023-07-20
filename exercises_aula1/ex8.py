#Faça um programa que leia um numero e diga se É PAR OU IMPAR 
num = int(input("Coloque um numero de sua escolha:  "))
print("O número é par" * (num % 2 == 0), "O número é ímpar" *  (num % 2 != 0))
