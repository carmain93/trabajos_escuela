from examen import ListaEnlazada
class ListaEnlazada(ListaEnlazada):
    
    def suma_recursiva(self,nodo = None):
        if nodo is None:
            nodo=self.cabeza
        if nodo in None:
            return 0
        return nodo.valor + self.suma_recursiva(nodo.siguiente)
    
#crear una lista y probar el metodo
mi_lista = ListaEnlazada()
mi_lista.agregar_elemento(3)
mi_lista.agregar_elemento(7)
mi_lista.agregar_elemento(10)
print("suma de la lista es: ", mi_lista.suma_recursiva())
