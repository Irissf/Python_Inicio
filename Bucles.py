for i in [1,2,3]:
    print("Hola")
    #Esto ejecutará 3 veces hola

for i in ["Primavera","Otoño","Invierno","Verano"]:
    print(i)
    #Esto ejecutaría 4 veces, asignando a i el valor de la lista correspondiente

for i in ["Iris", "es", "guay"]:
    print(i,end=(" "))
    #Con end determinamos lo que hay entre print y print, quitamos el salto de linea

print()

for i in "cadena":
    print (i,end=("-"));
    #El resultado es: c-a-d-e-n-a-
    
print()

for i in range(5):
    print (i,end=(" ")) 
    #El resultado es: 0 1 2 3 4

for i in range(5,9):
    print (f"Valor de la variables es {i}") 
    #f de format antes de las comillas
    #i tomará los valores de 5,6,7,8

for i in range(0,10,2):
    print(i,end=(" "))
    #resultado = 0 2 4 6 8
    #El último dato de range determinacada cuantos numeros recorre, 
    #En este caso de 2 en 2, pero puede ser de 3 en 3 etc
