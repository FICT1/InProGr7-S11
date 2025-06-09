import operaciones as op

def main():  
    op.limpiar()

    while True:
        numero = input("Ingresa un número entero no negativo \n--> ")

        try:
            numero = int(numero)
            if numero < 0:
                print("Error: el número debe ser no negativo.\n")
                continue
        except ValueError:
            print("Error: debes ingresar un número entero.\n")
            continue

        resultado = op.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
        break
