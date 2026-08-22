def subtracao(*numeros):
    if numeros is None or len(numeros) == 0:
        raise ValueError("Nenhum numero fornecido para subtracao")
    for numero in numeros:
        if not isinstance(numero, int):
            raise TypeError("Apenas numeros inteiros sao permitidos")
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado -= numero
    return resultado