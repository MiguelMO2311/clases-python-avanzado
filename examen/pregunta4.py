def require_string(func):
    def wrapper(s, *args, **kwargs):
        if not isinstance(s, str):
            raise TypeError("Argument must be a string")
        return func(s, *args, **kwargs)
    return wrapper

def add_info(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Processed: {result}"
    return wrapper

@require_string
@add_info
def process(s: str):
    return s.upper()
