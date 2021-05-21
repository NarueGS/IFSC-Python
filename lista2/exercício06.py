"""
6. Faça um programa que imprima na tela os números de 1 a 20, um  abaixo do outro. Depois modifique o programa para que ele mostre os  números um ao lado do outro.
"""
array = [0 for _ in range(21)]

for x in  range(21):
    array[x] = x
    print(x)
print("Um do lado do outro fica assim: ")
print(array)