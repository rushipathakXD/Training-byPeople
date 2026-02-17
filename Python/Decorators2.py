def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_value = ', '.join(str(arg) for arg in args)
        print(f"Function name: {func.__name__} and arguments: {args_value}")
        return result
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Rushi")