"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N  um número inteiro fornecido pelo usuário.
 O programa deverá mostrar  também o número de divisões que ele executou para encontrar os números  primos. Serão avaliados o funcionamento,
  o estilo e o número de testes  (divisões) executados. 
"""
total = int(input("Digite um número inteiro:  "))
divisoes = 0
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
        divisoes += 1
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
print("O número de divisôes foi: ",divisoes)
