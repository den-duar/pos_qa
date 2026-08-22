def potencia (base, expoente):
    if not isinstance(base, (int, float)):
        raise TypeError("A base deve ser um numero")
    if not isinstance(expoente, (int, float)):
        raise TypeError("O expoente deve ser um numero")
    return base ** expoente
