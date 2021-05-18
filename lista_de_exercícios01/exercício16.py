x = int(input("Digite o primero valor inteiro: "))
y = int(input("Digite o segundo valor inteiro: "))

temp = x
x = y
y = temp
print("Primeiro valor permutado: {} e o segundo: {}".format(x,y))