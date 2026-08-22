def soma(*numeros):
    if numeros is None or len(numeros) == 0:
        raise ValueError("Nenhum numero fornecido para soma")
    for numero in numeros:
        if not isinstance(numero, int):
            raise TypeError("Apenas numeros inteiros sao permitidos")
    return sum(numeros)
