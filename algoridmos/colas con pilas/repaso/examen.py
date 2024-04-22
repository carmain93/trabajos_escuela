class cola:
    def __init__(self):
        self.elementos=[]
    def vacia(self):
        if self.elementos==[]:
            print("la cola esta vacia")
            return True
        else:
            print("la cola existe")
            return False
        
    def agregar(self, nodo):
        self.elementos.append(nodo)
            
    def consultar(self):
        print(self.elementos)
            
    def eliminar(self):
        if self.vacia():
            print("la cola esta vacia")
        else:
            self.elementos=[]
    def secuencia(self,nodos):
        for i in nodos:
            self.agregar(i)
            
    def mostrar_se(self):
        for i in self.elementos:
            print(i)
            


p=cola()
p.agregar(3)
p.agregar(4)
p.consultar()
#p.eliminar()
p.consultar()
p.secuencia([5,6])
p.consultar()
p.mostrar_se()
while len(p.elementos)>0:
    print("Que desea haacer")
    print("1.-agreagar")
    print("2.- consultar")
    print("3.-eliminar")
    i=input("deme el numero de la opcion\n")
    if i=="1":
        print("escogio agregar")
    if i=="2":
        print("escogio ver")
    if i=="3":
        print("escogio eliminar")
        p.eliminar()
        
print("fin del ciclo")