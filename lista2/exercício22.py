"""
22. Altere o programa de cálculo dos números primos, informando, caso  o número não seja primo, por quais número ele é divisível. 
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

