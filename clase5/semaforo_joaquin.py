import threading
import time

# Voy a compartir esto
recurso = []

# Semaforo de 2
sem = threading.Semaphore(2)

def usar_recurso():
    with sem:
        print(f"Hilo {threading.current_thread().name} usando el recurso")
        time.sleep(1)
        print(f"Hilo {threading.current_thread().name} liberando el recurso")

# Para que veas como funciona, voy a usar 20 hilos
hilos = [threading.Thread(target=usar_recurso, name=f"Hilo-{i+1}") for i in range(10)]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()