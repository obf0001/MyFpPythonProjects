#Lo hice de 5 cifras al principio por lo que nlas variables empiezan en 2 XD
num2=1
num3=1
num4=1
num5=1

while (num2 != 6):
    for j in range(5):
        num3=1
        for h in range(5):
            num4=1
            for g in range(5):
                num5=1
                for i in range(5):
                    print(num2,num3,num4,num5)
                    num5+=1
                num4+=1
            num3+=1
        num2+=1
