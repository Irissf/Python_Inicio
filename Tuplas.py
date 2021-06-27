#se ejecutan más rápido que las listas
#puede no llevar paréntesis, pero mejor ponerlos
from typing import List


tuplaEjemplo = ("Iris",22,True,'a',"Iris")
print(tuplaEjemplo[:])

#convertir tupla a lista, se puede al revés
miLista = list(tuplaEjemplo)
print(miLista[:])

#de lista a tupla sería -> miTuple = tuple(miLista) <-

#comprobar si hay elementos con in
print("Iris" in tuplaEjemplo)

#contar cuantas veces aparece un elemento
print(tuplaEjemplo.count("Iris"))

#el número de elementos que hay en la tupla
print(len(tuplaEjemplo))

#tupla unitaria, con un solo elemento, debe llevar una coma al final
tuplaUni = ("Iris",)

#podemos asignar los elementos de una tupla a variables "desempaquetado de tuplas"
tuplaVar = ("iris",34,"Acuario")
nombre,edad,horoscopo = tuplaVar
#phyton asigana cada elemento de la tupla a una variable
print(nombre)
