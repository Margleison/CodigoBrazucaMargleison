#6 Desenvolva uma classe Book com atributos title, author e year. Implemente um método get_age que retorna quantos anos o 
#livro tem desde o ano atual.

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def get_age(cls):
        print("Passe as devidas informações sobre seu livro")
        title = input("Digite o titulo: ")
        author = input("Diga o nome do autor: ")
        year = int(input("Digite o ano em que seu livro foi feito:  "))
        Year_creator = 2023 - year
        print(f"Seu livro foi criado a [{Year_creator}] anos atrás. Parabens, esta super conservado!")
        return cls(title, author, year)
    

def main():
    livro = Book.get_age()
    livro


if __name__ == "__main__":
    main()