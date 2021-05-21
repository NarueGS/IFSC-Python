"""
10. Faça um programa que receba dois números inteiros e gere os  números inteiros que estão no intervalo compreendido por eles.

"""
A = [0,0]
A[0] = int(input("Digite o 1 valor:  "))
A[1] = int(input("Digite o segundo valor:  "))
A.sort()
while 1:
    if A[0] != A[1]+1:
        print(A[0])
        A[0] += 1
    else:
        break