cuenta = 1000000
transaccion = "s"
count = 0 
total = 0 

print("valor en la cuenta : ", cuenta)
print("menu")
print("Retirar = 1 ")
print("consignar = 2 ")

opcion = int(input("Escoja su transaccion : "))

if opcion == 1 : 
    retiro = int(input(" cuanto desea retirar : "))
    saldo = cuenta - retiro
    count -= 1
    total -= retiro 
    print("su saldo  ahora es: ", saldo)
    
if opcion == 2 :
    consignar = int(input(" cuanto desea consignar : "))
    saldo = cuenta + consignar 
    count += 1
    total += consignar
    print("su saldo  ahora es: ", saldo)

if count < 3 and saldo > 0:
        transaccion = input("desea imprimir factura s/S y para no registrar n/N: ")
        
        print("________________________________________")
        print("su retiro fue: ", retiro )
        print("tu saldo actual es: ", saldo)
        
if count < 3 and saldo > 0:
    transaccion = input("desea imprimir factura s/S y para no registrar n/N: ")
        
print("________________________________________")
print("su retiro fue: ", consignar )
print("tu saldo actual es: ", saldo)       


