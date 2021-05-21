"""
19. Altere o programa anterior para que ele aceite apenas números entre  0 e 1000. 
"""
resultado = 0
while 1:
    N = int(input("Quantos números deseja verificar?  de 1 a 1000  "))
    if N >0 and N<1001:
        break
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