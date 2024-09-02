class Persona:
    def __init__(self, matricula, dni, nombre_apellido, direccion):
        self.matricula = matricula
        self.dni = dni
        self.nombre_apellido = nombre_apellido
        self.direccion = direccion

    def mostrar_datos(self):
        print(f"Matrícula: {self.matricula}, DNI: {self.dni}, Nombre y Apellido: {self.nombre_apellido}, Dirección: {self.direccion}")

class Estudiante(Persona):
    def __init__(self, matricula, dni, nombre_apellido, direccion, anio_curso, materias):
        super().__init__(matricula, dni, nombre_apellido, direccion)
        self.anio_curso = anio_curso
        self.materias = materias

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Año de Curso: {self.anio_curso}, Materias: {self.materias}")

class Docente(Persona):
    def __init__(self, matricula, dni, nombre_apellido, direccion, cursos_acargo):
        super().__init__(matricula, dni, nombre_apellido, direccion)
        self.cursos_acargo = cursos_acargo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Cursos a Cargo: {self.cursos_acargo}")

# Crear objetos
estudiante1 = Estudiante("E001", "12345678", "Juan Pérez", "Calle 1", 2022, ["Matemáticas", "Física"])
estudiante2 = Estudiante("E002", "23456789", "María García", "Calle 2", 2023, ["Literatura", "Historia"])
estudiante3 = Estudiante("E003", "34567890", "Pedro Rodríguez", "Calle 3", 2022, ["Química", "Biología"])

docente1 = Docente("D001", "45678901", "Ana López", "Calle 4", ["Matemáticas", "Física"])
docente2 = Docente("D002", "56789012", "Juan Carlos", "Calle 5", ["Literatura", "Historia"])
docente3 = Docente("D003", "67890123", "María Elena", "Calle 6", ["Química", "Biología"])

# Mostrar datos
estudiante1.mostrar_datos()
print()

estudiante2.mostrar_datos()
print()

estudiante3.mostrar_datos()
print()

docente1.mostrar_datos()
print()

docente2.mostrar_datos()
print()
readme.py