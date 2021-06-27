#listas
miLista=["iris","aitor","ici","ka","vicki"]
miListaDos = [1,"iris",33.5,True]

#acceder a un elemento de la lista
print(miLista[2])

#podemos recorrerla al revés, siendo la última posición -1
print(miLista[-1])

#Porción de lista, si la lista es muy larga podemos acceder a 
#una seccion: ejemplo los 3 primeros elementos
print(miLista[0:3])
#de la posión 0 a la 3, la 3 es escluyente, el 0 es inclusive

#agregar elemento al final
miLista.append("Maria")

#agregar en una posición
miLista.insert(1,"Carlos")

#agregar varios elementos
miLista.extend(["sofia","ana","mila"])

#me muestra los elementos de la lista
print(miLista[:])
print(miListaDos[:])

#conseguir el indice de un elemento, si hay varios devuelve el primero
print(miLista.index("iris"))

#ver si un elemento está en la lista
print("iris" in miLista)

#eliminar elemtento
miLista.remove("ana")
print(miLista[:])

#eliminar ultimo elemento de la lista
miLista.pop()

#sumar listas diferentes
miListaUnida = miLista + miListaDos
print(miListaUnida[:])

#multiplicar los datos de una lista
milistaRepe=["aaa",111]*5
print(milistaRepe[:])