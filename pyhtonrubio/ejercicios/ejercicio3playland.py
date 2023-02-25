edad = int(input("ingresa tu edad \n"))

if 0 <= edad <= 4:
    print("puedes ingresar gratis")
elif 5 <= edad <= 17:
    print("el valor de tu voleta es $20.000")
elif 18 <= edad <= 60:
    print("el valor de tu voleta es $15.000")
else:
    print("el valor de tu voleta es $3.000")
