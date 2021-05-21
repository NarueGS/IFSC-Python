"""
26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o  número de votos de cada candidato.
"""
A = 0
B = 0
C = 0
eleitores = int(input("Digite quantos eleitores tem na votação  "))

for cont in range(eleitores):
    while 1:
        voto = input("Digite em qual candidato deseja votar: A, B ou C  ")
        voto = voto.upper()
        voto = voto[0]
        if voto == 'A' or voto == 'B' or voto == 'C':
            break
    if voto == 'A':
        A += 1
    elif voto == 'B':
        B += 1
    elif voto == 'C':
        C+= 1
print("Votos do candidato A: ",A)
print("Votos do candidato B: ",B)
print("Votos do candidato C: ",C)
