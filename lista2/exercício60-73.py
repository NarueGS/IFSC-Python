"""
60. Em uma competição de ginástica, cada atleta recebe votos de sete  jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média  dos votos restantes. 
Você deve fazer um programa que receba o nome do  ginasta e as notas dos sete jurados alcançadas pelo atleta em sua  apresentação e depois informe a sua média,
 conforme a descrição acima  informada (retirar o melhor e o pior salto e depois calcular a média com as  notas restantes). As notas não são informados ordenadas.
  Um exemplo de  saída do programa deve ser conforme o exemplo abaixo: 
61. Atleta: Aparecido Parente 
62. Nota: 9.9 
63. Nota: 7.5 
64. Nota: 9.5 
65. Nota: 8.5 
66. Nota: 9.0 
67. Nota: 8.5 
68. Nota: 9.7 
69. 
70. Resultado final: 
71. Atleta: Aparecido Parente 
72. Melhor nota: 9.9 
73. Pior nota: 7.5 
"""
import os
medias = []
atletas = []
while 1:
    atleta = input("Digite o nome do atleta  ")
    if atleta == "":
        os.system('cls')
        break
    saltos = [0,0,0,0,0,0,0]
    media = 0.0
    saltos[0] = float(input("Digite a nota que o 1° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[1] = float(input("Digite a nota que o 2° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[2] = float(input("Digite a nota que o 3° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[3] = float(input("Digite a nota que o 4° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[4] = float(input("Digite a nota que o 5° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[5] = float(input("Digite a nota que o 6° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos[6] = float(input("Digite a nota que o 7° jurado deu ao atleta: {}   ".format(atleta))) 
    saltos.sort()
    print("A pior nota foi {:.2f} ".format(saltos[0]))
    print("A melhor nota foi {:.2f} ".format(saltos[4]))
    media = (saltos[1] + saltos[2] + saltos[3] + saltos[4] + saltos[5]) / 5
    print("Média dos demais saltos: {:.2f} metros".format(media))
    atletas.append(atleta)
    medias.append(media)
position = 0
melhormedia = 0
for x in range(len(medias)):
    if medias[x] > melhormedia:
        melhormedia = medias[x]
        position = x
print("##############################\n")
print("Resultado Final: ",atletas[position]," com uma média de {} ".format(medias[position]))
