n=[1,2,3,4,5,6,7,8,9]
p,s, *otros=n
print(p,s,otros)
#tomar el primero
p, *otros, ultimo=n
print(p,ultimo,otros)
#tomar el primero ultimo y antepenultimo
p,s,*ot,pe,ul=n
print(p,s,pe,ul,*ot)