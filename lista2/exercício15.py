"""
15. A série de Fibonacci é formada pela sequência  1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o  n−ésimo termo. 
"""
a = 1
b = 0
aux = 0
n = int(input("Digte quantas vezes quer fazer o fibonnaci: "))
for x in range(n):
    aux = a
    a = a+b
    b = aux
    print(b)