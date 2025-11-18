def validador_mayoria_edad(edad_minima):
    def validar(edad):
        return edad >= edad_minima
    return validar

print(validador_mayoria_edad(18)(20))  # True
print(validador_mayoria_edad(21)(20))  # False
