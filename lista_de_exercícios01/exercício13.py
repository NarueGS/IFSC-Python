r1 = int(input("Digite o valor do resistor número 1: "))
r2 = int(input("Digite o valor do resistor número 2: "))
r3 = int(input("Digite o valor do resistor número 3: "))

result1 = r1*r2/(r1+r2)
result2 = result1+r3
print("o valor equivalente das resistências é: {}".format(result2))