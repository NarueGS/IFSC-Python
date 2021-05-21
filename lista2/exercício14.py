"""
14. Faça um programa que peça 10 números inteiros, calcule e mostre a  quantidade de números pares e a quantidade de números ímpares. 
"""
impar = 0
par = 0
array = [0 for _ in range(10)]
for x in range(10):
    array[x] = int(input("Digite um valor"))
for x in range(10):
    if array[x] % 2 != 0:
        impar+= 1
    else:
        par+= 1
print("Números impares: ",impar)
print("Números pares: ",par)
