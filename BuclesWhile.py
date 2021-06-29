i = 1
while i <= 10:
    print(i)
    i=i+1

# ejemplito
edad = int(input("introduce edad"))

while edad < 0 or edad > 150:
    print("edad incorrecta")
    edad = int(input("introduce edad"))

print("edad:"+str(edad))

#Continue
nombre = "Iris la nigromante"
contador = 0

for i in nombre:
    if i == " ":
        #si no es un espacio, que no lo cuente
        continue
    contador +=1
print(contador)