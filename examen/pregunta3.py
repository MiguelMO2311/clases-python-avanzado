import asyncio

async def worker(i):
    await asyncio.sleep(0.01)
    return i*2

async def main():
    tasks = [asyncio.create_task(worker(i)) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
