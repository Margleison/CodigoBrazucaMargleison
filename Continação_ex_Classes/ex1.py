class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name:  {self.name} Age: {self.age}"
    #Getter Function
    @classmethod
    def get(cls):
        name = input("Name:  ")
        age = int(input("Age:  "))
        return cls(name, age)



def main():
    aluno1 = Student.get()
    print(aluno1)



if __name__ == "__main__":
    main()


    #Getter Function
  #"""@property
    #def name(self):
        #return self._name

    #Setter Function
    #@name.setter
    #def name(self, name):
       #if isinstance(name, str):
            #self._name = name
        #else: 
            #raise ValueError: