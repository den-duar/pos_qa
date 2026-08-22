def multiplicacao(*numeros):
    if numeros is None or len(numeros) == 0:
        return 0
    for numero in numeros:
        if not isinstance(numero, int):
            raise TypeError("Apenas numeros inteiros sao permitidos")
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado