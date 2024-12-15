# Programa para calcular el promedio semanal de temperaturas
# Utilizando estructuras de funciones (Programación Tradicional)

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas(predefinidas=None):
    """
    Solicita al usuario ingresar las temperaturas de cada día de la semana
    y las almacena en una lista. Si se proporcionan temperaturas predefinidas,
    las utiliza en lugar de solicitar la entrada interactiva.
    Retorna la lista de temperaturas.
    """
    print("\nIngrese las temperaturas diarias de la semana (si no se proporcionan valores predefinidos):")
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    if predefinidas:
        if len(predefinidas) != len(dias):
            raise ValueError("La lista de temperaturas predefinidas debe tener exactamente 7 valores.")
        return predefinidas

    for dia in dias:
        while True:
            try:
                # Solicita la temperatura y la convierte en un número flotante
                temperatura = float(input(f"Temperatura para {dia}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas ingresadas.
    Recibe una lista de temperaturas como argumento.
    Retorna el promedio.
    """
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para organizar la ejecución del programa
def main():
    """
    Función principal del programa que organiza la ejecución:
    - Llama a ingresar_temperaturas() para obtener los datos.
    - Llama a calcular_promedio() para procesar los datos.
    - Muestra el resultado final.
    """
    # Datos predefinidos (simulación de entrada interactiva)
    temperaturas_predefinidas = [20.5, 22.0, 19.8, 21.5, 23.1, 20.0, 18.9]

    # Entrada de datos
    temperaturas = ingresar_temperaturas(temperaturas_predefinidas)

    # Cálculo del promedio
    promedio_semanal = calcular_promedio(temperaturas)

    # Salida de resultados
    print("\nResumen semanal:")
    print("Temperaturas ingresadas:", temperaturas)
    print(f"Promedio semanal de temperaturas: {promedio_semanal:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
