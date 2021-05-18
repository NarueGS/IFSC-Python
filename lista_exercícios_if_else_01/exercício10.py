
lista = [[0,0] for _ in range(3)]

for cont in range(3):
    x = int(input("Digite o primero valor da linha número {} do seu triangulo\n".format(cont+1)))
    y = int(input("Digite o segundo valor da linha número {} do seu triangulo\n".format(cont+1)))
    array = [x,y]
    lista[cont] = array
if lista[0] == lista[1] == lista[2]:
    print("O triangulo é equilátero")
elif lista[0] != lista[1] != lista[2] and lista[0] != lista[2]:
    print("O triangulo é Escaleno")
else:
    print("O triangulo é isósceles")