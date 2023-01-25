import math

num1=int(input("Ponga un numero: "))
#Numero de espacios
hueco=num1-1
#Los numeros que va a escribir
numeros=1
#Los numeros que va a haber en cada fila
numeroFila = 1
#El numero que esta a mitad por el que se empieza a restar
divisor=1
'''Booleano para que no reste en la primera vuelta, ya que sino la primera fila seria 12 ya que lo
sumo en la linea 24 y lo vuelve a escribir en la linea 30'''
check = False

for i in range(num1):
    print('')
    numeros= 1
    for j in range(hueco):
        print(" ", end='')
    hueco-=1
    for g in range(divisor):
        print(numeros,end='')
        numeros+=1
    
    numeroFila+=2
    divisor = (int) (math.floor(numeroFila/2))
    if( check==True):
        for f in range(divisor):
            print(numeros,end='')
            numeros-=1
    check = True