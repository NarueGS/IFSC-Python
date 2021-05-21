"""
17. Faça um programa que calcule o fatorial de um número inteiro  fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

"""
result = 0
fatorial = int(input("Digite um número que quer saber o fatorial:  "))
for x in range(1,fatorial,1):
    fatorial = fatorial*x
print(fatorial)