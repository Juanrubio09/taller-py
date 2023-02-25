num1 = int(input("ingrese el pirmer numero \n"))
num2 = int(input("ingrese el segundo numero \n"))

if num1 > num2:
    print("El numero mayor es", num1)
elif num2 > num1:
    print("El numero mayor es", num2)
else:
    print("los numeros", num1, "y", num2, "son iguales")
