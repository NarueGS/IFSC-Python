"""
35. Encontrar números primos é uma tarefa difícil. Faça um programa que  gera uma lista dos números primos existentes entre 1 e um número inteiro  informado pelo usuário. 
"""
total = int(input("Digite um número inteiro:  "))
cont = 0
num = 2
primo = False
while 1:
    aux = num//2
    aux += 1
    while 1:
        if num == 2:
            primo = True
            break
        if num%aux == 0 :
            primo = False
            break
        aux -= 1
        if aux <= 1:
            primo = True
            break
    if primo == True:
        print(num)
        cont+= 1
        primo = False
        if cont == total:
            break
    num += 1
