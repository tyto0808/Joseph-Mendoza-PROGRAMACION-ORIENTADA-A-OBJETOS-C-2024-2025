import os
import subprocess


def mostrar_codigo(ruta_script):
    """Muestra el contenido de un script Python."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return None


def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en una nueva terminal según el sistema operativo."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['cmd', '/k', 'python', ruta_script])
        elif os.name == 'posix':  # Linux y macOS
            subprocess.run(['x-terminal-emulator', '-e', f'python3 {ruta_script}'])
        else:
            print("Sistema operativo no compatible para ejecución automática.")
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")


def mostrar_menu():
    """Muestra el menú principal."""
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    while True:
        print("\n=====================")
        print("  Dashboard Principal")
        print("=====================")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            print("Saliendo...")
            break
        elif eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print("Opción inválida, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """Muestra las subcarpetas dentro de una unidad."""
    if not os.path.exists(ruta_unidad):
        print("Unidad no encontrada.")
        return
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n--- Submenú ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar")

        eleccion = input("Elige una subcarpeta: ")
        if eleccion == '0':
            break
        try:
            eleccion_idx = int(eleccion) - 1
            if 0 <= eleccion_idx < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_idx]))
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada no válida.")


def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles en una subcarpeta y permite ver/ejecutar uno."""
    if not os.path.exists(ruta_sub_carpeta):
        print("Carpeta no encontrada.")
        return
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts Disponibles ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        eleccion = input("Elige un script: ")
        if eleccion == '0':
            break
        try:
            eleccion_idx = int(eleccion) - 1
            if 0 <= eleccion_idx < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_idx])
                if mostrar_codigo(ruta_script):
                    if input("¿Ejecutar script? (1: Sí, 0: No): ") == '1':
                        ejecutar_codigo(ruta_script)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada no válida.")


if __name__ == "__main__":
    mostrar_menu()
