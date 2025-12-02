
# Cohesión Funcional (buena))
# Cada función hace una sola tarea clara y bien definida por ejemplo una calculadora de áreas
def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Ejemplo de uso
print("Área cuadrado:", calcular_area_cuadrado(4))
print("Área rectángulo:", calcular_area_rectangulo(5, 3))
print("Área triángulo:", calcular_area_triangulo(6, 2))


# Cohesión Secuencial (buena)
# La salida de una función es la entrada de la siguiente

def leer_numeros():
    return "10,20,30"

def convertir_a_lista(cadena):
    return [int(x) for x in cadena.split(",")]

def sumar_lista():
    datos = convertir_a_lista(leer_numeros())
    return sum(datos)

# Ejemplo de uso
print("Suma de lista:", sumar_lista())


# Cohesión Comunicacional (aceptable)
# Todas las funciones trabajan sobre los mismos datos

def crear_producto(nombre, precio):
    return {"nombre": nombre, "precio": precio}

def aplicar_descuento(producto, porcentaje):
    producto["precio"] *= (1 - porcentaje)

def mostrar_producto(producto):
    print(f"{producto['nombre']} cuesta {producto['precio']} €")

# Ejemplo de uso
p = crear_producto("Libro", 20)
aplicar_descuento(p, 0.1)
mostrar_producto(p)


# Cohesión Procedimental (moderada, bandera amarilla)
# Las funciones están relacionadas porque deben ejecutarse en orden

def abrir_sesion(usuario):
    print(f"Sesión abierta para {usuario}")

def validar_sesion(usuario):
    print(f"Validando permisos de {usuario}")

def cerrar_sesion(usuario):
    print(f"Sesión cerrada para {usuario}")

def flujo_sesion(usuario):
    abrir_sesion(usuario)
    validar_sesion(usuario)
    cerrar_sesion(usuario)

# Ejemplo de uso
flujo_sesion("Miguel")
