#Erick Alberto Mancillas Magdaleno
#Modulo 1 - Práctica 2
#Compiladores D03
#git add . -> git commit -> git push.

class Automata:
    def __init__(self):
        self.estado = 'inicio'
        self.caracteres_prohibidos = {'$', '#', '/', '(', '@', '-', '\\', '|', ':', ';', '.', ',', '?', '!', ')', '&', '<', '>', ' '}
        self.operadores = {'+', '-', '*', '/', '%', '='}

    def transicion(self, caracter):
        if self.estado == 'inicio':
            # El primer caracter: letra o '_' (no puede empezar con número)
            if (caracter.isalpha() or caracter == '_') and caracter not in self.caracteres_prohibidos:
                self.estado = 'valido'
            else:
                self.estado = 'invalido'
        elif self.estado == 'valido':
            # Siguientes: alfanuméricos o '_'
            if (caracter.isalnum() or caracter == '_') and caracter not in self.caracteres_prohibidos:
                self.estado = 'valido'
            else:
                self.estado = 'invalido'

    def es_valida(self, cadena):
        if not cadena: return False # Caso cadena vacía
        self.estado = 'inicio'
        for caracter in cadena:
            self.transicion(caracter)
            if self.estado == 'invalido':
                return False
        return self.estado == 'valido'
    
    def clasificar_cadena(self, cadena):
        if self.es_valida(cadena):
            return "Variable válida +"
        else:
            return "Variable no válida"
    

    # Añadimos el método para procesar la lista completa
    def validar_lista(self, lista):
        return [self.es_valida(v) for v in lista]



lista = ["_variable1", "var2", "3variable", "var-3", "var 4", "var$nombre", "_var_final", "nombre@", "a", "_1var", " "]

automata = Automata()
resultados = automata.validar_lista(lista)

for i, variable in enumerate(lista):
    if resultados[i]:
        print(f"La variable '{variable}' es válida.")
    else:
        print(f"La variable '{variable}' no es válida.")