def fib(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n musi być liczbą całkowitą.")
    if n < 0:
        raise ValueError("n nie może być ujemne.")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(0))
print(fib(1))
print(fib(7))
