# import requests
# from threading import Thread, Semaphore

# sem = Semaphore(10)

# def request_url(url:str):
#     global active_sessions
#     with sem:
#         try:
#             response = requests.get(url)
#             print(f"Request on {url} -> status {response.status_code}")
#         except requests.exceptions.Timeout:
#             print(f"Timout on {url}")
#         except Exception as e:
#             print(f"Could not get {url} Error ---> {e}")

# if __name__ in "__main__":
#     centenar_urls = [f"https://httpbin.org/get?p={i}" for i in range(100)]
#     threads = [Thread(target=request_url, args=(url,)) for url in centenar_urls]
#     threads_started = []
#     for t in threads:
#         threads_started.append(t)
#         t.start()

#     for th in threads_started:
#         t.join()
 
 
# import requests
# from concurrent.futures import ProcessPoolExecutor, as_completed

# def request_url(url: str):
#     try:
#         response = requests.get(url)
#         return f"Request on {url} -> status {response.status_code}"
#     except requests.exceptions.Timeout:
#         return f"Timeout on {url}"
#     except Exception as e:
#         return f"Could not get {url} Error ---> {e}"

# if __name__ == "__main__":
#     centenar_urls = [f"https://httpbin.org/get?p={i}" for i in range(50)]

#     with ProcessPoolExecutor(max_workers=4) as executor:
#         # Lanzamos cada tarea con submit → devuelve un Future
#         futures = [executor.submit(request_url, url) for url in centenar_urls]

#         # Proceso de resultados conforme van llegando
#         for future in as_completed(futures):
#             print(future.result())
import time, os
import math
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy_function(args):
    start_i, end_i = args
    checksum = 0.0
    t0 = time.perf_counter()
    _math_sqrt = math.sqrt
    _math_sin = math.sin

    for i in range(start_i, end_i):
        checksum += _math_sqrt(i) * _math_sin(i)

    elapsed = time.perf_counter() - t0
    # devolvemos el PID para ver qué proceso lo ejecutó
    return os.getpid(), elapsed, (end_i - start_i), checksum

if __name__ == "__main__":
    workers = cpu_count() - 1   # usamos todos los núcleos menos 1
    N_total = 50_000_000        # número total de iteraciones

    # dividimos el trabajo en chunks
    chunk_size = N_total // workers
    ranges = []
    start = 1
    for w in range(workers):
        end = start + chunk_size
        if w == workers - 1:
            end = N_total + 1   # último proceso llega hasta el final
        ranges.append((start, end))
        start = end

    # lanzamos los procesos con submit
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futuros = [pool.submit(cpu_heavy_function, r) for r in ranges]

        # recogemos resultados
        for f in futuros:
            os_id, elapsed, iters, chk = f.result()
            print(f"PID {os_id} — Tiempo: {elapsed:.3f} s — Iteraciones: {iters} — checksum: {chk:.6f}")
