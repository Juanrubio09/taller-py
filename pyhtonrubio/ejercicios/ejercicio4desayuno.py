leche = input("¿trajiste la leche? \n digite s o n \n")
pan = input("¿trajiste el pan? \n digite s o n \n")
huevos = input("¿trajiste los huevos? \n digite s o n \n")

# mama estricta
if leche == "s" and pan == "s" and huevos == "s":
    print("era lo minimo venga y desayuna")
else:
    print("calvazo con posible trauma craneocefalico")

# mama compresiva
if leche == "s" or pan == "s" or huevos == "s":
    print("bueno mi amor")
else:
    print("va a tocar despertar a su papa para que valla")
