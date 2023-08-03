class Dogloco:
    def __init__(self, dog_name, dog_age):
        self.name = dog_name
        self.age = dog_age

def main():
    pit = get_dog()
    pit_2 = get_dog()
    print(f"O {pit.name} tem {pit.age} anos")
    print(f"O {pit_2.name} tem {pit_2.age}")

def get_dog():
    dog_name = input("Qual o nome do seu cachorro:  ")
    dog_age = int(input("Qual a idade do seu cachorro"))
    return Dogloco(dog_name, dog_age)


if __name__=="__main__":
    main()

