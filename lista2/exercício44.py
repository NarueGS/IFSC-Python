"""
44. Em uma eleição presidencial existem quatro candidatos. Os votos são  informados por meio de código. Os códigos utilizados são: o 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc) o 5 - Voto Nulo 
o 6 - Voto em Branco 
Faça um programa que calcule e mostre: 
o O total de votos para cada candidato;
o O total de votos nulos; 
o O total de votos em branco; 
o A percentagem de votos nulos sobre o total de votos; o A percentagem de votos em branco sobre o total de votos. Para  finalizar o conjunto de votos tem-se o valor zero.
"""
A = 0.0
B = 0.0
C = 0.0
D = 0.0
nulo = 0.0
branco = 0.0
total = 0.0
percentualNulo = 0.0
while 1:
    print("Digite em que candidato deseja votar\n 1 - Jose \n 2 - João \n 3 - Carlos \n 4 - Josué \n 5 - Nulo \n 6 - Branco \n 0 - Para sair da aba de votação")
    voto = int(input())
    if voto == 0:
        break
    elif voto == 1:
        A += 1.0
    elif voto == 2:
        B += 1.0
    elif voto == 3:
        C += 1.0
    elif voto == 4:
        D += 1.0
    elif voto == 5:
        nulo += 1.0
    elif voto == 6:
        branco += 1.0

print("O total de votos que José recebeu foi:  ",A)
print("O total de votos que João recebeu foi:  ",B)
print("O total de votos que Carlos recebeu foi:  ",C)
print("O total de votos que Josué recebeu foi:  ",D)
print("O total de votos nulo foi: ",nulo)
print("O total de votos em branco foi: ",branco)
total = A+B+C+D+nulo+branco
percentualNulo = (nulo*100.0)/total
print("A porcentagem de votos nulos foi {:.1f}%".format(percentualNulo))
if branco != 0:
    percentualBranco = (branco*100/total)
else:
    percentualBranco = 0.0
print("A porcentagem de votos brancos foi: {:.1f}%".format(percentualBranco))