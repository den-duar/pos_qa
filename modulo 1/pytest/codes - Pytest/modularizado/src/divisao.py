def divisao(*numeros):
    if numeros is None or len(numeros) == 0:
        raise ValueError("Nenhum numero fornecido para divisao")
    for numero in numeros:
        if not isinstance(numero, (int, float)):
            raise TypeError("Apenas numeros sao permitidos")
    resultado = numeros[0]
    for numero in numeros[1:]:
        if numero == 0:
            raise ZeroDivisionError("Divisao por zero nao e permitida")
        resultado /= numero
    return resultado