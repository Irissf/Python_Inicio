print("Asignaturas optativas año 2021")
print("Informática gráfica - Pruebas de software - Usabilidad y accesiblidad")

opcion = input("Escribe la asignatura escogida: ")

#python es Case Sensitive
#podemos solucionarlo con lower() o upper
asignatura = opcion.lower();

if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesiblidad"):
    #si no es un estring lo que se concatena hay que convertirlo
    print("Asignatura elegida " + asignatura)
else:
    print("No existe la asignatura")

