#Crea un diccionario llamado juegos_zelda_cronologicos con los siguientes datos, 
# donde cada clave es la posición cronológica del juego y el valor es el nombre del juego.
juegos_zelda_cronologicos ={
    1: 'The Legend of Zelda: Skyward Sword',
 2: 'The Legend of Zelda: The Minish Cap',
 3: 'The Legend of Zelda: Four Swords',
 4: 'The Legend of Zelda: Ocarina of Time',
 5: 'The Legend of Zelda: Majora\'s Mask',
 6: 'The Legend of Zelda: Twilight Princess',
 7: 'The Legend of Zelda: Link\'s Awakening',
 8: 'The Legend of Zelda: Oracle of Ages',
 9: 'The Legend of Zelda: Oracle of Seasons',
 10: 'The Legend of Zelda: A Link to the Past',
11: 'The Legend of Zelda: A Link Between Worlds',
12: 'The Legend of Zelda: Tri Force Heroes',
13: 'The Legend of Zelda: The Wind Waker',
14: 'The Legend of Zelda: Phantom Hourglass',
15: 'The Legend of Zelda: Spirit Tracks',
16: 'The Legend of Zelda: Breath of the Wild'
}
#Cambia el valor de los datos en las posiciones 3, 7, 11 y 16 por el nombre de su posición.
# Por ejemplo, el valor en la posición 3 debe cambiarse a ‘Posición 3’.
juegos_zelda_cronologicos[3]="pocicion 3"
juegos_zelda_cronologicos[7]="pocicion 7"
juegos_zelda_cronologicos[11]="pocicion 11"
juegos_zelda_cronologicos[16]="pocicion 16"
print(juegos_zelda_cronologicos)
print()
#Ejecuta el código para devolver la lista con las claves (keys) y los valores (values) en listas separadas.
key=juegos_zelda_cronologicos.keys()
val=juegos_zelda_cronologicos.values()
#Ejecuta el código para devolver una tupla con los pares de datos (claves y valores).
tupac=(juegos_zelda_cronologicos.copy())
#print(tupac)
#Elimina las últimas posiciones para que el diccionario quede en un top 5 según tu criterio. Si no has jugado a los juegos, simplemente haz un top 5.
top={juegos_zelda_cronologicos.get(12),
     juegos_zelda_cronologicos.get(13),
     juegos_zelda_cronologicos.get(14),
     juegos_zelda_cronologicos.get(15),
     juegos_zelda_cronologicos.get(16),
     }

#Imprime el diccionario con todos los datos establecidos, luego la lista de las claves, la lista de los valores, la tupla y al final el resultado de las eliminaciones.
print("\n",key)
print("\n",val)
print("\n",tupac)
print("\n",top)