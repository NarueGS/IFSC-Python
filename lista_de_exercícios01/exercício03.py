import math

raio = float(input("Digite o raio: "))

diametro = raio ** 2
area = math.pi * diametro
perimetro = math.pi * raio * 2
print("Diametro: {:.2f}".format(diametro))
print("Area: {:.2f}".format(area))
print("Perimetro: {:.2f}".format(perimetro))