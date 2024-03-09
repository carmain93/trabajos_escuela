class Personaje:
    
    def __init__(self,nombre, velocidad, fuerza, agilidad, resistencia, poder ):
        self.nombre= nombre
        self.velocidad= velocidad
        self.fuerza=fuerza
        self.agilidad=agilidad
        self.resistencia=resistencia
        self.poder=poder
        self.siguiente= None
        
def mostrar(nodo):
    print("nombre: ",nodo.nombre)
    print("Velocidad: ",nodo.velocidad)
    print("Fuerza: ",nodo.fuerza)
    print("Agilidad",nodo.agilidad)
    print("Resistencia: ",nodo.resistencia)
    print("Poder: ",nodo.poder)
    print("-------------------------------")
    

#asignaci0on perosnaje
nodo1 = Personaje("Scorpion", 85, 55, 75, 45, "Spear Slam")
nodo2= Personaje("Sub-Zero", 40, 85, 45, 85, "Frostbite Fury")
nodo3 = Personaje("Liu Kang", 75, 50, 80, 55, "Dragon Kick")
nodo4 = Personaje("Raiden", 90, 60, 70, 80, "Thunderstorm Asault")
nodo5= Personaje("Sonya Blade", 60, 50, 75, 50, "Sonic Pulse")
nodo6 = Personaje("Johnny Cage", 80, 55, 80, 50, "Groin Stricke")
nodo7 = Personaje("Kitana", 85, 50, 75, 55, "Fan Blade Whirlwind")
nodo8 = Personaje("Kano", 55, 80, 75, 50, "Laser Eye Beam")
nodo9 = Personaje("Jax", 50, 85, 50, 80, "Sonic Wave Punch")
nodo10= Personaje("Mileena", 90, 55, 80, 50, "Tarkatan Bite")
nodo11 = Personaje("Baraka", 50, 85, 50, 80, "Blade Barrage")
nodo12 = Personaje("Shang Tsung", 55, 55, 75, 55, "Shape-shifter's Gambit")
nodo13 = Personaje("Shao Khan", 25, 90, 25, 90, "Kahn's Wrath")
nodo14 = Personaje("Kung Lao", 80, 55, 80, 55, "Razor Hat Spin")
nodo15 = Personaje("Reptile", 90, 55, 80, 50, "Acid Spid")
nodo16 = Personaje("Goro", 20, 90, 20, 90, "Double Fist Smash")
nodo17 = Personaje("Quan Chi", 55, 30, 55, 50, "Dark Sorcery")
nodo18 = Personaje("Cyrax", 85, 50, 75, 50, "Net Boom")
nodo19 = Personaje("Smoke", 85, 50, 75, 50, "Teleportation Asault")
nodo20 = Personaje("Noob Saibot", 90, 85, 90, 30, "Shadow Clone Onslaught")
nodo21 = Personaje("Sindel", 80, 50, 75, 50, "Sonic Scream")
nodo22 = Personaje("Nightwolf", 90, 55, 80, 55, "Spirit Arrow Barrage")
nodo23 = Personaje("Kabal", 85, 55, 80, 50, "Rapid Blade Assault")
nodo24 = Personaje("Shinnok", 55, 90, 50, 85, "Soul Theft")
nodo25 = Personaje("Fujin", 90, 50, 75, 50, "Wind Blade Clone")
nodo26 = Personaje("Kotal Kahn", 25, 90, 25, 90, "Solar Beam")
nodo27 = Personaje("Cassie Cage", 90, 50, 75, 50, "Gatling Gun kick")
nodo28 = Personaje("D'Vorah", 90, 50, 75, 50, "Deadly Swaem Asault")
nodo29 = Personaje("Erron Black", 90, 90, 90, 55, "Precision Marksman")
nodo30 = Personaje("Jacqui Bringgs", 90, 50, 75, 50, "Bionic Power Slam")
#asignaccion de siguiente
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo6
nodo6.siguiente = nodo7
nodo7.siguiente = nodo8
nodo8.siguiente = nodo9
nodo9.siguiente = nodo10
nodo10.siguiente = nodo11
nodo11.siguiente = nodo12
nodo12.siguiente = nodo13
nodo13.siguiente = nodo14
nodo14.siguiente = nodo15
nodo15.siguiente = nodo16
nodo16.siguiente = nodo17
nodo17.siguiente = nodo18
nodo18.siguiente = nodo19
nodo19.siguiente = nodo20
nodo20.siguiente = nodo21
nodo21.siguiente = nodo22
nodo22.siguiente = nodo23
nodo23.siguiente = nodo24
nodo24.siguiente = nodo25
nodo25.siguiente = nodo26
nodo26.siguiente = nodo27
nodo27.siguiente = nodo28
nodo28.siguiente = nodo29
nodo29.siguiente = nodo30
#mostrar(nodo3)

#Obten al personaje con mayor y menor valoración de velocidad, imprime solo el personaje con los valores correspondientes.
def mav(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.velocidad>m.velocidad:
            return mav(nodo_a.siguiente,nodo_a)
        else:
            return mav(nodo_a.siguiente,m)
def mev(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.velocidad<m.velocidad:
            return mev(nodo_a.siguiente,nodo_a)
        else:
            return mev(nodo_a.siguiente,m)
print("el personaje mas rapido es:")
mostrar(mav(nodo1,nodo1))
print("el personaje mas lento es:")
mostrar(mev(nodo1,nodo1))

#Obten al personaje con mayor y menor valoración de fuerza. 
def maf(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.fuerza>m.fuerza:
            return maf(nodo_a.siguiente,nodo_a)
        else:
            return maf(nodo_a.siguiente,m)
def mef(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.fuerza<m.fuerza:
            return mef(nodo_a.siguiente,nodo_a)
        else:
            return mef(nodo_a.siguiente,m)
print("el personaje mas fuerte es")
mostrar(maf(nodo1,nodo1))
print("el personaje mas debil es")
mostrar(mef(nodo1,nodo1))

#Obten al personaje con mayor y menor valoración de agilidad.  
def maA(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.agilidad>m.agilidad:
            return maA(nodo_a.siguiente,nodo_a)
        else:
            return maA(nodo_a.siguiente,m)
def meA(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.agilidad<m.agilidad:
            return meA(nodo_a.siguiente,nodo_a)
        else:
            return meA(nodo_a.siguiente,m)
print("el personaje mas agil  es")
mostrar(maA(nodo1,nodo1))
print("el personaje menos agil es")
mostrar(meA(nodo1,nodo1))

#Obten al personaje con mayor y menor valoración de resistencia.
def maR(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.resistencia>m.resistencia:
            return maR(nodo_a.siguiente,nodo_a)
        else:
            return maR(nodo_a.siguiente,m)
def meR(nodo_a,m):

    if nodo_a.siguiente == None:
        return m
    else:
        if nodo_a.resistencia<m.resistencia:
            return meR(nodo_a.siguiente,nodo_a)
        else:
            return meR(nodo_a.siguiente,m)
print("el personaje mas resistente es")
mostrar(maR(nodo1,nodo1))
print("el personaje menos resitente es")
mostrar(meR(nodo1,nodo1))

#Imprime la lista de ordenada ascendente de poderes especiales mostrando el poder y personaje.
def imprimir_poder(nodo):
    if nodo.siguiente == None:
        print("nombre: ",nodo.nombre)
        print("Poder: ",nodo.poder)
        print("-------------------------------")
        return print("fin de la lista")
    else:
        print("nombre: ",nodo.nombre)
        print("Poder: ",nodo.poder)
        print("-------------------------------")
        return imprimir_poder(nodo.siguiente)
imprimir_poder(nodo1)
    
#Imprime el nodo de tu personaje favorito.
mostrar(nodo4)

#Imprime la lista completa enlazada.
def imprimir_todo(nodo):
    if nodo.siguiente == None:
        return print(mostrar(nodo),"\nfin de la lista")
    else:
        mostrar(nodo)
        return imprimir_todo(nodo.siguiente)
    
imprimir_todo(nodo1)