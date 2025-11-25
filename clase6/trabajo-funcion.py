import time
from threading import Thread

def trabajo(nombre):
    """Función que simula un trabajo con entrada, espera y salida"""
    print(f"[{nombre}] Entrando al trabajo")
    time.sleep(2)  
    print(f"[{nombre}] Saliendo del trabajo")

if __name__ == "__main__":
    # Creamos dos hilos que ejecutan la misma función
    hilo1 = Thread(target=trabajo, args=("Hilo_1",))
    hilo2 = Thread(target=trabajo, args=("Hilo_2",))

    # Iniciamos los hilos
    hilo1.start()
    hilo2.start()

    # Esperamos a que terminen
    hilo1.join()
    hilo2.join()

    print("Todos los hilos han terminado")
