class Node: 
    def __init__(self, num):
        self.num=num
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
        
#insertar nodo al inicio
    def inas(self, num):
        new_node = Node(num)
        if (self.head is None):
            self.head = new_node
            return
        current=self.head
        while(current.next):
            current=current.next#si el nodo existe sera igual al siguiente
        current.next=new_node#so el nodo ya existe sera igual al primero
    
    def pll(self):
        current=self.head
        while current:
            print(current.num,"->",end="")
            current=current.next#mientras exista el nodo sera igual al siguiente
    
    def esp(self,num):
        if (self.head is None):
            print("lista vacia")
            return False
        
        current= self.head
        while current.num != num:
            current=current.next
            if current is None:
                print("no existe")
                return False
            
        print(f"{num}")
        return True
    
    def das(self):
        if(self.head is None):
            print("no hay nada que borar")
            return
        self.head=self.head.next
    
    def dae(self):
        if self.head is None:
            print("nada que borrar")
            return
        if self.head.next is None:
            self.head=None 
            return
        current=self.head #itera
        while current.next.next:
            current=current.next
        current.next=None
        #borramos solo un elemento
        
    def exi(self,num):
        if (self.head is None):
            print("lista vacia")
            return False
        
        current= self.head
        while current.num != num:
            current=current.next
            if current is None:
                print("no existe")
                return False
            
        print("existe ")
        return True
        
#Creacion de las listas
my_list=LinkedList()
my_list.inas(5)
my_list.inas(6)
my_list.inas(7)
my_list.das()
my_list.dae()
my_list.pll()
my_list.exi(6)

primero=LinkedList()
primero.inas("Charmander")
primero.inas("Charmeleon")
primero.inas("Charizard")
segundo=LinkedList()
segundo.inas("Pichu")
segundo.inas("Pikachu")
segundo.inas("Raichu")
tercero=LinkedList()
tercero.inas("Squirtle")
tercero.inas("Wartotle")
tercero.inas("Blastoise")
cuarto=LinkedList()
cuarto.inas("Carterpie")
cuarto.inas("Metapod")
cuarto.inas("Butterfree")
quinto=LinkedList()
quinto.inas("Bulbasaur")
quinto.inas("Ivysaur")
quinto.inas("Venusaur")
#La lista completa, la ultima evolución del primer pokemon y determina si la primer y ultima evolucion existe .
primero.pll()
primero.esp("Charizard")
primero.exi("Charmander")
primero.exi("Charizard")
#La lista completa, la evolución mas conocida del segundo pokemon y determina si la segunda evolucion existe.
segundo.pll()
segundo.esp("Pikachu")
segundo.exi("Pikachu")
#La lista completa, la evolucción mas poderosa del tercer pokemon y determina si su versión mas conocida existe
tercero.pll()
tercero.esp("Blastoise")
tercero.esp("Squirtle")
#La lista completa del cuarto pokemon, sus dos ultimas evoluciones y determina si la primer evolución existe.
cuarto.pll()
cuarto.esp("Metapod")
cuarto.esp("Butterfree")
cuarto.exi("Carterpie")
#La lista completa del quinto pokemon, y determina según tu criterio mediante eliminación cual es la evolución mas poderosa.
quinto.pll()
quinto.das()
quinto.das()
print("")
quinto.pll()
