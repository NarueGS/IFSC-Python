"""
39. Faça um programa que leia dez conjuntos de dois valores, o primeiro  representando o número do aluno e o segundo representando a sua altura  em centímetros.
 Encontre o aluno mais alto e o mais baixo. Mostre o número  do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. 
"""
maisalto = 0.0
maisaltonumero = 0.0
maisbaixo = 1000.0
maisbaixonumero = 0.0
for x in range(10):
    numero = int(input("Digite o numero do aluno:  "))
    altura = float(input("Digite a altura do seu aluno: "))
    if altura > maisalto:
        maisalto = altura
        maisaltonumero = numero
    if altura < maisbaixo:
        maisbaixo = altura
        maisbaixonumero = numero
print("O aluno mais alto é o número {} com {} metros".format(maisaltonumero,maisalto))
print("O aluno mais baixo é o número {} com {} metros".format(maisbaixonumero,maisbaixo))