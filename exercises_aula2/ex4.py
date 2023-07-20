#Calcule um aumento de 15% no salario de um funcionario

value_of_user = float(input("Coloque o valor de seu salario:  ")) # 1000

porc = (15 * value_of_user / 100) 
print("seu aumento foi de:  ", porc)
aumento = (value_of_user + porc) 

print("seu valor cheio é:  ", aumento )