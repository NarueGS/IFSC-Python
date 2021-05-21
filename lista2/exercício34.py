"""
34. Os números primos possuem várias aplicações dentro da  Computação, por exemplo na Criptografia. 
Um número primo é aquele que é  divisível apenas por um e por ele mesmo. Faça um programa que peça um  número inteiro e determine se ele é ou não um número primo. 
"""
num = int(input("Digite um número inteiro:  "))
aux = num//2
aux += 1
while aux > 1:
    if num == 2:
        aux = 1
        break
    elif num%aux == 0 :
        print("O número {} não é primo".format(num))
        break
    else:
        aux-= 1
if aux <= 1:
    print("O número {} é primo".format(num))

