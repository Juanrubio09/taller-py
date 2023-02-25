import random

print("^^^^^^CRAPS apuesta a un solo tiro ^^^^^^")
print("como ganas: \n con un numero par de uno en los dados \n que el toral de los dados sena tres \n si el total entre los dos dados es 11 \n si obtienes 2 o 12 en los dos dados \n y si el total de los dados da 7 ")

dado1 = random.randint(1, 6)
print("resultado", dado1)
dado2 = random.randint(1, 6)
print("resultado", dado2)

if dado1 == 1 and dado2 == 1:
    print("sacaste par 1 :\n Ganaste")
elif dado1+dado2 == 3:
    print("sumaste en los dos dados 3 :\n Ganaste")
elif dado1+dado2 == 11:
    print("sumaste en los dos dados 11 :\n Ganaste")
elif dado1+dado2 == 2:
    print("sumaste en los dos dados 2 :\n Ganaste")
elif dado1+dado2 == 12:
    print("sumaste en los dos dados 12 :\n Ganaste")
elif dado1+dado2 == 7:
    print("sumaste en los dos dados 7:\n Ganaste")
else:
    print("mala suerte GAME OVER!!!")
