from operaciones import suma_digitos_potencia
from origen import limpiar as lim
from origen import t

def main():
    lim()
    while True:
        try:
            print("**Suma de los dígitos de un número elevado a un exponente**")
            numero = int(input("Ingresa un número entero positivo: "))
            exponente = int(input("Ingresa el exponente: "))
            if numero < 0 or exponente < 0:
                print("Error: ambos números deben ser positivos.")
                t.sleep(2)
                lim()
                continue
            break
        except ValueError:
            print("Error: debes ingresar números enteros.")
            t.sleep(2)
            lim()
            continue

    resultado, suma = suma_digitos_potencia(numero, exponente)
    print(f"\nEl numero {numero}^ a {exponente} da igual a = {resultado}")
    print(f"Y la suma de los dígitos es: {suma}")

main()
