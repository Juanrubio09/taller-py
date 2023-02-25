
presupuesto = 100000
respuesta = "s"
count = 0
total = 0
while (respuesta == "s" or respuesta == "S") and presupuesto>= 0 and count<3:
    gasto = int(input("ingrese el valor del gasto: "))
    presupuesto = presupuesto - gasto
    count += 1
    total += gasto
    print("su presupuesto ahora es: ", presupuesto)
    if count < 3 and presupuesto > 0:
        respuesta = input(
            "desea registrar un nuevo gasto presione s/S y para no registrar n/N: ")
    

print("________________________________________")
print("el total de tus gastos fueron: ", total)
print("tu presupuesto actual es: ", presupuesto)
