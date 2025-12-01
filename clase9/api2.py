# Versión original sin hilos, realizada por Joaquín
# import time
# import math

# def cpu_heavy_hard():
#     N = 50_000_000
#     checksum = 0.0

#     t0 = time.perf_counter()
#     _math_sqrt = math.sqrt
#     _math_sin = math.sin

#     for i in range(1, N + 1):
#         checksum += _math_sqrt(i) * _math_sin(i)

#     elapsed = time.perf_counter() - t0
#     return elapsed, N, checksum

# if __name__ == "__main__":
#     elapsed, iters, chk = cpu_heavy_hard()
#     print(f"Tiempo: {elapsed:.3f} s — Iteraciones: {iters} — checksum: {chk:.6f}")


import time
import math
from multiprocessing import Pool

# Función que calcula el checksum en un rango concreto
def cpu_heavy_batch(rango):
    inicio, fin = rango
    checksum = 0.0
    _math_sqrt = math.sqrt
    _math_sin = math.sin

    for i in range(inicio, fin):
        checksum += _math_sqrt(i) * _math_sin(i)

    return checksum

if __name__ == "__main__":
    N = 50_000_00
    num_procesos = 4

    # Dividimos N en batches iguales
    batch_size = N // num_procesos
    batches = [(i * batch_size + 1, (i + 1) * batch_size + 1) for i in range(num_procesos)]

    t0 = time.perf_counter()

    # Creamos el pool de procesos y ejecutamos cada batch en paralelo
    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(cpu_heavy_batch, batches)

    # Sumamos todos los checksums parciales
    checksum_total = sum(resultados)
    elapsed = time.perf_counter() - t0

    print(f"Tiempo total: {elapsed:.3f} s — Iteraciones: {N} — checksum: {checksum_total:.6f}")
