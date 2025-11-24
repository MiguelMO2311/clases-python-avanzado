def nombres_mayus(lista_nombres):
    for nombre in lista_nombres:
        yield nombre.upper()

# Ejemplo de uso
if __name__ == "__main__":
    nombres = ["Miguel", "Joaquin", "Oleguer", "Alvaro"]
    for n in nombres_mayus(nombres):
        print(n)

#  Ejemplo con comprehension de listas (no es un generador)

def nombres_mayus(lista_nombres):
    """Devuelve todos los nombres en mayúsculas de golpe usando comprensión de listas"""
    return [nombre.upper() for nombre in lista_nombres]

# Ejemplo de uso
if __name__ == "__main__":
    nombres = ["Miguel", "Joaquin", "Oleguer", "Alvaro"]
    for n in nombres_mayus(nombres):
        print(n)
