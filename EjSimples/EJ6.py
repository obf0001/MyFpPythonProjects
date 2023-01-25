num1=int(input("Ponga un numero: "))
hueco=num1-1
estrella=1
#Va a dar num1 de vueltas
for i in range(num1):
    #Metemos un salto de linea
    print('')
    #For para los espacios que da hueco vueltas
    for j in range(hueco):
        #Metemos un espacio y que no meta salto de linea 
        print(" ", end='')
    hueco-=1
    #For para escribir las estrellas
    for g in range(estrella):
        print("*",end='')
    #Le vamos sumando dos para que la fila este ordenada y la primera estrella se quede en medio de la segunda fila
    estrella+=2