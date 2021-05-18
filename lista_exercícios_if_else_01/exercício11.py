ang1 = int(input("Digite o primeiro angulo do triangulo: "))
ang2 = int(input("Digite o segundo angulo do triangulo: "))
ang3 = int(input("Digite o terceiro angulo do triangulo: "))
if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print("Triangulo Retangulo")
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print("Triangulo Obstusangulo")
else:
    print("Triangulo actuangulo")
