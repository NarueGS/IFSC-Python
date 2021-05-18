money = int(input("Digite o valor que quer receber: "))
temp = 0
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

notas100 = money//100
temp = money%100
notas50 = temp//50
temp = (temp%50)
notas20 = temp//20
temp = temp%20
notas10 = temp//10
temp = temp%10
notas5 = temp//5
temp = temp%5
notas2 = temp//2
temp = temp%2
notas1 = temp

print("notas de 100: {}".format(notas100))
print("notas de 50: {}".format(notas50))
print("notas de 20: {}".format(notas20))
print("notas de 10: {}".format(notas10))
print("notas de 5: {}".format(notas5))
print("notas de 2: {}".format(notas2))
print("notas de 1: {}".format(notas1))