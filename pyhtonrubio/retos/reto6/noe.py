import random
count = "c"
aleatorio = random.randrange (0,4)
descuento = ""
totalcompra = 0


compra = int(input("ingresa el valor de tu compra :  "))
if compra >= 50000:
    print("participa del sorteo")
    print("bolita roja obtienes 10%")
    print("bolita azul obtienes 30%")
    print("bolita amarilla obtienes 50%")
    print("bolita blanca llevas toda tu compra gratis !!!")

if aleatorio ==0:
    descuento = compra *0.10
    totalcompra = compra - descuento 
    print(" tu bolita fue la roja tu valor total es : ", totalcompra)
elif aleatorio ==1:
    descuento = compra *0.30
    totalcompra = compra - descuento 
    print(" tu bolita fue la azul tu valor total es : ", totalcompra) 
elif aleatorio ==2:
    descuento = compra *0.50
    totalcompra = compra - descuento 
    print(" tu bolita fue la amarilla tu valor total es : ", totalcompra) 
elif aleatorio ==3:

    totalcompra = compra - compra 
    print(" tu bolita fue la blanca tu valor total es : ", totalcompra) 
      
print("_________________")

    

    
    
    
