class fila():
    def __init__(self):
        self.elementos=[]
    
    def agregar(self,nodo):
        self.elementos.append(nodo)
    
    def consultar(self):
        print(self.elementos)
    def eliminar(self):
        self.elementos.pop()
    def vacia(self):
        if len(self.elementos)<0:
            print("pila vacia")
            return True
        else:
            return False
    def acciones(self):
        for i in self.elementos:
            print(i)
    
a=fila()
