#Faça um programa que verifique se o numero digitado é par

num = int(input("Coloque um numero de sua escolha:  "))
print("O número é par" * (num % 2 == 0))