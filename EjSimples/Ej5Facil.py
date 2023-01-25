num1 = int(input("Introduzca el num 1: "))
num2 = int(input("Introduzca el num 2: "))
num3 = int(input("Introduzca el num 3: "))

#Comprobamos si los 3 son iguales
if(num1 == num2 or num1 == num3 or num2 == num3):
    if(num1 == num2 == num3):
        print(num1, ", ",num2," y ",num3," son iguales")
    else:
        #Comprobamos si solo dos numeros son iguales
        if(num1 == num2 ):
            print(num1, " y ",num2," son iguales")
            if (num3 > num1):
                print(num3, " es el mayor")
            else:
                print(num3, " es el menor")
        elif(num1 == num3):
            print(num1, " y ",num3," son iguales")
            if (num2 > num1):
                print(num2, " es el mayor")
            else:
                print(num2, " es el menor")
        else:
            print(num2, " y ",num3," son iguales")
            if (num1 > num2):
                print(num1, " es el mayor")
            else:
                print(num1, " es el menor")
#Si no ocurre nada de lo anterior comprobamos que los 3 son diferentes entre si
if ( num1 != num2 and num1 != num3 and num2 !=num3):
    #Comprobamos cual es el mayor y luego cuales son el menor y el mediano
    if (num1 > num2 and num3):
        print(num1, " es el mayor")
        if(num2 < num3):
            print(num2, " es el menor")
            print(num3, " es el mediano")
        else:
            print(num3, " es el menor")
            print(num2, " es el mediano")
    elif(num2 > num3 and num1):
        print(num2, " es el mayor")
        if(num1 < num3):
            print(num1, " es el menor")
            print(num3, " es el mediano")
        else:
            print(num3, " es el menor")
            print(num1, " es el mediano")
    else:
        print(num3, " es el mayor")
        if(num2 < num1):
            print(num2, " es el menor")
            print(num1, " es el mediano")
        else:
            print(num1, " es el menor")
            print(num2, " es el mediano")


