def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    elif not isinstance(n, int):
        raise TypeError("Fatorial só é definido para números inteiros")
    elif n == 0:
        return 1
    else:
        return n * fatorial(n - 1)