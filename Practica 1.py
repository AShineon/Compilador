#Erick Alberto Mancillas Magdaleno
#Modulo 1 - Práctica 2
#Compiladores D03
#git add . -> git commit -> git push.
#Esta es la rama principal (main)

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, {self.valor})"

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.caracter_actual = self.texto[self.pos] if self.texto else None
        
        self.operadores = {'+', '-', '*', '=', '/','(', ')'}
        
        self.caracteres_prohibidos = {
            '$', '#', '@', '\\', '|', ':', ';', '.', ',', 
            '?', '!', '&', '<', '>', ' '
        }

    def avanzar(self):
        self.pos += 1
        if self.pos < len(self.texto):
            self.caracter_actual = self.texto[self.pos]
        else:
            self.caracter_actual = None

    def _saltar_espacios(self):
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()

    def _leer_numero(self):
        num_str = ''
        while self.caracter_actual is not None and self.caracter_actual.isdigit():
            num_str += self.caracter_actual
            self.avanzar()
        return Token('NUM', int(num_str))

    def _leer_identificador(self):
        id_str = ''
        while self.caracter_actual is not None and (self.caracter_actual.isalnum() or self.caracter_actual == '_'):
            id_str += self.caracter_actual
            self.avanzar()
        return Token('ID', id_str)

    def tokenizar(self):
        tokens = []
        while self.caracter_actual is not None:
            
            if self.caracter_actual.isspace():
                self._saltar_espacios()
                continue
            
            if self.caracter_actual.isdigit():
                tokens.append(self._leer_numero())
                continue
            
            if self.caracter_actual.isalpha() or self.caracter_actual == '_':
                tokens.append(self._leer_identificador())
                continue
            
            if self.caracter_actual in self.operadores:
                tipo = 'PARENTESIS' if self.caracter_actual in '()' else 'OP'
                tokens.append(Token(tipo, self.caracter_actual))
                self.avanzar()
                continue
            
            if self.caracter_actual in self.caracteres_prohibidos:
                tokens.append(Token('INVALIDO', self.caracter_actual))
                self.avanzar()
                continue
            
            tokens.append(Token('DESCONOCIDO', self.caracter_actual))
            self.avanzar()
            
        return tokens

lista_cadenas = [
    "3_Var = 13 - 7", 
    "Total = 5 * (10 + 2)",
    "C:/Users/alber/python.exe"
]


for i, cadena in enumerate(lista_cadenas, 1):
    print(f"\n--- Analizando cadena {i}: '{cadena}' ---")
    
    lexer = Lexer(cadena)
    lista_tokens = lexer.tokenizar()

    for token in lista_tokens:
        print(f"Tipo: {token.tipo}, Valor: '{token.valor}'")

'''
for i, cadena in enumerate(lista_cadenas, 1):
    print(f"\n--- Analizando cadena {i}: '{cadena}' ---")
    
    lexer = Lexer(cadena)
    lista_tokens = lexer.tokenizar()

    for token in lista_tokens:
        nota = ""
        if token.tipo == 'ID':
            nota = " -> Variable Valida"
        elif token.tipo == 'INVALIDO':
            nota = " -> Caracter Invalido/Prohibido"
        
        print(f"Tipo: {token.tipo}, Valor: '{token.valor}'{nota}")
'''