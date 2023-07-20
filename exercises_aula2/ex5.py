#Faça um programa que leia o preço e retorne o valor com 5% de desconto

value_of_product = float(input("Digite o valor do produto:  "))

descount = (5 * value_of_product / 100)
valor_inteiro = (value_of_product - descount)
print("seu desconto é de:  ", -descount)

print("O valor ficou em:  ",  valor_inteiro)