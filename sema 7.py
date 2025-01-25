class FileHandler:
    """
    Esta clase se encarga de manejar operaciones básicas de archivos.
    Utiliza un constructor para abrir un archivo y un destructor para cerrarlo automáticamente.
    """

    def __init__(self, filename, mode):
        """
        Constructor que inicializa el objeto y abre el archivo.
        :param filename: Nombre del archivo a manejar.
        :param mode: Modo en el que se abrirá el archivo (por ejemplo, 'r', 'w', 'a').
        """
        self.filename = filename
        self.mode = mode
        try:
            self.file = open(filename, mode)
            print(f"Archivo '{filename}' abierto en modo '{mode}'.")
        except Exception as e:
            print(f"Error al abrir el archivo '{filename}': {e}")
            self.file = None

    def write(self, content):
        """
        Escribe contenido en el archivo si está abierto en modo escritura.
        :param content: Contenido a escribir en el archivo.
        """
        if self.file and not self.file.closed and 'w' in self.mode:
            self.file.write(content)
            print(f"Se ha escrito contenido en el archivo '{self.filename}'.")
        else:
            print("El archivo no está abierto en modo escritura o no se pudo abrir.")

    def read(self):
        """
        Lee el contenido del archivo si está abierto en modo lectura.
        """
        if self.file and not self.file.closed and 'r' in self.mode:
            print(f"Leyendo contenido del archivo '{self.filename}':")
            return self.file.read()
        else:
            print("El archivo no está abierto en modo lectura o no se pudo abrir.")
            return None

    def __del__(self):
        """
        Destructor que cierra el archivo automáticamente al destruirse el objeto.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado.")

# Clase secundaria para mostrar el uso de constructores y destructores con datos temporales
class TempData:
    """
    Esta clase crea un objeto temporal que genera y elimina datos en memoria.
    """
    def __init__(self, data):
        """
        Constructor que inicializa el objeto con datos temporales.
        :param data: Datos temporales a manejar.
        """
        self.data = data
        print("Objeto TempData creado con los datos:", self.data)

    def process_data(self):
        """
        Procesa los datos (simulación de alguna operación).
        """
        print("Procesando datos:", self.data)
        return [d.upper() for d in self.data]

    def __del__(self):
        """
        Destructor que elimina los datos del objeto al destruirse.
        """
        print("Objeto TempData destruido y los datos han sido limpiados.")

# Demostración de las clases
def main():
    # Demostración del manejo de archivos
    handler = FileHandler("demo.txt", "w")
    handler.write("Hola, este es un archivo de demostración.\n")
    del handler  # Forzamos la destrucción del objeto para cerrar el archivo

    # Demostración del manejo de datos temporales
    temp = TempData(["dato1", "dato2", "dato3"])
    processed = temp.process_data()
    print("Datos procesados:", processed)
    del temp  # Forzamos la destrucción del objeto para limpiar los datos

if __name__ == "__main__":
    main()
