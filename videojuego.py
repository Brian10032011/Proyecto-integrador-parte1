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