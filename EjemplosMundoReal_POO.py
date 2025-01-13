# Ejemplo de sistema de reservas para un hotel utilizando POO en Python

# Clase para representar una habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación con un número, tipo y precio.
        :param numero: int, número de la habitación
        :param tipo: str, tipo de habitación (ej. "Simple", "Doble")
        :param precio: float, precio por noche
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False  # Estado inicial de la habitación

    def ocupar(self):
        """Marca la habitación como ocupada."""
        self.ocupada = True

    def desocupar(self):
        """Marca la habitación como desocupada."""
        self.ocupada = False

    def __str__(self):
        """Devuelve una representación legible de la habitación."""
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero}: {self.tipo}, ${self.precio:.2f} por noche ({estado})"

# Clase para representar una reserva
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        """
        Inicializa una reserva con los datos del cliente, la habitación y el número de noches.
        :param cliente: str, nombre del cliente
        :param habitacion: Habitacion, objeto de la clase Habitacion
        :param noches: int, número de noches de la estancia
        """
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.total = habitacion.precio * noches

    def confirmar(self):
        """Confirma la reserva y ocupa la habitación."""
        if not self.habitacion.ocupada:
            self.habitacion.ocupar()
            return f"Reserva confirmada para {self.cliente} en la habitación {self.habitacion.numero} por {self.noches} noches. Total: ${self.total:.2f}"
        else:
            return f"La habitación {self.habitacion.numero} ya está ocupada."

    def cancelar(self):
        """Cancela la reserva y desocupa la habitación."""
        self.habitacion.desocupar()
        return f"Reserva de {self.cliente} cancelada."

# Clase para gestionar el sistema del hotel
class Hotel:
    def __init__(self, nombre):
        """
        Inicializa un hotel con un nombre y una lista de habitaciones.
        :param nombre: str, nombre del hotel
        """
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación a la lista del hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra el estado de todas las habitaciones del hotel."""
        for habitacion in self.habitaciones:
            print(habitacion)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear el hotel
    hotel = Hotel("Hotel Python")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Simple", 50.0))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80.0))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 120.0))

    # Mostrar habitaciones disponibles
    print("Habitaciones disponibles:")
    hotel.mostrar_habitaciones()

    # Crear una reserva
    habitacion_seleccionada = hotel.habitaciones[1]  # Habitación 102
    reserva = Reserva("Juan Pérez", habitacion_seleccionada, 3)

    # Confirmar la reserva
    print("\n" + reserva.confirmar())

    # Mostrar habitaciones después de la reserva
    print("\nEstado de las habitaciones tras la reserva:")
    hotel.mostrar_habitaciones()

    # Cancelar la reserva
    print("\n" + reserva.cancelar())

    # Mostrar habitaciones después de cancelar la reserva
    print("\nEstado de las habitaciones tras cancelar la reserva:")
    hotel.mostrar_habitaciones()
