def limpiar():
    import os
    os.system ("cls || clear")
def factorial (n):
    try:
        n= int(n)
    except ValueError:
        return ("El valor ingresado no es un numero entero")
    if n < 0:
        return ("El factorial de un numero negativo no existe")
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

