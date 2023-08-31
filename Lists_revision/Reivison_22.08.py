#Crie programa que simule uma corrida entre dois carros, onde os carros avancam a cada iteração do loop
#O carro A e o carro B comecam na posicao 0. Cada carro avanca uma distancia aleatoria entre 1 e 5. O carro que
#atingir a posição de 30 primeiro é declarado vencedor
from random import randint 


posição_A = 0
posição_B = 0
while posição_A <= 30 and posição_B <=30:
    avanço_A = randint(1, 5)
    posição_A += avanço_A

    avanço_B = randint(1, 5)
    posição_B += avanço_B 
    print(f"O carro A avançou {avanço_A} unidades. Posição:{posição_A}")
    print(f"O carro A avançou {avanço_B} unidades. Posição:{posição_B}")

if posição_A >= 30:
    print("Carro A venceu!")

else:
    print("O carro B venceu")