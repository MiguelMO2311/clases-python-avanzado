# clase que sea edificio 

class Edificio:
    def __init__ (self, planta:str , orientacion:str, superficie:float):
        self.planta = planta
        self.orientacion = orientacion
        self.superficie = superficie
        self.luces = False

    def interruptor(self):
        self.luces = not self.luces
        if self.luces:
            return (f"Las luces del edificio están encendidas.")
        else:
            self.luces == False
            return (f"Las luces del edificio están apagadas.")
        
        
    #Ejemplo de uso
edificio1 = Edificio("3","Este",120.2)
print(edificio1.interruptor())
print(edificio1.interruptor())
print(edificio1.interruptor())


    # una clase reloj que tenga un metodo que me diga la hora actual, atributos solo la hora, minutos y segundos.
    
from datetime import datetime

class Reloj:
    def __init__(self):
        ahora = datetime.now()
        self.hora = ahora.hour
        self.minutos = ahora.minute
        self.segundos = ahora.second

    def hora_actual(self) -> str:
        ahora = datetime.now()
        self.hora = ahora.hour
        self.minutos = ahora.minute
        self.segundos = ahora.second
        return f"{self.hora:02d}:{self.minutos:02d}:{self.segundos:02d}"


# Ejemplo de uso
reloj = Reloj()
print(reloj.hora_actual())




















# class Dispositivo:
#     def __init__(self):
#         self.encendido = False

#     def interruptor(self):
#         self.encendido = not self.encendido
#         return "Encendido" if self.encendido else "Apagado"

# class Reloj(Dispositivo):
#     def __init__(self, hora: int, minutos: int, segundos: int):
#         super().__init__()
#         self.hora = hora
#         self.minutos = minutos
#         self.segundos = segundos

#     def mostrar_hora(self):
#         return f"{self.hora:02d}:{self.minutos:02d}:{self.segundos:02d}"
    
# reloj = Reloj(21, 5, 30)
# print(reloj.mostrar_hora())
# print(reloj.interruptor()) 