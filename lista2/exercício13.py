"""
13. Faça um programa que peça dois números, base e expoente, calcule  e mostre o primeiro número elevado ao segundo número. Não utilize a função  de potência da linguagem. 
"""
Valor = 0
base = int(input("Digte o valor da base:  "))
expoente = int(input("Digite o valor do expoente:  "))
Valor = base
for x in range(1,expoente,1):
    Valor = Valor*base
print(Valor)