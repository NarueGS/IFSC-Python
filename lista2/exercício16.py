"""
16. A série de Fibonacci é formada pela sequência  0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o  valor seja maior que 500. 

"""
a = 1
b = 0
aux = 0
while 1:
    aux = a
    a = a+b
    b = aux
    if b <= 500:
     print(b)
    else:
        quit()