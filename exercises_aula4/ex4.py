m1 = int(input("Digite um valor:  "))
m2= int(input("Digite um valor:  "))
m3 = int(input("Digite um valor:  "))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print("As medidas citadas podem formar um triangulo.")
else:
    print("As medidas citadas nao podem formar um triangulo")