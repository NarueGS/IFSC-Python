"""
42. Faça um programa que leia uma quantidade indeterminada de  números positivos e conte quantos deles estão nos seguintes intervalos:
 [0- 25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando  for lido um número negativo. 
 """

A = 0
B = 0
C = 0
D = 0

while 1:
    num = int(input("Digite um número positivo   "))
    if num < 0:
        break
    elif num <26:
        A += 1
    elif num<51:
        B += 1
    elif num <76:
        C += 1  
    elif num <101:
        D += 1

print("Há {} números entre 0 e 25".format(A))
print("Há {} números entre 26 e 50".format(B))
print("Há {} números entre 51 e 75".format(C))
print("Há {} números entre 76 e 100".format(D))