import random
count="s"
aleatorio = random.randrange(0,3)
elijePc = ""
print("1. piedra")
print("2. papel")
print("3. tijera")
opcion= int(input("elige tu opcion"))
    
if opcion ==1:
    elijeUsuario = "pierda"
elif opcion ==2:
    elijeUsuario = "papel"
elif opcion ==3:
    elijeUsuario = "tijera"
print("elejiste:", elijeUsuario)
    
if aleatorio ==0:
    elijePc="piedra"
elif aleatorio ==1:
    elijePc="papel"
elif aleatorio ==2:
    elijePc="tijera"
print("la maquina elijio: ", elijePc)
print("_________________")

if elijePc == "piedra" and elijeUsuario == "papel":
    print("Ganaste")
elif elijePc == "papel" and elijeUsuario == "tijera":
    print("Ganaste")
elif elijePc == "tijera" and elijeUsuario == "piedra":
    print("Ganaste")
    
if elijePc == "piedra" and elijeUsuario == "tijera":
    print("perdiste")
elif elijePc == "tijera" and elijeUsuario == "papel":
    print("perdiste")
elif elijePc == "papel" and elijeUsuario == "piedra":
    print("perdiste")
elif elijePc == elijeUsuario:
    print("empate")
    
while count="s" or count="S":
    jugarDeNuevo=input("quieres jugar de nuevo: s/S o salir n/N")
    if juagarDeNuevo="s":
        break

