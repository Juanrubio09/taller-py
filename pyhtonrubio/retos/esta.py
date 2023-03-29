intentos = 3
claveA = '1234'
saldoD = 4500
saldo = 4500

print("___________ Bienenidos a Nequi colombia____________ \n")
celular = input('Ingrese su numero de celular: \n')
clave = input('Ingrese su clave de acceso de 4 dígitos: \n')


if clave == claveA: 
    print(f'Su saldo disponible es de $ {saldoD}')
else:
    intentosRestantes = 3
    while intentosRestantes > 0:
        print('¡Upp! Parece que tus datos de acceso no son correctos. Tienes', intentosRestantes, 'intentos más.')
        celular = input('Ingrese su numero de celular : ')
        clave = input('Ingrese su clave de acceso de 4 dígitos: ')
        if clave == claveA:
            print(f'Su saldo disponible es de ${saldoD}')
            break
        intentosRestantes -= 1
    if intentosRestantes == 0:
        print('Lo siento, no puedes acceder a la aplicación. Ha superado el número máximo de intentos permitidos.')


def generarCodigo():
    import random
    return random.randint(100000, 999999)

while True:
    print("\n Bienvenido a Nequi Colombia ")
    print("1. Retirar dinero")
    print("2. Enviar dinero")
    print("3. Recargar saldo")
    print("4. Salir")

    opcion = input("\n Que opcion desea escoger? ")

    if opcion == "1":
        print(" Opciones de retiro:")
        print("1. Cajero")
        print("2. Punto físico")

        opcionRetiro = input("¿Cómo desea retirar su dinero? ")
        if opcionRetiro == "1":
            print("Retirando dinero en cajero...")
        elif opcionRetiro == "2":
            print("Retirando dinero en punto físico...")
        else:
            print("Opción no válida")

        if saldo < 2000:
            print(" No es posible hacer el retiro, su saldo no alcanza")
        else:
            cantidadRetiro = int(input("¿Cuanto desea retirar? "))
            if cantidadRetiro > saldo:
                print("No es posible hacer el retiro, la cantidad deseada supera su saldo")
            else:
                saldo -= cantidadRetiro
                codigoRetiro = generarCodigo()
                print(f"Retiro exitoso, su nuevo saldo es de $ {saldo}")
                print(f"Su código de retiro es {codigoRetiro}")

    elif opcion == "2":
     
        numeroDestino = input("Ingrese el número de teléfono al que desea enviar dinero: ")
        valorEnvio = int(input("¿Cuánto desea enviar? "))
        if valorEnvio > saldo:
            print("No es posible hacer el envío, la cantidad deseada supera su saldo")
        else:
            saldo -= valorEnvio
            print(f"Envío exitoso, su nuevo saldo es de ${saldo}")

    elif opcion == "3":
     
        valorRecarga = int(input("¿Cuánto desea recargar? "))
        confirmacion = input(f"¿Está seguro que desea recargar ${valorRecarga}? (si/no) ")
        if confirmacion == "si":
            saldo += valorRecarga
            print(f"Recarga exitosa, su nuevo saldo es de ${saldo}")
        else:
            print("Recarga cancelada")

    elif opcion == "4":
    
        print("Gracias por utilizar Nequi Colombia")
        break

    else:
        print("Opción no válida")

print("Fin del programa")