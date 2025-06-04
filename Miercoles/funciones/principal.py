
import operaciones as operation

def main():
    while (True):
        operation.limpiar()
        operation.menu()
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            operation.limpiar()
            num1 = int(input("Ingrese el primer número: "))
            num2 =int(input("Ingrese el segundo número: "))
            suma=operation.sumar(num1, num2)
            print (f"La suma de {num1} y {num2} es {suma}")
            operation.presionar()
        elif op == 2:
            operation.limpiar()
            num1 = int(input("Ingrese el primer número: "))
            num2 =int(input("Ingrese el segundo número: "))
            resta=operation.restar(num1, num2)
            print (f"La resta de {num1} y {num2} es {resta}")
            operation.presionar()
        elif op == 3:
            operation.limpiar()
            num1 = int(input("Ingrese el primer número: "))
            num2 =int(input("Ingrese el segundo número: "))
            multi=operation.multiplicar(num1, num2)
            print (f"La multiplicacion de {num1} y {num2} es {multi}")
            operation.presionar()
        elif op == 4:
            operation.limpiar()
            num1 = int(input("Ingrese el primer número: "))
            num2 =int(input("Ingrese el segundo número: "))
            div=operation.dividir(num1, num2)
            print (f"La division de {num1} y {num2} es {div}")
            operation.presionar()
        elif op == 5:
            False
            break
        elif op == 6:
            x = int(input("Ingrese el valor de x: "))
            y = int(input("Ingrese el valor de y: "))
            z = int(input("Ingrese el valor de z: "))
            mult = operation.multiplicar(2, y)
            sum = operation.sumar(x, mult)
            div = operation.dividir(sum, z)
            print(f"El resultado es: {div}")
            operation.presionar()
        else:
            operation.limpiar()
            print("Opcion no válida")
            operation.presionar()


if __name__ == "__main__":
    main()