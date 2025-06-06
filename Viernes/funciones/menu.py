import Modelos.clases as m
import dao.operaciones as o

lista = o.Estudiantedao()

def menu():
    print ("**Menu principal**")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")


def agregar_estudiante():
    print("Digite los siguientes datos del estudiante")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")
    promedio = int(input("Promedio: "))
    est = m.estudiante(nombre, apellido, carrera, promedio)
    lista.agregar_estudiante(est)

def mostrar_estudiantes():
    print("Regisistro de estudiantes")
    for est in lista.mostrar():
        print(est)


def main ():
    while (True):
        menu()
        opcion = input ()
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print("Adios")
            break
        else :
            print("Opcion no valida")