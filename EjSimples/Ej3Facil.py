num = 1
numUsuario = int(input("Introduzca un num: "))
contador = 0
while(numUsuario>=num):
    if (numUsuario % num == 0):
        contador+=1
    num+=1

if(contador == 2):
    print("Es es primo")
else:
    print("No es primo")