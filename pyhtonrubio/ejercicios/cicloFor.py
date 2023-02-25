"""for i in range(1,5,1):
    #aqui instrucciones que deseas repetir
    price=int(input("Ingrese el precio del producto"))
    cantidad=int(input("ingrese la cantidad del producto"))
    print("Aqui estoy dentro del ciclo for")
print("aqui estoy fuera del ciclo for")"""

#solicitar al usuario un numero positivo y mostrar la tabla de multipolicar del 0 al 10 para ese numero

"""num=int(input("ingresa el numero"))
for i in range(0,11,1):
    res=num*i
    print(num,"x",i,"=",res)    """
   
    count=0
    total=0
    for i in range(1,6,1):
        prince=int(input("ingrese los precios del producto\n"))
        cantidad=int(input("ingrese la canidad del producto"))
        count=count+1 #inicia el contador 
        subtotal = prince*cantidad
        total=total+subtotal
        
print("el total a pagar es", total)
 pago=int(input("ingrese con cuanto paga"))
 cambio= pago-total_ordering()
 
 print("su cambio es:", cambio)
 
 puntos=input("cuanta con telefonia movil exito ?? \n digiste si o no \n")
 
 if puntos=="si":
     print("con su compra obtuvo:", count, "minutos")
 else:
     print("no pierdas mas minutos, adquiere ya tu telefonia exito")         

#print("se registraron", count,"referencias")
        
    

