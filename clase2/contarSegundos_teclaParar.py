import threading
import time

# Variable de control
detener = False

def contar():
    segundos = 0
    while not detener:
        print(f"{segundos} segundos")
        time.sleep(1)
        segundos += 1

# Lanzar el hilo como demonio (no bloquea la salida del programa)
threading.Thread(target=contar, daemon=True).start()

# El hilo principal espera a que presiones Enter
input("Presiona Enter para detener...\n")
detener = True

print("Contador detenido.")
