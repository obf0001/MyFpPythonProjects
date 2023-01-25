lado1 = input("Dame el primer lado: ")
lado2 = input("Dame el segundo lado: ")
lado3 = input("Dame el tercer lado: ")

if(lado1 == lado2 == lado3):
    print("Triangulo equilatero")
if(lado1 == lado2 != lado3 ):
    print("Es un triangulo isosceles")
if(lado1 != lado2 != lado3 ):
    print("Es un triangulo escaleno")
    