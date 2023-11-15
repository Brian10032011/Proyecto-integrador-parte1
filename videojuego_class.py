import os
import readchar
from readchar import readkey, key


#pedir nombre del jugador por teclado
nombre = input ("Por favor, ingresa tu nombre ")
#Mensaje de bienvenida con el nombre
print("Bienvenido "+nombre)


def clearScreen():
    clear = lambda: os.system("cls")
    clear()

class Juego(object):
    # Constructor
    def __init__(self, laberinto_parametro):
        # atributo
        self.laberinto = laberinto_parametro
        self.laberinto_normalizado = None
        self.laberinto_desnormalizado = None
        self.position_nueva = [0,0]
        self.posicion_actual = None
        self.valid = True
        self.normalizacionLaberinto()
    
    def normalizacionLaberinto(self):
        laberinto_normalizado = list(map(list,self.laberinto.split("\n")))

        # AÑADIENDO LAS PAREDES DE LAS ULTIMAS DOS FILAS 
        laberinto_normalizado[len(laberinto_normalizado)-2].append("#")
        laberinto_normalizado[len(laberinto_normalizado)-1].append("#")

        self.laberinto_normalizado = laberinto_normalizado
    
    def posicion_valida(self):
        response = False
        laberinto = self.laberinto_normalizado.copy()
        if (laberinto[self.position_nueva[1]][self.position_nueva[0]] == "."):
            laberinto[self.position_nueva[1]][self.position_nueva[0]] = "P"
            if (self.posicion_actual):
                laberinto[self.posicion_actual[1]][self.posicion_actual[0]] = "."
            response = True
        if not response:
            self.valid = False
        self.laberinto_normalizado = laberinto
            
    def movimientos_user(self):
        posicion = self.position_nueva.copy()
        while True:
            k = readkey()
            if k == key.UP:
                posicion[1] -= 1
                break
            if k == key.DOWN:
                posicion[1] += 1
                break
            if k == key.LEFT:
                posicion[0] -= 1
                break
            if k == key.RIGHT:
                posicion[0] += 1
                break
        self.position_nueva = posicion
    
    def desnormalizacionLaberinto(self):
        string_nuevo = ""
        fr = self.laberinto_normalizado.copy()
        for n in self.laberinto_normalizado:
            for j in n:
                string_nuevo += j
            string_nuevo += "\n"
        self.laberinto_desnormalizado = string_nuevo[:-1]

    def finJuego(self):
        response = "Gracias por jugar {} , tu juego a finalizado"
        print(response.format(nombre))
    
    def __main__(self):
        continue_game = True
        while continue_game:

            self.posicion_valida()     
            self.posicion_actual = self.position_nueva
            if (self.valid):
                clearScreen()
                self.desnormalizacionLaberinto()
                print(self.laberinto_desnormalizado)
                self.movimientos_user()                
            else:
                self.finJuego()
                continue_game = False


# miJuego = Juego(string_laberinto)
# miJuego.__main__()

