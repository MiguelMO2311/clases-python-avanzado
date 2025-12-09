def _inner(x):
    return x * x

def make_tasks():
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(_inner, range(5)))
    return results
