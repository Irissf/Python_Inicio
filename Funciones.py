#Función
def nombreFuncion():
    print("Esto es una función")
    print("con sus instrucciones")
    
#la llamamos
print("la llamamos")
nombreFuncion()

#funciones con pasos de parámetros
def suma(num1,num2):
    print(num1+num2)

print(suma(3,5))

#funciones con retorno de datos
def sumaRes(num1,num2):
    resultado = num1+num2
    return resultado

print(sumaRes(8,8))