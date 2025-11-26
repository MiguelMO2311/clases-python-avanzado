import asyncio
import httpx

def normalizar_frase(data: dict) -> dict[str, str]:
    """
    Normaliza la estructura de la frase para que siempre tenga 'quote' y 'author'.
    """
    return {
        "quote": data.get("quote") or data.get("q") or data.get("phrase", "Sin texto"),
        "author": data.get("author") or data.get("a") or "Anónimo"
    }

async def obtener_frase(url: str, index: int = 0) -> dict[str, str]:
    """
    Obtiene y normaliza una frase desde la URL dada.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()

            if isinstance(data, list):
                if index < len(data):
                    return normalizar_frase(data[index])
                else:
                    return {"quote": f"Índice {index} fuera de rango", "author": "Sistema"}
            elif isinstance(data, dict):
                return normalizar_frase(data)
            else:
                return {"quote": "Formato inesperado", "author": "Sistema"}
        except Exception as e:
            return {"quote": f"Error: {e}", "author": "Sistema"}

async def main(urls: list[str], index: int = 0):
    """
    Lanza tareas para obtener frases desde múltiples URLs en paralelo.
    """
    resultados = await asyncio.gather(*(obtener_frase(url, index) for url in urls))

    for i, frase in enumerate(resultados, start=1):
        print(f"[{i}] {frase['quote']} — {frase['author']}")

if __name__ == "__main__":
    urls = [
        "https://motivational-spark-api.vercel.app/api/quotes",
        "https://zenquotes.io/api/quotes",
        "https://frasedeldia.azurewebsites.net/api/phrase"
    ]
    asyncio.run(main(urls, index=1))
