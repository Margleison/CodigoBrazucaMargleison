#Faça um programa que leia a altura e a largura de uma parede e calcule sua area,
#mostre quantos litros de tinta sera necessario para pintar sabendo que 1L pinta
#2m quadrados


height = float(input("Insira a altura de sua parede:  "))
width = float(input("Insira a largura de sua parede:  "))

liters_of_paint = (1 / 2)

value = ((height + width) / (liters_of_paint))

print (value)