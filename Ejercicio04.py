class Libro:
    def __init__(self, titulo, autor, anio):
        """Constructor de la clase Libro."""
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        """Presta el libro si está disponible."""
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado exitosamente."
        else:
            return f"El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        """Devuelve el libro."""
        if not self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto exitosamente."
        else:
            return f"El libro '{self.titulo}' ya se encontraba disponible."

    def __str__(self):
        """Representación en string del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}, Estado: {estado}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanoMB):
        """Constructor de LibroDigital con propiedades adicionales."""
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamanoMB = tamanoMB
    
    def prestar(self):
        """Un libro digital siempre está disponible para préstamo."""
        return f"Libro Digital '{self.titulo}' consultado/prestado (siempre disponible en formato {self.formato})."

    def __str__(self):
        """Representación en string con datos adicionales."""
        base_str = super().__str__()
        return f"{base_str}, Formato: {self.formato}, Tamaño: {self.tamanoMB}MB"

class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con un conjunto vacío de libros."""
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro a la colección de la biblioteca."""
        self.libros.append(libro)
        print(f"\nAgregado: {libro.titulo}")

    def listar_libros(self):
        """Lista todos los libros con su disponibilidad."""
        print("\n--- Listado de Libros en Biblioteca ---")
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for libro in self.libros:
            print(libro)
        print("---------------------------------------")

    def buscar_por_autor(self, autor):
        """Busca y lista libros por autor."""
        print(f"\n--- Libros encontrados del autor: {autor} ---")
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")
        print("-------------------------------------------------")
        return encontrados

    def prestar_libro(self, titulo):
        """Busca el libro por título y lo presta si está disponible."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(libro.prestar())
                return
        print(f"Error: Libro '{titulo}' no encontrado.")


lib_fisico1 = Libro("El Quijote", "Cervantes", 1605)
lib_fisico2 = Libro("Cien Años de Soledad", "García Márquez", 1967)
lib_fisico3 = Libro("1984", "Orwell", 1949)

lib_digital1 = LibroDigital("Fundamentos de Programación I", "Aedo López", 2025, "PDF", 15.5)
lib_digital2 = LibroDigital("Guía EPUB", "Smith", 2020, "EPUB", 8.2)

biblioteca = Biblioteca()

biblioteca.agregar_libro(lib_fisico1)
biblioteca.agregar_libro(lib_fisico2)
biblioteca.agregar_libro(lib_fisico3)
biblioteca.agregar_libro(lib_digital1)
biblioteca.agregar_libro(lib_digital2)

print("\nPRUEBAS DE LA BIBLIOTECA")

biblioteca.listar_libros()

biblioteca.prestar_libro("El Quijote")

print("\nIntentos de préstamo de libro digital:")
for i in range(5):
    biblioteca.prestar_libro("Fundamentos de Programación I")

biblioteca.listar_libros()

biblioteca.prestar_libro("El Quijote")

biblioteca.buscar_por_autor("Cervantes")
biblioteca.buscar_por_autor("Aedo López")