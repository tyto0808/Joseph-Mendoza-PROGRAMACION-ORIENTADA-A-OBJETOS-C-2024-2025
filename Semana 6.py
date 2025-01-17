# Programa que demuestra los conceptos de Herencia, Encapsulación y Polimorfismo

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado (encapsulación)
        self.edad = edad

    # Método para acceder al atributo privado
    def get_nombre(self):
        return self.__nombre

    # Método para modificar el atributo privado
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método que se puede sobrescribir (polimorfismo)
    def descripcion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.edad}"

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.grado = grado

    # Sobrescritura de método (polimorfismo)
    def descripcion(self):
        return f"Estudiante {self.get_nombre()}, Edad: {self.edad}, Grado: {self.grado}"

# Clase derivada adicional para mostrar otro ejemplo de polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Sobrescritura de método (polimorfismo)
    def descripcion(self):
        return f"Profesor {self.get_nombre()}, Edad: {self.edad}, Materia: {self.materia}"

# Crear instancias de las clases
persona = Persona("Juan", 45)
estudiante = Estudiante("Ana", 20, "Matemáticas")
profesor = Profesor("Luis", 38, "Historia")

# Uso de los métodos
print(persona.descripcion())  # Uso de método de la clase base
print(estudiante.descripcion())  # Uso del método sobrescrito
print(profesor.descripcion())  # Uso del método sobrescrito

# Encapsulación: modificar y acceder a un atributo privado
print(f"Nombre original: {persona.get_nombre()}")
persona.set_nombre("Carlos")
print(f"Nombre modificado: {persona.get_nombre()}")
