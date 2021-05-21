"""
46. Em uma competição de salto em distância cada atleta tem direito a  cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior  resultados são eliminados. 
O seu resultado fica sendo a média dos três  valores restantes. 
Você deve fazer um programa que receba o nome e as  cinco distâncias alcançadas pelo atleta em seus saltos
 e depois informe a  média dos saltos conforme a descrição acima informada (retirar o melhor e o  pior salto e depois calcular a média).
  Faça uso de uma lista para armazenar  os saltos. Os saltos são informados na ordem da execução, portanto não são  ordenados. 
  O programa deve ser encerrado quando não for informado o  nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: 
47. Atleta: Rodrigo Curvêllo 
48. 
49. Primeiro Salto: 6.5 m 
50. Segundo Salto: 6.1 m 
51. Terceiro Salto: 6.2 m 
52. Quarto Salto: 5.4 m 
53. Quinto Salto: 5.3 m 
54. 
55. Melhor salto: 6.5 m 
56. Pior salto: 5.3 m 
57. Média dos demais saltos: 5.9 m 
58. 
59. Resultado final: 
Rodrigo Curvêllo: 5.9 m
"""
medias = []
atletas = []
while 1:
    atleta = input("Digite o nome do atleta  ")
    if atleta == "":
       break
    saltos = [0,0,0,0,0]
    media = 0.0
    saltos[0] = int(input("Quantos metros o {} pulou no 1° salto?  ".format(atleta))) 
    saltos[1] = int(input("Quantos metros o {} pulou no 2° salto?  ".format(atleta))) 
    saltos[2] = int(input("Quantos metros o {} pulou no 3° salto?  ".format(atleta))) 
    saltos[3] = int(input("Quantos metros o {} pulou no 4° salto?  ".format(atleta))) 
    saltos[4] = int(input("Quantos metros o {} pulou no 5° salto?  ".format(atleta))) 
    saltos.sort()
    print("O pior salto foi {:.2f} metros".format(saltos[0]))
    print("O melhor salto foi {:.2f} metros".format(saltos[4]))
    media = (saltos[1] + saltos[2] + saltos[3]) / 3
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
print("Resultado Final: ",atletas[position]," com uma média de {} metros por pulo".format(medias[position]))





