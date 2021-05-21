"""
40. Foi feita uma estatística em cinco cidades brasileiras para coletar  dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
. Código da cidade; 
a. Número de veículos de passeio (em 1999); 
b. Número de acidentes de trânsito com vítimas (em  1999). Deseja-se saber: 
c. Qual o maior e menor índice de acidentes de transito e a que  cidade pertence; 
d. Qual a média de veículos nas cinco cidades juntas; 
e. Qual a média de acidentes de trânsito nas cidades com menos  de 2.000 veículos de passeio. 
"""
A = [0,0]
B = [0,0]
C = [0,0]
D = [0,0]
E = [0,0]
acidentes = [0 for _ in range(5)]
veiculos = [0 for _ in range(5)]
A[0] = int(input("Digite quantos veículos de passeio tinha na cidade A em 1999  "))
B[0] = int(input("Digite quantos veículos de passeio tinha na cidade B em 1999  "))
C[0] = int(input("Digite quantos veículos de passeio tinha na cidade C em 1999  "))
D[0] = int(input("Digite quantos veículos de passeio tinha na cidade D em 1999  "))
E[0] = int(input("Digite quantos veículos de passeio tinha na cidade E em 1999  "))
A[1] = int(input("Digite quantos acidentes de trânsito com vitimas ocorreram na cidade A em 1999  "))
B[1] = int(input("Digite quantos acidentes de trânsito com vitimas ocorreram na cidade B em 1999  "))
C[1] = int(input("Digite quantos acidentes de trânsito com vitimas ocorreram na cidade C em 1999  "))
D[1] = int(input("Digite quantos acidentes de trânsito com vitimas ocorreram na cidade D em 1999  "))
E[1] = int(input("Digite quantos acidentes de trânsito com vitimas ocorreram na cidade E em 1999  "))
acidentes = [A[1],B[1],C[1],D[1],E[1]]
acidentes.sort()
veiculos = [A[0],B[0],C[0],D[0],E[0]]
veiculos.sort()
print(acidentes)
print(veiculos)
print()
if A[0] == acidentes[4]:
    print("A cidade A é a que teve mais acidentes com {} acidentes".format(acidentes[4]))
elif B[0] == acidentes[4]:
    print("A cidade B é a que teve mais acidentes com {} acidentes".format(acidentes[4]))
elif C[0] == acidentes[4]:
    print("A cidade C é a que teve mais acidentes com {} acidentes".format(acidentes[4]))
elif D[0] == acidentes[4]:
    print("A cidade D é a que teve mais acidentes com {} acidentes".format(acidentes[4]))
elif E[0] == acidentes[4]:
    print("A cidade E é a que teve mais acidentes com {} acidentes".format(acidentes[4]))

if A[0] == acidentes[0]:
    print("A cidade A é a que teve menos acidentes com {} acidentes".format(acidentes[0]))
elif B[0] == acidentes[0]:
    print("A cidade B é a que teve menos acidentes com {} acidentes".format(acidentes[0]))
elif C[0] == acidentes[0]:
    print("A cidade C é a que teve menos acidentes com {} acidentes".format(acidentes[0]))
elif D[0] == acidentes[0]:
    print("A cidade D é a que teve menos acidentes com {} acidentes".format(acidentes[0]))
elif E[0] == acidentes[0]:
    print("A cidade E é a que teve menos acidentes com {} acidentes".format(acidentes[0]))


if A[1] == veiculos[4]:
    print("A cidade A é a que teve mais veiculos em 1997 com {} veiculos".format(veiculos[4]))
elif B[1] == veiculos[4]:
    print("A cidade B é a que teve mais veiculos em 1997 com {} veiculos".format(veiculos[4]))
elif C[1] == veiculos[4]:
    print("A cidade C é a que teve mais veiculos em 1997 com {} veiculos".format(veiculos[4]))
elif D[1] == veiculos[4]:
    print("A cidade D é a que teve mais veiculos em 1997 com {} veiculos".format(veiculos[4]))
elif E[1] == veiculos[4]:
    print("A cidade E é a que teve mais veiculos em 1997 com {} veiculos".format(veiculos[4]))

if A[1] == veiculos[0]:
    print("A cidade A é a que teve menos veiculos em 1997 com {} veiculos".format(veiculos[0]))
elif B[1] == veiculos[0]:
    print("A cidade B é a que teve menos veiculos em 1997 com {} veiculos".format(veiculos[0]))
elif C[1] == veiculos[0]:
    print("A cidade C é a que teve menos veiculos em 1997 com {} veiculos".format(veiculos[0]))
elif D[1] == veiculos[0]:
    print("A cidade D é a que teve menos veiculos em 1997 com {} veiculos".format(veiculos[0]))
elif E[1] == veiculos[0]:
    print("A cidade E é a que teve menos veiculos em 1997 com {} veiculos".format(veiculos[0]))

mediaAcidentes = 0
mediaVeiculos = 0
for x in range(5):
    mediaAcidentes += acidentes[x]
for x in range(5):
    mediaVeiculos += veiculos[x]
print("A média de veículos nas cinco cidades juntas é:  {}".format(int(mediaAcidentes/5)))
print("A média de acidentes nas cinco cidades juntas é:  {}".format(int(mediaAcidentes/5)))

