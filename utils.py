from time import time


def print_execution_time(name: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                print('{}:\t\t{}s'.format(name, round(time() - start, 2)))
        return wrapper
    return decorator

