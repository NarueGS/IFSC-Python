import math
r = float(input("Digite o raio do cilindro em metros: "))
h = float(input("Digite a altura do cilindro em metros: "))

v = math.pi * (r**2) * h
print("O volume em m3 é: {:.1f}".format(v))