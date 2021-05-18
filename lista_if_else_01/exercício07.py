a = int(input("Digte o valor da primeira reta: "))
b = int(input("Digte o valor da segunda reta: "))
c = int(input("Digte o valor da terceira reta: "))

temp = b-c
if temp < 0:
    temp = temp * -1
if temp < a < (b+c):
    temp = a - c
    if temp < 0:
        temp = temp*-1
    if temp < b < (a+c):
        temp = a - b
        if temp<0:
            temp = temp*-1
        if temp < c < a+b:
            if a = b = c:
                print("é um triangulo equilatero")
            elif a != b != c and a != c:
                print("É um triangulo escaleno")
            else:
                print("É um triangulo isóceles")
            quit()
print("Não é possível criar um triangulo com esses valores")