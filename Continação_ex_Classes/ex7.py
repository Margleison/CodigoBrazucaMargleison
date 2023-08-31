#7 Crie uma classe Employee com atributos name, position e salary. Adicione um método apply_raise que aumenta o salário do 
# funcionário em uma determinada porcentagem.

class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    @classmethod
    def apply_raise(cls):
        print("Passe seus dados abaixo.")
        print("Cargos",
              "Gerente = 1 /",
              "Atendente = 2 /",
              "Garçom = 3")

        name = input("Nome: ")
        position = int(input("Cargo na empresa: "))
        salary = float(input("Seu salario atual: "))
        
        if name == "rodrigo":
            aumento_gerente = 70 * salary / 100
            print(f"Voce teve teve um aumento de 70%, por que vc merece, seu salario reajustado ficou em {aumento_gerente + salary}")
        elif position == 1:
            aumento_gerente = 15 * salary / 100
            print(f"Voce teve teve um aumento de 15%, seu salario reajustado ficou em {aumento_gerente + salary}")
        elif position == 2:
            aumento_atendente = 10 * salary / 100
            print(f"Voce teve teve um aumento de 10%, seu salario reajustado ficou em {aumento_atendente + salary}")
        elif position == 3:
            aumento_garçom = 5 * salary / 100
            print(f"Voce teve teve um aumento de 5%, seu salario reajustado ficou em {aumento_garçom + salary}")
        return cls(name, position, salary)
        
def main():
    funcionario = Employee.apply_raise()


if __name__ == "__main__":
    main()