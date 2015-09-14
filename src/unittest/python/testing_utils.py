from functools import wraps

def reported(foo):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        print(foo.__name__)
        return foo(*args, **kwargs)
    return wrapper

