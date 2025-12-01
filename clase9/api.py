import asyncio
import aiohttp

URL = "https://motivational-spark-api.vercel.app/api/quotes"

async def hacer_get(session, i):
    async with session.get(URL) as resp:
        print(f"GET {i}: {resp.status}")
        return await resp.json()

async def hacer_post(session, i):
    datos = {"autor": f"user{i}", "quote": "Usando API con asyncio"}
    async with session.post(URL, json=datos) as resp:
        print(f"POST {i}: {resp.status}")
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tareas = []
        # 18 GET
        for i in range(18):
            tareas.append(hacer_get(session, i))
        # 2 POST
        for i in range(2):
            tareas.append(hacer_post(session, i))

        # Ejecutar todas las tareas en paralelo
        resultados = await asyncio.gather(*tareas)
        print("Total de respuestas:", len(resultados))

# Ejecutar el bucle principal
asyncio.run(main())
