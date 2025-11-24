import time
from threading import Thread, Lock

habitaciones_disponibles = 10
lock = Lock()

# "lock" protege el acceso concurrente
def reservar_habitacion(cliente):
    global habitaciones_disponibles
    with lock:  
        if habitaciones_disponibles > 0:
            print(f"[{cliente}] - {habitaciones_disponibles} habitaciones disponibles")
            time.sleep(0.1) 
            habitaciones_disponibles -= 1
            print(f"[{cliente}] Reserva confirmada. Quedan {habitaciones_disponibles}")
        else:
            print(f"[{cliente}] No hay habitaciones disponibles")

def main(clientes):
    threads = []
    for cliente in clientes:
        hilo = Thread(target=reservar_habitacion, args=(cliente,))
        threads.append(hilo)
        hilo.start()

    for hilo in threads:
        hilo.join()

if __name__ == "__main__":
    
# Ejemplo: 15 clientes intentando reservar 10 habitaciones
    clientes_prueba = [f"Cliente_{i}" for i in range(15)]
    main(clientes_prueba)
