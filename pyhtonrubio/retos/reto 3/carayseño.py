import random

escoje = ("cara", "sello")

seleccion = int(input("escoje un numero entre 1 y 2 \n"))
for i in range(1):
    print(random.choice(escoje))

resultado = str(input("se sencero que escojiste escribe lo que escojiste \n"))
if resultado = escoje:
    print("gano")
else:
    print("perdio")
