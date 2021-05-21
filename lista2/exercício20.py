"""
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular  o fatorial várias vezes e limitando o fatorial a números inteiros positivos e  menores que 16. 
"""
result = 0
while 1:
    while 1:
        fatorial = int(input("Digite um número que quer saber o fatorial:  "))
        if fatorial > 0 and fatorial < 17:
            break
    for x in range(1,fatorial,1):
        fatorial = fatorial*x
    print(fatorial)