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
my_list.exi(3)