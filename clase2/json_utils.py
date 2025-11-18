def procesar_json(datos, callback):
    """
    Aplica la función callback al JSON (dict) y devuelve el resultado.
    """
    return callback(datos)

def todo_mayusculas(datos):
    """
    Convierte todas las cadenas del JSON a mayúsculas (solo nivel 1).
    """
    return {k: (v.upper() if isinstance(v, str) else v) for k, v in datos.items()}

def buscar_error(datos):
    """
    Devuelve las cadenas que contienen 'ERROR' en el JSON (solo nivel 1).
    """
    return [v for v in datos.values() if isinstance(v, str) and "ERROR" in v.upper()]


# Definir el JSON de ejemplo
datos = {
    "mensaje": "esto es un error",
    "codigo": "ERROR123",
    "usuario": "Miguel"
}



# Usar el callback para transformar a mayúsculas
resultado_mayus = procesar_json(datos, todo_mayusculas)
print("Todo en mayúsculas:", resultado_mayus)

# Usar el callback para buscar 'ERROR'
resultado_error = procesar_json(datos, buscar_error)
print("Entradas con 'ERROR':", resultado_error)