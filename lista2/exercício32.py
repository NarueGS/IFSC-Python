"""32. Faça um programa que calcule o fatorial de um número inteiro  fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o  exemplo abaixo: 
o Fatorial de: 5 
o 5! = 5 . 4 . 3 . 2 . 1 = 120
"""
result = 0
fatorial = int(input("Digite um número que quer saber o fatorial:  "))
start = fatorial
print (start, end = ' . ')
for x in range(1,fatorial,1):
    fatorial = fatorial*x
    if x+1 == start:
        print(start-x)
    else:
        print((start-x), end= ' . ')