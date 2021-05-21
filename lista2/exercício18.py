"""
18. Faça um programa que, dado um conjunto de N números, determine  o menor valor, o maior valor e a soma dos valores. 
"""
resultado = 0
N = int(input("Quantos números deseja verificar?  "))
array = [0 for _ in range(N)]
for x in range(N):
    print(("Digite o {}° número").format(x+1))
    array[x] = int(input())
array.sort()
print("O menor número é: ",array[0])
print("O maior número é: ",array[len(array)-1])
for x in range(N):
    resultado += array[x]
print("A soma de todos os números é: ",resultado)    