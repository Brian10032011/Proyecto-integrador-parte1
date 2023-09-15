#pedir nombre del jugador por teclado
nombre = input ("Por favor, ingresa tu nombre")
#Mensaje de bienvenida con el nombre
print("Bienvenido "+nombre)


from readchar import readkey, key

while True:
  k = readkey()
  if k != key.UP:
    print(k)
  else:
    break

import os
import readchar
def borrar_e_imprimir (i):
  os.system('cls' if os.name=='nt' else 'clear')
    
  if i == 50:
    print("Fin del programa")
  else:
    print(f"Numero : {i}")
i =0
while i <= 50:
    key = readchar.readkey()
    if key == "n":
       borrar_e_imprimir(i)
       i+=1

    
