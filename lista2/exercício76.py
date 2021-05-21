"""
76. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule  o valor de H com N termos. 
"""
soma = 1
n = int(input("Digite quantos termos tem sua função:  "))
for x in range(2,n+1,1):
    aux = 1/x
    soma += aux
print(soma)

"""
Não entendi se era pra ser N termos ou até chegar em 1/N portanto fiz até chegar em 1/N, porque a série começa com 1/2
"""