"""
75. Faça um programa que mostre os n termos da Série a seguir: o S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.  Imprima no final a soma da série. 
"""
soma = 0.0
aux = 0.0
n = int(input("Quantas vezes deseja continuar a série?"))
for x in range(0,n,1):
    aux = (1+x)/(1+(x*2))
    soma += aux
    print((1+x),"/",(1+x*2))
print("A soma é: {:.2f}".format(soma))

