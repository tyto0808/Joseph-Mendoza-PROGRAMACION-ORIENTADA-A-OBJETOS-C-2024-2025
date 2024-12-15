# Programa para calcular el promedio semanal de temperaturas
# Utilizando Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Clase que representa el clima semanal.
    Permite almacenar temperaturas diarias, calcular el promedio semanal,
    y gestionar la entrada de datos.
    """

    def __init__(self):
        """
        Inicializa una instancia de ClimaSemanal con una lista vacía de temperaturas.
        """
        self.__temperaturas = []  # Atributo privado para almacenar las temperaturas

    def ingresar_temperaturas(self, temperaturas_predefinidas=None):
        """
        Método para ingresar las temperaturas diarias.
        Si se proporcionan temperaturas predefinidas, las utiliza; de lo contrario,
        solicita las temperaturas al usuario.
        """
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        if temperaturas_predefinidas:
            if len(temperaturas_predefinidas) != len(dias):
                raise ValueError("La lista de temperaturas predefinidas debe tener exactamente 7 valores.")
            self.__temperaturas = temperaturas_predefinidas
            return

        print("\nIngrese las temperaturas diarias de la semana:")
        for dia in dias:
            while True:
                try:
                    temperatura = float(input(f"Temperatura para {dia}: "))
                    self.__temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio semanal de las temperaturas almacenadas.
        """
        if not self.__temperaturas:
            raise ValueError("No se han ingresado temperaturas.")
        total = sum(self.__temperaturas)
        return total / len(self.__temperaturas)

    def mostrar_resumen(self):
        """
        Muestra un resumen de las temperaturas ingresadas y el promedio semanal.
        """
        print("\nResumen semanal:")
        print("Temperaturas ingresadas:", self.__temperaturas)
        print(f"Promedio semanal de temperaturas: {self.calcular_promedio():.2f}°C")

# Función principal para ejecutar el programa
def main():
    """
    Función principal del programa que organiza la ejecución:
    - Crea una instancia de ClimaSemanal.
    - Llama a los métodos de la clase para ingresar datos, calcular y mostrar resultados.
    """
    # Crear una instancia de ClimaSemanal
    clima = ClimaSemanal()

    # Datos predefinidos para simulación
    temperaturas_predefinidas = [20.5, 22.0, 19.8, 21.5, 23.1, 20.0, 18.9]

    # Ingresar datos (se pueden usar temperaturas predefinidas o interactivo)
    clima.ingresar_temperaturas(temperaturas_predefinidas)

    # Mostrar resultados
    clima.mostrar_resumen()

# Llamada a la función principal
if __name__ == "__main__":
    main()
