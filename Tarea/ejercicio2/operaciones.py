# Ejercicio 2: Convertir un número decimal a binario
# Planteamiento: Escribe una función que reciba un número entero positivo y devuelva una cadena con su representación en binario (base 2). Por ejemplo, si se ingresa 10, la función debe devolver "1010". No uses funciones integradas de conversión a binario; implementa la lógica dividiendo el número y construyendo la cadena manualmente.


def decimal(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        if n % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        n = n // 2
    return binario
