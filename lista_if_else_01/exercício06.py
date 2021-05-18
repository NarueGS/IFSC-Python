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
            print("Com esses valores é possível criar um triangulo")
            quit()
print("Não é possível criar um triangulo com esses valores")