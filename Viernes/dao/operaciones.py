#data access object
#DAO
class Estudiantedao:
    def __init__(self):
        self.estudiantes=[]

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar(self):
        return self.estudiantes