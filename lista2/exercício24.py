"""
24. Faça um programa que calcule o mostre a média aritmética de N  notas. 
"""
result = 0
num = int(input("Digite quantas notas deseja adicionar:  "))
array = [0 for _ in range(num)]
for cont in range(num):
    nota = int(input("Digite a {}° nota:  ".format(cont)))
    array[cont] = nota
for cont in range(num):
    result += array[cont]
print("A média aritmética é: {:.2f}".format((result/num)))