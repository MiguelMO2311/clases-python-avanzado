class Diccionario:
    def __init__(self):
        self.claves = []
        self.valores = []

    def agregar(self, clave, valor):
        """Añade o sustituye el valor de una clave."""
        if clave in self.claves:
            i = self.claves.index(clave)
            self.valores[i] = valor
        else:
            self.claves.append(clave)
            self.valores.append(valor)

    def obtener(self, clave):
        """Devuelve el valor asociado a una clave."""
        if clave in self.claves:
            i = self.claves.index(clave)
            return self.valores[i]
        raise KeyError(f"Clave '{clave}' no encontrada")

    def eliminar(self, clave):
        """Elimina una clave y su valor."""
        if clave in self.claves:
            i = self.claves.index(clave)
            del self.claves[i]
            del self.valores[i]
        else:
            raise KeyError(f"Clave '{clave}' no encontrada")

    def update(self, otro):
        """Actualiza con otro MiniDiccionario (último sobrescribe)."""
        for c, v in zip(otro.claves, otro.valores):
            self.agregar(c, v)

    def __contains__(self, clave):
        """Test de pertenencia: 'clave in diccionario'."""
        return clave in self.claves

    def keys(self):
        """Devuelve todas las claves."""
        return list(self.claves)

    def values(self):
        """Devuelve todos los valores."""
        return list(self.valores)

    def items(self):
        """Devuelve lista de tuplas (clave, valor)."""
        return list(zip(self.claves, self.valores))

    def __len__(self):
        """Devuelve el tamaño total."""
        return len(self.claves)

    def clear(self):
        """Limpia el diccionario por completo."""
        self.claves = []
        self.valores = []

    def __repr__(self):
        pares = [f"{c}: {v}" for c, v in zip(self.claves, self.valores)]
        return "{" + ", ".join(pares) + "}"

# Ejemplo de uso
d1 = Diccionario()
d1.agregar("nombre", "Miguel")
d1.agregar("edad", 50)

d2 = Diccionario()
d2.agregar("edad", 51)
d2.agregar("ciudad", "Madrid")

d1.update(d2)
print(d1)

print("edad" in d1)
print(d1.keys())
print(d1.values()) 
print(d1.items()) 
print(len(d1))

d1.eliminar("nombre")
print(d1)

d1.clear()
print(d1) 