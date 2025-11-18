import threading
import time
import msvcrt  # solo en Windows

detener_evento = threading.Event()

def contar():
    segundos = 0
    while not detener_evento.is_set():
        print(f"{segundos} segundos")
        time.sleep(1)
        segundos += 1

hilo = threading.Thread(target=contar)
hilo.start()

print("Pulsa cualquier tecla para detener...\n")
while True:
    if msvcrt.kbhit():
        msvcrt.getch()
        detener_evento.set()   # señal de parada
        break

hilo.join()
print("Contador detenido.")
