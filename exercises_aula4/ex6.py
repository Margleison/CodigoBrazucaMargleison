#Escreva um codigo que pergunte o salario de um funcionario e de um aumento de 15% caso o salario for maior que 1250
#caso contrario 10%
value_of_user = float(input("Coloque o valor de seu salario:  ")) # 1000

if value_of_user >= 1250: 
    porcentage_maior =  (15 * value_of_user / 100)
    aumento = (value_of_user + porcentage_maior)
    print("seu aumento foi de:  ", porcentage_maior)
    print("seu valor cheio é:  ", aumento )
elif value_of_user <= 750: 
    porcentage_maior1 =  (20 * value_of_user / 100)
    aumento = (value_of_user + porcentage_maior1)
    print("seu aumento foi de:  ", porcentage_maior1)
    print("seu valor cheio é:  ", aumento )
else: 
    porcentage_menor = (10* value_of_user / 100)
    aumento = (value_of_user + porcentage_menor)

    print("seu aumento foi de:  ", porcentage_menor)
    print("seu valor cheio é:  ", aumento )
    



