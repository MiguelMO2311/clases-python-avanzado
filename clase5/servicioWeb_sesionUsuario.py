# # Version con "lock"

# import time
# import random
# from threading import Thread, Lock

# sesiones_activas = 0
# lock = Lock()
# MAX_SESIONES = 10

# def sesion_usuario(cliente):
#     global sesiones_activas
#     with lock:  # protege el acceso concurrente
#         if sesiones_activas < MAX_SESIONES:
#             sesiones_activas += 1
#             print(f"[{cliente}]  clsSesión iniciada. Activas: {sesiones_activas}")
#         else:
#             print(f"[{cliente}]  No se pudo iniciar sesión (límite alcanzado)")
#             return

#     # Simula trabajo dentro de la sesión
#     time.sleep(random.uniform(0.5, 1.5))

#     # Al terminar, liberar sesión
#     with lock:
#         sesiones_activas -= 1
#         print(f"[{cliente}]  Sesión finalizada. Activas: {sesiones_activas}")

# def main(clientes):
#     threads = []
#     for cliente in clientes:
#         hilo = Thread(target=sesion_usuario, args=(cliente,))
#         threads.append(hilo)
#         hilo.start()

#     for hilo in threads:
#         hilo.join()

# if __name__ == "__main__":
#     clientes_prueba = [f"Cliente_{i}" for i in range(20)]
#     main(clientes_prueba)

# Version con "Semaforo"

import time
import random
from threading import Thread, Semaphore

MAX_SESIONES = 10
semaforo = Semaphore(MAX_SESIONES)

def sesion_usuario(cliente):
    # Intentar adquirir un "permiso" de sesión
    if semaforo.acquire(blocking=False):
        print(f"[{cliente}]  Sesión iniciada")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[{cliente}]  Sesión finalizada")
        semaforo.release()  # liberar permiso
    else:
        print(f"[{cliente}]  No se pudo iniciar sesión (límite alcanzado)")

def main(clientes):
    threads = []
    for cliente in clientes:
        hilo = Thread(target=sesion_usuario, args=(cliente,))
        threads.append(hilo)
        hilo.start()

    for hilo in threads:
        hilo.join()

if __name__ == "__main__":
    clientes_prueba = [f"Cliente_{i}" for i in range(20)]
    main(clientes_prueba)

"""
Comparación Lock vs Semaphore:

- Lock: Sirve como un candado para proteger un recurso compartido.
  Útil si quieres controlar manualmente un contador o una sección crítica,
  pero requiere que tú lleves la lógica de rechazo.

- Semaphore: Solo deja pasar a un número fijo de hilos.
  En este caso, refleja directamente la restricción de infraestructura:
  máximo 10 sesiones simultáneas. No necesitas contar nada, el semáforo lo hace solo.

Conclusión:
Prefiero usar Semaphore porque es más claro, elegante y reduce errores
al limitar directamente cuántas sesiones pueden estar activas a la vez.
"""
