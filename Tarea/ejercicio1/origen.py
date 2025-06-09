import operaciones as op
from operaciones import limpiar as lim
import time as t
def main():  
    lim()

    while True:
        numero = input("Ingresa un número entero no negativo \n--> ")

        try:
            numero = int(numero)
            if numero < 0:
                print("Error: el número debe ser no negativo.\n")
                t.sleep(2)
                lim()
                continue
        except ValueError:
            print("Error: debes ingresar un número entero.\n")
            t.sleep(2)
            lim()
            continue

        resultado = op.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
        break
