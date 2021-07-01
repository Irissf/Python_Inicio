def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    #si pone dividir entre 0 salta error
    try:
	    return num1/num2
    except ZeroDivisionError:
        return "No se puede dividir entre 0"		
	
#ya se puede ver que si nos ponen letras, nos salta una excepcion
#así que toca controlarla con try-except-finally

valido = False
while(valido == False):
    try:
        num1=(int(input("Introduce el primer número: ")))
        num2=(int(input("Introduce el segundo número: ")))
        valido = True		
    #podemos concatenar excepciones como en otro lenguajes	
    except ValueError:
        print("Dato incorrecto")
    finally:
        #Lo que va aqui se ejecuta siempre, salte o no una excepción
        #si no ponemos except, el programa no captura la excepcion
        #pero si salta el finally
        print("Paso por aqui")

#Otra opcion
#while True:
    #instrucciones
    #break

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(num1,num2))
elif operacion=="resta":
	print(resta(num1,num2))
elif operacion=="multiplica":
	print(multiplica(num1,num2))
elif operacion=="divide":
	print(divide(num1,num2))
else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")