"""
28. Faça um programa que calcule o valor total investido por um  colecionador em sua coleção de CDs e o valor médio gasto em cada um  deles. 
O usuário deverá informar a quantidade de CDs e o valor para em  cada um. 
"""
valor = 0
quantidade = int(input("Quantos CD's você tem?  "))
for x in range(quantidade):
    preco = float(input("Quanto custou o {}° CD?  ".format(x+1)))
    valor += preco
print("Você tem em média {:.2f}R$ por CD".format(valor/quantidade))
