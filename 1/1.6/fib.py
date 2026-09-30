import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.6f} с")
        return result

    return wrapper


def next_fib(a, b):
    return a + b


@timeit
def fib_while(a, b, n):
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, next_fib(a, b)
    return result


@timeit
def fib_range(a, b, n):
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, next_fib(a, b)
    return result


@timeit
def fib_generator(a, b, n):
    def gen(a, b, n):
        for _ in range(n):
            yield a
            a, b = b, next_fib(a, b)

    return list(gen(a, b, n))


if __name__ == "__main__":
    print(fib_while(0, 1, 10), end='\n\n')
    print(fib_range(0, 1, 10), end='\n\n')
    print(fib_generator(0, 1, 10), end='\n\n')

    n = 100000
    print(f"Замер времени для n = {n} чисел Фибоначчи:")
    res_while = fib_while(0, 1, n)
    res_range = fib_range(0, 1, n)
    res_generator = fib_generator(0, 1, n)

    print("Результаты совпали: ", res_while == res_range and res_range == res_generator)
