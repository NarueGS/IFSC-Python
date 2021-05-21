"""
33. O Departamento Estadual de Meteorologia lhe contratou para  desenvolver um programa que leia as um conjunto indeterminado de  temperaturas,
 e informe ao final a menor e a maior temperaturas informadas,  bem como a média das temperaturas. 
"""
quant = int(input("Digite quantas temperaturas deseja checar  "))
min = 0
max = 0
media = 0
array = [0 for _ in range(quant)]

for x in range(quant):
    array[x] = float(input("Digite a temperatura do {}° termometro: ".format(x+1)))
    media += array[x]
array.sort()
min = array[0]
max = array[quant-1]

print("A média é: {:.2f}".format(media/quant))
print("O minimo é: ",min)
print("O máximo é: ",max)