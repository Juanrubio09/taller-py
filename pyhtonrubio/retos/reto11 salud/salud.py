class Persona:
#atributos
    tipoDoc=" "
    documento=0
    nombre=" "
    apellido=" "
    peso=0
    estatura=0
    edad=0
    sexo=" "

#metodos

    def __init__(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo):
        self.tipoDoc=tipoDoc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo

    def pedirDatos(self):
        self.tipoDoc = input("Ingrese el tipo de documento : ")
        self.documento = int(input("Ingrese el numero de documento : "))
        self.nombre = input("Ingrese el nombre  : ")
        self.apellido = input("Ingrese el apellido  : ")
        self.peso = int(input("Ingrese el peso : "))
        self.estatura = int(input("Ingrese la estatura : "))
        self.edad = int(input("Ingrese la edad : "))
        self.sexo = input("Ingrese el sexo  : ")

    def mostrarPersona(self):
        print(
            f"Tipo de documento: {self.tipoDoc} , Documento: {self.documento} , Nombre: {self.nombre} , Apellido {self.apellido} , Peso {self.peso} , Estatura :  {self.estatura }, Edad : {self.edad} , Sexo : {self.sexo} ")
    
    def calcularImc(self,peso, estatura):
        pesoActual = peso / (estatura)**2
        return pesoActual


    def mayorEdad(self, edad):
        if edad >= 18:
            print("El usuario es mayor de edad")
        else:
            print("El usuatio es menor de edad") 
        






