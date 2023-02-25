countH = 0
countM = 0
binario = 0
for i in range(1, 11, 1):
    genero = int(input("ingresa tu genero porfavor : \n 1 para hombre o 2 mujer \n "))

    if genero == 1:
        countH = countH+1
    elif genero == 2:
        countM = countM+1

print("en el grupo de personas hay:", countH, "hombres" "y", countM, "mujeres")
