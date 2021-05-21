"""
8. Faça um programa que leia 5 números e informe a soma e a média  dos números. 
"""
resultado = 0
resultado2 = 0
array = [0,0,0,0,0]
array[0] = int(input("Digite o 1° valor: "))
array[1] = int(input("Digite o 2° valor: "))
array[2] = int(input("Digite o 3° valor: "))
array[3] = int(input("Digite o 4° valor: "))
array[4] = int(input("Digite o 5° valor: "))
for x in range(len(array)):
    resultado += array[x]
print(resultado)
resultado2 = resultado/len(array)
print(resultado2)
