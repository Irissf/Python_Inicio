#sintaxis clave-valor, el tipo de dato no importa
miDiccionario = {"España":"Madrid","Alemania":"Berlín","Portugal":"Lisboa"} 

#acceder a un elemento con su clave
print(miDiccionario["España"])

#añadir elemento
miDiccionario["Italia"]="Romass"

#Modificar un dato, sobreescribimos el dato
miDiccionario["Italia"]="Roma"

#Eliminar 
del miDiccionario["Alemania"]

#Imprimir diccionario
print(miDiccionario)

#puede haber tipos de datos diferentes, siempre que la clave no se repita
diccionarioVarios = {3:"cosas","iris":True,44:10.5}
print(diccionarioVarios)

