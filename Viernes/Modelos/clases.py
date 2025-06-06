class estudiante:
    
    def __init__(self, nombre, apellidos, carrera, nota):
        self.first_name = nombre
        self.last_name = apellidos
        self.major = carrera
        self.nota = nota
    
    def __str__(self):
        return f"**Datos del estudiante** \n Nombre completo: {self.first_name} {self.last_name} \n Carrera: {self.major} \n nota: {self.nota}"
    
