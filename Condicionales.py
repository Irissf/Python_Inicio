print("Introduce la nota del alumno")

#Entrada de teclado,
#cualquier dato que metas lo cogerá como un string
notaAlumno = input()

def condicionalIf(nota):
    #sintaxis básica de un if-else
    if(nota < 5):
        valoracion = "No aprobado"
    else:
        valoracion = "Aprobado"
    return valoracion


# con int, lo transformamos en int siempre que sea posible
print(condicionalIf(int(notaAlumno)))

