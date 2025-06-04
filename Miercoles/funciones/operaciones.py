#nombre de las funciones son verbos
def sumar (num1 = 0, num2 = 0):
    return num1 + num2

def restar (num1 = 0, num2 = 0):
    return num1 - num2

def multiplicar (num1 = 0, num2 = 0):
    return num1 * num2

def dividir (num1 = 0, num2 = 0):
    if num2 == 0:
        return "no se puede dividir por 0"
    return  num1 / num2


def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. Resuelve (x+2y)/z")
def limpiar():
    import os
    os.system ("cls || clear")

def presionar():
    input("Presione enter para volver al menu...")


