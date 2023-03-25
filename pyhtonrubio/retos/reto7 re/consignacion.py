cuenta = 1000000
transaccion = "c"
count = 0
total = 0 

print("valor en la cuenta : ", cuenta)


while (transaccion == "c" or transaccion == "C") and cuenta>= 0 and count<1:
    consignar = int(input(" ingrese el valor a consignar : "))
    saldo = cuenta + consignar 
    count += 1
    total += consignar
print("su saldo  ahora es: ", saldo)
if count < 3 and saldo > 0:
        transaccion = input("desea registrar un nuevo gasto presione s/S y para no registrar n/N: " )
        
print("________________________________________")
print("su consignacion fue: ", consignar )
print("tu saldo actual es: ", saldo)