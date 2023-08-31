#5 Defina uma classe Car com atributos make, model e year. Crie um método start_engine que imprime uma mensagem indicando que o motor foi iniciado.
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 

    @classmethod
    def start_engine(cls):
        print("Escolha seu carro atraves do dados passados.")
        make = input("Defina o veiculo desejado:  ")
        model = input("Defina a fabricadora do veiculo:  ")
        year = int(input("Defina o ano do veiculo:  "))
        return cls(make, model, year)
    
    def __str__(self):
        return f"O veiculo {self.make}, de fabricadora {self.model}, e ano {self.year}", 


def main():
    car = Car.start_engine()
    print(car)


if __name__ == "__main__":
    main()
        