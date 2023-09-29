class Cpf:
    value = ''

    def __init__(self, param= str):
        self.value = param

    
    def validate(self)-> bool:
        return True

class Cpf2:
    def validate(self, param: str)->bool:
        return True

class Cpf3:
    @staticmethod
    def validate(param: str)-> bool:
        return True






cpf_a_validar = 'xxxxxxxxxxx'
cpf = Cpf(cpf_a_validar)
print(cpf.validate)

cpf = Cpf2()
print(cpf.validate(cpf_a_validar))

print(Cpf3.validate(cpf_a_validar)) # melhor forma de programar orientado a objetos.