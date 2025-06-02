def calcular_monto(precio = 0, cantidad = 0):
    return precio * cantidad

precio = float(input("ingrese el precio: "))
cantidad = int(input("ingrese la cantidad: "))

monto = calcular_monto(precio, cantidad)

print(f"El monto es: {monto}")