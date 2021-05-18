import math


l = int(input("Digite quantos lados tem seu polígono: "))
lado = int(input("Digite o valor em cm que tem cada lado do seu polígono: "))
if l == 3:
    print("Triangulo com area = {}".format(l*3))
elif l ==4:
    print("Quadrado com area = {}".format(l*l))
elif l == 5:
    temp = ((3*l**2) * math.sqrt(3)) / 2
    print("Pentagono com area = {}".format(temp)))
else:
    print("Valor invalido de poligono")
