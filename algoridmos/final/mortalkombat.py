class NodoPersonaje:
    def __init__(self,nombre,poder,valoracion):
        self.nombre= nombre
        self.poder = poder
        self.valoracion=valoracion
        self.siguiente= None

nodo1= NodoPersonaje("scorpion","fuego",96)
nodo2=NodoPersonaje("subzero","hielo",95)
nodo3=NodoPersonaje("shao khan","fuerza",98)

#enlace nodo
nodo1.siguiente=nodo2
nodo2.siguiente=nodo3
#funcion para mostrar la informacion del codigo
def mostrar_info(nodo):
    print("Nombre:",nodo.nombre)
    print("Poder:",nodo.poder)
    print("Valoracion",nodo.valoracion)
    print("-------------------------------")
    
mostrar_info(nodo1)
mostrar_info(nodo2)
mostrar_info(nodo3)