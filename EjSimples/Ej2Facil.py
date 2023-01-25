num = 1
num2 = 1
numUsuario = int(input("Introduzca un num: "))
contador = 0
while(numUsuario>=num2):
    for i in range(num2):
        if (num2 % num == 0):
            contador+=1
        num+=1
    if(contador==2):
        contador=0
        print(num2 , " es primo")
    num2+=1
    num=1