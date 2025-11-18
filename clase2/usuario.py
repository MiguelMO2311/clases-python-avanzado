class Usuario:
    def __init__(self, nombre, edad):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.nombre = nombre
        self.edad = edad

    def es_adulto(self):
        return self.edad >= 18

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nuevo_nombre
        return self.nombre
