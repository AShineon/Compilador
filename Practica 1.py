#Erick Alberto Mancillas Magdaleno
#Modulo 1 - Práctica 2
#Compiladores D03
#git add . -> git commit -> git push.
#Esta es la rama principal (main)

# Clase token para representar los tokens generados por el lexer
class token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor})"
    
# Clase nodo para representar los nodos del árbol sintáctico
class nodo:
    
    def __init__(self, valor, tipo):
        self.valor = 0
        self.tipo = 0
        self.hijos = []
        
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo) 
    
    def __repr__(self):
        return f"Nodo({self.tipo}, {self.valor})"

# Clase lexer para el análisis léxico (Es quien se encarga de dividir el código fuente en tokens)
class lexer:
    def __init__(self, entrada):
        self.entrada = entrada
        self.posicion = 0
        self.caracter_actual = self.entrada[self.posicion] if self.entrada else None
        self.operadores = {'+', '-', '*', '/', '%', '=', "(", ")"} 
        self.caracteres_prohibidos = {'$', '#', '/', '@', '\\', '|', ':', ';', '.', ',', '?', '!', '&', '<', '>', ' '}
    
    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.entrada):
            self.caracter_actual = self.entrada[self.posicion]
        else:
            self.caracter_actual = None
    
    def _saltar_espacios(self):
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()
            
    def _leer_numero(self):
        numero = ''
        while self.caracter_actual is not None and self.caracter_actual.isdigit():
            numero += self.caracter_actual
            self.avanzar()
        return token('NUMERO', int(numero))
    
    def _leer_identificador(self):
        identificador = ''
        while self.caracter_actual is not None and (self.caracter_actual.isalnum() or self.caracter_actual == '_'):
            identificador += self.caracter_actual
            self.avanzar()
        return token('IDENTIFICADOR', identificador)
    
    def obtener_tokens(self):
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
                tokens.append(token('OPERADOR', self.caracter_actual))
                self.avanzar()
                continue
            if self.caracter_actual in self.caracteres_prohibidos:
                raise ValueError(f"Caracter prohibido encontrado: {self.caracter_actual}")
            raise ValueError(f"Caracter desconocido encontrado: {self.caracter_actual}")
        tokens.append(token('EOF', None))
        return tokens
    
# Clase parser para el análisis sintáctico (Es quien se encarga de construir el árbol sintáctico a partir de los tokens)
class parser:
    
    def __init__(self, lista_tokens):
        self.pos_actual = 0
        self.token_actual = lista_tokens[self.pos_actual]
    
    def consumir(self, tipo_esperado):
        #verifica si el token actual es del tipo esperado
        return
    
    def parsear(self):
        return
    
    def expr(self):
        #Prioridad suma y resta
        return
    
    def termino(self):
        #Prioridad multiplicacion, division y modulo
        return
    
    def factor(self):
        #Prioridad numeros, variables y parentesis
        return