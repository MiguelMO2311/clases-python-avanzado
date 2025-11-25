import time
from multiprocessing import Process

def elevar_cuadrado(numero):
    """Función que eleva un número al cuadrado"""
    resultado = numero ** 2
    print(f"[Proceso {numero}] - {numero}^2 = {resultado}")

if __name__ == "__main__":
    # 8 números para 8 procesos
    numeros = list(range(1, 9))  

    procesos = [Process(target=elevar_cuadrado, args=(n,)) for n in numeros]
    # medir tiempo de inicio
    inicio = time.time() 

    # Lanzamos todos los procesos
    for p in procesos:
        p.start()

    # Esperamos a que terminen
    for p in procesos:
        p.join()
    # medir tiempo de fin
    fin = time.time()  

    print(f"Todos los procesos han terminado en {fin - inicio:.4f} segundos")
