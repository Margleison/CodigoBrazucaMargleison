#Leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse angulo

from math import cos,tan,sin, radians

value_of_user = float(input("Digite um angulo:  "))
print(cos(radians((value_of_user))))
print(tan(radians((value_of_user))))
print(sin(radians((value_of_user))))