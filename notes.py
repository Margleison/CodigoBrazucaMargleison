#"\n" = new line
#tuplas-> usadas para quando nao se quer alterar o valor

#raiz quadra
import math

print(math.sqrt())

#raiz cubica
import math

print(math.cbrt())

#importar funçao especifica, caso queira mais alguma, apenas acrescentar virgula

from math import sqrt

#biblioteca para qualquer coisa que precise ser aleatoria como se fosse um sorteador de numeros
import random 
num = random.randint

#si, se não, então
#(If)= si
#( : )Então ->
print("start")

if True:
    print("True")

print("Is")    

#como indentificar algo especifico com o ( if, (else), elif->(se não,se) )

name = input("Say your name:  ")
if name == "Rodrigo":  #if->(se)
    print("Nice to meet you!")
elif name == "Pedro":  #Elif->(se este codigo nao rodar e rode este!)
    print("Hi, Pedro!")
else:
    print("You are not Rodrigo")   
print(f"Hello, {name}")   

#por que nao usar 2 ifs? -> por que sempre ira printar os dois e não apenas o correto
score = int(input("Whats score"))

if score > 7:
    print(f"You get an B")
if score > 9:
    print(f"You get an A")
    
#Condicoes aninhadas

alunos = ["Magrin", "david", "drey"]
for aluno in range(len(alunos)):
    print(aluno+ 1, alunos[aluno])

#Como e quando usar o while
p = int(input("Qual sua idade?:  "))

while p != 0:
    print(f"Voce digitou{p}")
    p = int(input("Qual sua idade?:  "))

print("FIM")

#Validando informação com while
sexo = str(input("Qual o seu sexo [M/F]:  ")).upper# upper é uma função que transforma minusculo em maiusculo 

while sexo not in "MF":
    print("Digite um valor valido.")
    sexo = str(input("Qual o seu sexo [M/F]:  "))

print(f"O seu sexo é {sexo}")

#Como adicionar valores a uma lista atraves do while
pares = []
impares = []

while True:
    n = int(input("Digite um valor:  "))
    if n == 0: 
        break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if n == 0: 
        break

print(pares)
print("----")
print(impares)


#Usando (def) para criar funções

def dobra(x):
    print(f"O valor dobrado é{x}")

dobra(2)

#Usando def e main na criação de funçoes

def main(): #Estudar mais sobre como funciona e para que serve
    numero_dobrado = dobra(4)
    print(f"o numero dobrado é {numero_dobrado}")
    
def dobra(x=1):
    return x*2
main()


#Para passar valores que nao foram especificos
def test(*args):
    print(args)


test(1, 2, 3, 4, "Rodrigo")

#Para passar valores que nao foram especificos
def test(*args):
    for i in args:
        print(i)


test(1, 2, 3, 4, "Rodrigo", 5)


#Para desempacotar os valores da lista
lista = [1, 2, 3, 4, 5]
n1, n2, *n= lista
print(*lista )


#como trasformas a tupla com valor args em lista
def test(*args):
    print(args)
    args = lista(args)
    args[0] = 99

print("")

#*args= argumentos ////// **kwargs= keywordarguments or idade.kwargs.get("idade")
def test(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["idade"]) #-> aceita varios argumentos adicionados a chave.



lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2, nome= "Rodrigo", idade= 21)
