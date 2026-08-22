def soma(*numeros):
    for numero in numeros:
        if numero < 0:
            raise ValueError("Nao e permitido numeros negativos")
    for numero in numeros:
        if not isinstance(numero, int):
            raise TypeError("Apenas numeros inteiros sao permitidos")
    return sum(numeros)
