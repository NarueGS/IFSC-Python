altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kilos: "))
IMC = peso / altura**2
if IMC >= 40:
    print("Obesidade mórbida")
elif IMC < 20:
    print("Abaixo do normal")
else:
    if IMC >= 35 and IMC <=40:
        print("Obseidade moderada")
    elif IMC >= 30 and IMC < 35:
        print("Obesidade leve")
    elif IMC > 25 and IMC < 30:
        print("Sobrepeso")
    elif IMC > 20 and IMC <25:
        print("normal")