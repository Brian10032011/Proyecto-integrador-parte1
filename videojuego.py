import os
import readchar
from readchar import readkey, key


#pedir nombre del jugador por teclado
nombre = input ("Por favor, ingresa tu nombre ")
#Mensaje de bienvenida con el nombre
print("Bienvenido "+nombre)

# while True:
#   k = readkey()
#   if k != key.UP:
#       print(k)
#   else:
#       break


# def borrar_e_imprimir (i):
#   os.system('cls' if os.name=='nt' else 'clear')   
#   if i == 50:
#     print("Fin del programa")
#   else:
#     print(f"Numero : {i}")
# i =0
# while i <= 50:
#     key = readchar.readkey()
#     if key == "n":
#        borrar_e_imprimir(i)
#        i+=1

'''
PROCESO DE LABERINTO
Proposito. 
'''


string_laberinto = "..###################" +\
    "\n......#...#.....#...#" +\
    "\n###.#.#.#.#.#.###.###" +\
    "\n#.#.#.#.#...#.#.....#" +\
    "\n#.#.#######.#####.###" +\
    "\n#.............#.#...#" +\
    "\n###.#.#.#####.#.###.#" +\
    "\n#...#.#.#...#.......#" +\
    "\n#.#####.#.#.#######.#" +\
    "\n#...#...#.#...#.#...#" +\
    "\n#.#.#######.###.#.#.#" +\
    "\n#.#.#...#...#.....#.#" +\
    "\n#.###.###.#####.###.#" +\
    "\n#...#.#...#.#.#...#.#" +\
    "\n#####.###.#.#.###.###" +\
    "\n#.....#...#.........#" +\
    "\n#####.###.#.#####.###" +\
    "\n#.#...#.#.#.#.#.#.#.#" +\
    "\n#.###.#.#.#.#.#.#.#.#" +\
    "\n#...........#......." +\
    "\n###################."


print(string_laberinto)

laberinto_normalizado = list(map(list,string_laberinto.split("\n")))

# AÑADIENDO LAS PAREDES DE LAS ULTIMAS DOS FILAS 
laberinto_normalizado[len(laberinto_normalizado)-2].append("#")
laberinto_normalizado[len(laberinto_normalizado)-1].append("#")


continue_game = True


def posicion_valida(laberinto,position_nueva,posicion_actual):
    #import pdb;pdb.set_trace()
    response = False
    if (laberinto[position_nueva[1]][position_nueva[0]] == "."):
        laberinto[position_nueva[1]][position_nueva[0]] = "P"
        if (posicion_actual):
            laberinto[posicion_actual[1]][posicion_actual[0]] = "."
        response = True
    return response, laberinto

def movimientos_user(posicion):
    movimiento_incorrecto= True    
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
    #import pdb;pdb.set_trace()
    return posicion

def printCorrectFormat(laberinto_sin_formato):
    string_nuevo = ""
    for n in laberinto_sin_formato:
        for j in n:
            string_nuevo += j
        string_nuevo += "\n"
    return string_nuevo[:-1]


posicion_actual = None
posicion_nueva = [0,0]

laberinto_actualizado = laberinto_normalizado

while continue_game:    
    is_valid,laberinto_actualizado = posicion_valida(laberinto_actualizado, posicion_nueva, posicion_actual)     
    posicion_actual = posicion_nueva.copy()
    if (is_valid):
        clear = lambda: os.system("cls")
        clear()

        # print(laberinto_actualizado)
        print(printCorrectFormat(laberinto_actualizado))
        posicion_nueva = movimientos_user(posicion_nueva)
        
    else:
        continue_game = False
    # import pdb;pdb.set_trace()
