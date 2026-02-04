#Erick Alberto Mancillas Magdaleno
#Modulo 1 - Práctica 2
#Compiladores D03
#git add . -> git commit -> git push.

class Automata:
    def __init__(self):
        self.estado = "inicio"
        self.no_permitidos = ["&", "%", "$", "#", "@", "!", "¡", "?", "¿", "-", "+", "=", "*", "/", "\\", " "]
        
    def transicion(self, caracter):
        if self.estado == "inicio":
            if caracter.isalpha() or caracter == "_":
                self.estado = "valido"
            else:
                self.estado = "invalido"
        elif self.estado == "valido":
            if caracter.isalnum() or caracter == "_":
                self.estado = "valido"
            else:
                self.estado = "invalido" 
        else:
            if caracter in self.no_permitidos:
                self.estado = "invalido"
                
    def validar(self, lista, cadena):
        resultados = []
        for variable in lista:
            automata = Automata()
            # Cadena vacía no es válidas
            if len(variable) == 0:
                resultados.append(False)
                continue
            # Validar primer carácter
            if variable[0].isdigit():
                resultados.append(False)
                continue
            # Validar resto de caracteres
            valido = True
            for caracter in variable:
                automata.transicion(caracter)
                if automata.estado == "invalido":
                    valido = False
                    break
            resultados.append(valido)
        return resultados


lista = ["_variable1", "var2", "3variable", "var-3", "var 4", "var$nombre", "_var_final", "nombre@", "a", "_1var", " "]

automata = Automata()
resultados = automata.validar(lista, "")

for variable in lista:
    if resultados[lista.index(variable)]:
        print(f"La variable '{variable}' es válida.")
    else:
        print(f"La variable '{variable}' no es válida.")
