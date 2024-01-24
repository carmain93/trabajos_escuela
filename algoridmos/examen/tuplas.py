#Crea una tupla con los siguientes valores de videojuegos famosos, pero en orden inverso: ‘Super Mario Bros.’, ‘Tetris’, ‘The Legend of Zelda: Ocarina of Time’, ‘Minecraft’, ‘Grand Theft Auto V’, ‘The Elder Scrolls V: Skyrim’, ‘Fortnite’, ‘Pac-Man’, ‘World of Warcraft’, ‘Pokemon Red/Green/Blue’.

t=("Pokemon Red/Green/Blue","World of Warcraft","Pac-Man","Fortnite","The Elder Scrolls V: Skyrim","Grand Theft Auto V",
   "Minecraft", "The Legend of Zelda: Ocarina of Time","Tetris","Super Mario Bros")

#Ejecuta el código para saber qué elementos están en las posiciones 1, 3, 6 y 10.
print("1.-",t[1]," 3.-",t[3]," 6.-",t[6]," 10.-",t[9] )
#Ejecuta el código para saber si los valores de dichas posiciones se repiten en la misma tupla.
print("los valores anteriores se repiten","1.-",t.count(t[1])," 3.-",t.count(t[3])," 6.-",t.count(t[6])," 10.-",t.count(t[9]) )
#Imprime los resultados de las instrucciones 2 y 3.