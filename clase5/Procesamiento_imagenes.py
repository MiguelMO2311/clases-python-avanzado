import time
import random
from threading import Thread

def procesar_imagen(nombre_imagen):
    print(f"Iniciando procesamiento de {nombre_imagen}")
    time.sleep(random.uniform(0.5, 1.5))  # simula trabajo
    print(f"{nombre_imagen} procesada y guardada")

def main(imagenes):
    threads = []

    # Crear y lanzar un hilo por cada imagen de la lista
    for img in imagenes:
        hilo = Thread(target=procesar_imagen, args=(img,))
        threads.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in threads:
        hilo.join()

if __name__ == "__main__":
    # usamos la lista que nos den
    imagenes_prueba = ["foto1.jpg", "foto2.jpg", "foto3.jpg", "foto4.jpg"]  # ejemplo con 4
    main(imagenes_prueba)

