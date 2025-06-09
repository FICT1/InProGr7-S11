from oringen import convertir_numero, limpiar
import time


def main():
    limpiar()
    while True:
        numero_decimal = input("Ingresa un número decimal: ")
        try:
            numero_decimal = int(numero_decimal)
            if numero_decimal < 0:
                print("Error: el número debe ser no negativo.")
                continue
            break
        except ValueError:
            print("Error: debes ingresar un número entero.")
            time.sleep(2)
            limpiar()
            continue
    numero_binario = convertir_numero(numero_decimal)
    print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")

main ()

