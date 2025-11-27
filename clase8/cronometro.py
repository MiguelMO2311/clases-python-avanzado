# clase cronometro que tenga un metodo nuevo que me permita medir el tiempo, iterador y que tenga start y stop.

import time

class Cronometro:
    def __init__(self):
        self.inicio = None
        self.activo = False

    def start(self):
        self.inicio = time.time()
        self.activo = True

    def stop(self):
        self.activo = False

    def medir(self):
        if not self.inicio:
            return 0
        return int(time.time() - self.inicio)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.activo:
            raise StopIteration
        time.sleep(1)  # espera
        return self.medir()

# Ejemplo de uso
cronometro1 = Cronometro()
cronometro1.start()

for segundo in cronometro1:
    print(f"{segundo} segundo/s")
    if segundo >= 5:  # lo limitamos para que pare a los 5 segundos
        cronometro1.stop()
