"""
7. Faça um programa que leia 5 números e informe o maior número. 
"""
array = [0,0,0,0,0]
array[0] = int(input("Digite o 1° valor: "))
array[1] = int(input("Digite o 2° valor: "))
array[2] = int(input("Digite o 3° valor: "))
array[3] = int(input("Digite o 4° valor: "))
array[4] = int(input("Digite o 5° valor: "))
array.sort()
print(array[4])