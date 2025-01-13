"""
Programa: Calculadora de Áreas
Funcionalidad: Este programa calcula el área de diferentes figuras geométricas: círculo, cuadrado y triángulo.
El usuario selecciona la figura, ingresa los valores necesarios, y el programa calcula y muestra el área correspondiente.
Tipos de Datos: Utiliza integer, float, y string de manera adecuada.
"""

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: float, radio del círculo
    :return: float, área del círculo
    """
    return math.pi * radio ** 2


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el valor de uno de sus lados.

    :param lado: float, longitud de un lado del cuadrado
    :return: float, área del cuadrado
    """
    return lado ** 2


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    :param base: float, base del triángulo
    :param altura: float, altura del triángulo
    :return: float, área del triángulo
    """
    return 0.5 * base * altura


def menu_principal():
    """
    Muestra el menú principal y permite al usuario calcular el área de diferentes figuras geométricas.
    """
    while True:
        print("\n--- Calculadora de Áreas ---")
        print("1. Calcular área de un círculo")
        print("2. Calcular área de un cuadrado")
        print("3. Calcular área de un triángulo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                if radio > 0:
                    area = calcular_area_circulo(radio)
                    print(f"El área del círculo con radio {radio} es: {area:.2f}")
                else:
                    print("El radio debe ser un número positivo.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número válido.")

        elif opcion == "2":
            try:
                lado = float(input("Ingrese el lado del cuadrado: "))
                if lado > 0:
                    area = calcular_area_cuadrado(lado)
                    print(f"El área del cuadrado con lado {lado} es: {area:.2f}")
                else:
                    print("El lado debe ser un número positivo.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número válido.")

        elif opcion == "3":
            try:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                if base > 0 and altura > 0:
                    area = calcular_area_triangulo(base, altura)
                    print(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f}")
                else:
                    print("La base y la altura deben ser números positivos.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese números válidos.")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
