class Persona:
    def __init__(self, tipo_documento, numero_documento, nombres, apellidos):
        self._tipo_documento = tipo_documento
        self._numero_documento = numero_documento
        self.nombres = nombres
        self.apellidos = apellidos

    def get_tipo_documento(self):
        return self._tipo_documento

    def get_numero_documento(self):
        return self._numero_documento

    def set_tipo_documento(self, tipo_documento):
        self._tipo_documento = tipo_documento

    def set_numero_documento(self, numero_documento):
        self._numero_documento = numero_documento


class Empleado(Persona):
    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, cargo, valorhora, horastrabajadas, departamento):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos)
        self.cargo = cargo
        self.valorhora = valorhora
        self.horastrabajadas = horastrabajadas
        self.departamento = departamento

    def calcularHonorarios(self):
        total = self.valorhora * self.horastrabajadas
        reteica = total * 0.00966
        honorarios = total - reteica
        return honorarios

    def imprimirEmpleado(self):
        print(f"Tipo de documento: {self.get_tipo_documento()}")
        print(f"Número de documento: {self.get_numero_documento()}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Cargo: {self.cargo}")
        print(f"Horas trabajadas: {self.horastrabajadas}")
        print(f"Valor por hora: {self.valorhora}")
        print(f"Total a pagar: {self.calcularHonorarios()}")

