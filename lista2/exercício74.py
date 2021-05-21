"""
74. Faça um programa que peça um numero inteiro positivo e em seguida  mostre este numero invertido. 
o Exemplo: 
o 12376489 
 => 98467321 
"""
while 1:
    num = int(input("Digite um número inteiro positivo  "))
    if num > 0:
        break
strNum = str(num)
result = []
result [:] = strNum
result = result[::-1]
resultado = []
for x in range(len(result)):
    resultado.append(int(result[x]))
for x in range(len(resultado)):
    print(resultado[x], end = '')