import regex


class Cpf: 
    CPF_LENGHT = 11
    value = ''
    def __init__(self, value: str):
        error_msg = self.validate(value)
        if error_msg != 'OK':
            raise Exception(error_msg)
        self.value = value
    
    
    def _all_char_same(cls, param: str)->bool:
        if param.count(first_dig) == self.CPF_LENGHT:
            return 
    
    @classmethod
    def _remove_special_chars(cls, param)->str:
        param = regex.sub(r'\D', '', param)

    @classmethod
    def _make_first_dig(cls, param)->str:
        return '0'
    
    @classmethod
    def _make_second_dig(cls, param)->str:
        return '0'
    
    
    
    def validate(self, param)-> str:
        param = param or ''
        if (param == ''):
            return f'CPF Vazio'
        
        param = self._remove_special_chars(param)
        if len(param) != self.CPF_LENGHT:
            return f'CPF com tamanho diferente de {self.CPF_LENGHT}'
        
        first_dig = param[0]
        if self._all_char_same(param) == True:
            return f'Cpf invalido pois todos digitos são iguais'
        
        first_verify_dig = self._make_first_dig(param[0:9])
        if first_verify_dig != param[9]
            return f'Cpf invalido pois todos digitos são iguais'
        
        second_verify_dig = self._make_second_dig(param[0:10])
        if second_verify_dig != [10]:
            return f'Cpf invalido pois todos digitos são iguais'
        
        
        
        return 'OK'
        
        
        
cpf_a_validar = 'xxxxxxxxxxx'
cpf = Cpf(cpf_a_validar)
        
        
    




