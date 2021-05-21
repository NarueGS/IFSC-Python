"""
11. Altere o programa anterior para mostrar no final a soma dos números. 
"""
result = 0
A = [0,0]
A[0] = int(input("Digite o 1 valor:  "))
A[1] = int(input("Digite o segundo valor:  "))
A.sort()
while 1:
    if A[0] != A[1]+1:
        result += A[0]
        A[0] += 1
    else:
        break
print(result)
