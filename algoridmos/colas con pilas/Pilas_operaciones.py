class Pila:
    def __init__(self):
        self.elementos=[]
    #insertar
    
    def insertar(self,dato):
        self.elementos.append(dato)
        
    def esta_vacia(self):
        return len(self.elementos)==0
    #sacar elemento
    def quitar(self):
        if self.esta_vacia():
            print("pila vacia")
            return None
        return self.elementos
    def limpiar(self):
        del self.elementos[:]
        
    def cima(self):
        return len(self.elementos)
    #mostar elementos
    def mostrar_elementos(self):
        print("los elementos de la pila son: ")
        print(self.elementos)
        
a=Pila()
a.insertar(1)
a.insertar(2)
a.insertar(3)
a.mostrar_elementos()
print(a.cima())