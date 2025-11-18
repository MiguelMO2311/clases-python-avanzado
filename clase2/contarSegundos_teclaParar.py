import threading
import time
import msvcrt  # disponible en la librería estándar de Windows

detener = False

def contar():
    segundos = 0
    while not detener:
        print(f"{segundos} segundos")
        time.sleep(1)
        segundos += 1

hilo = threading.Thread(target=contar)
hilo.start()

print("Pulsa cualquier tecla para detener...\n")
while True:
    if msvcrt.kbhit():   # detecta pulsación
        msvcrt.getch()   # lee la tecla
        detener = True
        break

# Espera a que el hilo termine
hilo.join()
print("Contador detenido.")
