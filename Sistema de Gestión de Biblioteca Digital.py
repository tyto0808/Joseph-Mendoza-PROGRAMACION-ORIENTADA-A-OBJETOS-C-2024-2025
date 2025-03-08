class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable con título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"{self.info[0]} de {self.info[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __repr__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # ISBN como clave, objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para IDs de usuario únicos
        self.prestamos = {}  # Diccionario para rastrear préstamos (user_id: lista de libros)

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            self.prestamos[usuario.user_id] = []
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            if not self.prestamos[user_id]:  # Solo dar de baja si no tiene libros prestados
                self.usuarios_registrados.remove(user_id)
                del self.prestamos[user_id]
            else:
                print("El usuario tiene libros prestados y no puede darse de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.prestamos[user_id].append(libro)
        else:
            print("Usuario no registrado o libro no disponible.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados:
            for libro in self.prestamos[user_id]:
                if libro.isbn == isbn:
                    self.prestamos[user_id].remove(libro)
                    self.libros_disponibles[isbn] = libro
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if (criterio == "titulo" and libro.info[0] == valor) or
                         (criterio == "autor" and libro.info[1] == valor) or
                         (criterio == "categoria" and libro.categoria == valor)]
        return resultados if resultados else "No se encontraron libros."

    def listar_libros_prestados(self, user_id):
        if user_id in self.prestamos:
            return self.prestamos[user_id] if self.prestamos[user_id] else "No tiene libros prestados."
        return "Usuario no registrado."


# Ejemplo de uso
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "67890")
usuario1 = Usuario("Juan Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "12345")
print(biblioteca.listar_libros_prestados("U001"))
