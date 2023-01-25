numUsuario = int(input("Introduzca un num: "))
num = 1
print("Los numeros divisores son: ")
while(numUsuario>=num):
    if (numUsuario % num == 0):
        print(num)
    num+=1