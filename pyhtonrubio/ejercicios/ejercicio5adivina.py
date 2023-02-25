print("piensa en un numero")
print("¿ya lo tienes ? \n ahora sumale 5 \n")
print("ahora al resultado multiplicalo por 3")
print("y por ultimo a ese resultado restale 15")

resultado = int(input("ingresa ese resultado obtenido"))

solucion = resultado/3
print("el numero que pensaste originalmente es", solucion)

numero = int(input("¿es fue el numero que pensaste? \n si o no \n"))

if numero == "si" or numero == "Si" or numero == "SI":
    print(" soy todo un adivino")
else:
    print("rectifica tus cuentas y te daras cuenta que no me equivoco")
