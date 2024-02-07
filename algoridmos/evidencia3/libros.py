class Libro:
    def __init__(self, titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
    def __repr__(self):
        return(self.titulo)
        
        
libros=[
    Libro("El principito","antonie desant"),
    Libro("1984","george orwell"),
    Libro("el señor de los anillo","j.r.r tolkien"),
    Libro("harry pother","j.k. rowlling"),
    Libro("la historia del loco", "jhon katzenbacj")
]
#busqueda por autor
busautor="j.k. rowlling"


#busqueda libro por autor
encontrarlibro = next((libro for libro in libros if libro.autor ==busautor), None)
print(encontrarlibro)

print(f"arreglos de libros:")

for libro in libros:
    print(f"{libro.titulo} - {libro.autor}")
    
if encontrarlibro:
    print(f"\nlibro encontrado del autor'{busautor}':{encontrarlibro}")
else:
    print(f"\nNo se encontro ningun libro dle autor '{busautor}'.")
   