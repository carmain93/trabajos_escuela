class Estudiante:
    def init(self,nombre,edad,calificacion):
        self.nombre=nombre
        self.edad= edad
        self.calificacion=calificacion

#crear el arreglo
estudiante =[
    Estudiante("Miguel",20,85),
    Estudiante("Brisa",22,70),
    Estudiante("Jesus",18,92),
    Estudiante("Jordan",21,68),
    Estudiante("Mich",24,91),
    Estudiante("Rodolfo",25,79)
]

print(estudiante.nombre)
#estudiante con la calificacion mas alta
maxestu=max(estudiante,key=lambda estudiante: estudiante.calificacion)

    
    
print(f"estudiante con la calificacion mas alta")
print(f"nombre: {maxestu.nombre}")
print(f"edad: {maxestu.edad}")
print(f"calificacion: {maxestu.calificacion}")
