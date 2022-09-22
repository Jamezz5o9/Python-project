import functools
import time


def decorate(func):
    @functools.wraps(func)
    def wrap(*args, **Kwargs):
        print("I am before decorator")
        print(func(*args, **Kwargs))
        print("I am after decorator")

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **Kwargs):
        start = time.perf_counter()
        func = f(*args, **Kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@decorate
def hello(name):
    return f"Hello {name}"


@decorate
def add(x, y):
    return x + y


@performance_counter
@decorate
def add(x, y):
    """

  adds two numbers
    """

    return x + y


# hello = decorate(hello)
print(add.__name__)
print(add.__doc__)
hello("James")
add(2, 3)


def multiply(a, b):
    return a * b


multiply_by_5 = functools.partial(multiply, 5)
print(multiply_by_5(6))
