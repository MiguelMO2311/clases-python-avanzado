import json
import threading

# -------------------------
# Datos JSON de ejemplo (en memoria)
# -------------------------

json1 = {
    "empresa": "TechCorp",
    "empleados": [
        {"id": 1, "nombre": "Laura", "departamento": "IT"},
        {"id": 2, "nombre": "Carlos", "departamento": "Ventas"},
        {"id": 3, "nombre": "María", "departamento": "Marketing"},
        {"id": 4, "nombre": "Diego", "departamento": "Finanzas"}
    ],
    "proyectos": {
        "activos": ["Alpha", "Beta", "Gamma", "Delta"],
        "finalizados": ["Omega", "Sigma", "Lambda"]
    },
    "config": {
        "version": "1.4.8",
        "modulos": {
            "seguridad": True,
            "sincronizacion": True,
            "analitica": True
        }
    }
}

json2 = {
    "usuarios": ["Ana", "Luis", "Pedro"],
    "activo": True
}

json3 = {
    "items": list(range(100)),
    "metadata": {"source": "test"}
}

# Guardamos los JSON en archivos

with open("json1.json", "w", encoding="utf-8") as archivo1:
    json.dump(json1, archivo1, ensure_ascii=False, indent=2)

with open("json2.json", "w", encoding="utf-8") as archivo2:
    json.dump(json2, archivo2, ensure_ascii=False, indent=2)

with open("json3.json", "w", encoding="utf-8") as archivo3:
    json.dump(json3, archivo3, ensure_ascii=False, indent=2)

# Función para leer y medir longitud

def calcular_longitud_json(ruta_archivo, nombre):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo_json:
            contenido = json.load(archivo_json)

        if isinstance(contenido, (dict, list)):
            longitud = len(contenido)
        else:
            longitud = 1  # si es un valor simple

        print(f"{nombre} -> longitud: {longitud}")

    except FileNotFoundError:
        print(f"{nombre} -> ERROR: archivo {ruta_archivo} no encontrado")
    except json.JSONDecodeError as e:
        print(f"{nombre} -> ERROR: contenido JSON inválido ({e})")
    except Exception as e:
        print(f"{nombre} -> ERROR inesperado: {e}")

# Lanzamos los hilos

threads = [
    threading.Thread(target=calcular_longitud_json, args=("json1.json", "JSON 1")),
    threading.Thread(target=calcular_longitud_json, args=("json2.json", "JSON 2")),
    threading.Thread(target=calcular_longitud_json, args=("json3.json", "JSON 3")),
]

for thread_obj in threads:
    thread_obj.start()

for thread_obj in threads:
    thread_obj.join()
