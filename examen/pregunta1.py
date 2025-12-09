import threading, time

counter = 0
lock = threading.Lock()

def task():
    global counter
    for _ in range(1000):
        with lock:
            tmp = counter
            time.sleep(0.05)
            tmp += 1
            counter = tmp

# ¿Está este código bien diseñado, o presenta alguna mejora?
# A) Se debe reemplazar eemplazar threading.Thread por multiprocessing.Process y compartir counter con multiprocessing.Value. 
# B) EL código esta bien, lo unico, que se podria hacer más seguro con threading.Semaphore() y acquire()/release() alrededor del código que modifica counter.
# C) Hay una condición de carrera, y se debe añadir un threading.Lock() y usar with lock: alrededor de la lectura/incremento/asignación de counter.
# D) El código está perfectamente diseñado y no necesita cambios
# tmp = counter
# time.sleep(0.05)
# tmp += 1
# counter = tmp


# ✅ La opción correcta es:
# C) Hay una condición de carrera, y se debe añadir un threading.Lock() 
# y usar with lock: alrededor de la lectura/incremento/asignación de counter.