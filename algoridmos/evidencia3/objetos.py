class Estudiante:
    def __init__(self,nombre,edad,calificacion):
        self.nombre=nombre
        self.edad= edad
        self.calificacion=calificacion

#crear el arreglo
estudiantes =[
    Estudiante("Miguel",20,85),
    Estudiante("Brisa",22,70),
    Estudiante("Jesus",18,92),
    Estudiante("Jordan",21,68),
    Estudiante("Mich",24,91),
    Estudiante("Rodolfo",25,79)
]


#estudiante con la calificacion mas alta
maxestu=max(estudiante.calificacion for estudiante in estudiantes)

print("estudiantes con maxima calificacion")
for estudiante in estudiantes:
    if estudiante.calificacion == maxestu:
        print(f"estudiante con la calificacion mas alta")
        print(f"nombre: {estudiante.nombre}")
        print(f"edad: {estudiante.edad}")
        print(f"calificacion: {estudiante.calificacion}")
