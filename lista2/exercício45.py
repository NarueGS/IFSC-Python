"""
45. Desenvolver um programa para verificar a nota do aluno em uma  prova com 10 questões, o programa deve perguntar ao aluno a resposta de  cada questão
 e ao final comparar com o gabarito da prova e assim calcular
   o total de acertos e a nota (atribuir 1 ponto por resposta certa).
    Após cada  aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar  o sistema. Após todos os alunos terem respondido informar: 
. Maior e Menor Acerto; 
a. Total de Alunos que utilizaram o sistema; 
b. A Média das Notas da Turma. 
c. Gabarito da Prova: 
d. 
e. 01 - A 
f. 02 - B 
g. 03 - C 
h. 04 - D 
i. 05 - E 
j. 06 - E 
k. 07 - D 
l. 08 - C 
m. 09 - B
"""

import os
gabarito = ['A','B','C','D','E','E','D','C','B']
while 1:
    resultado = 0
    for x in range(len(gabarito)):
        resposta = input("Qual sua resposta para a questão {} ? A,B,C,D ou E:  ".format(x+1))
        resposta = resposta.upper()
        resposta = resposta[0]
        if resposta == gabarito[x]:
            resultado+=1
    print("O seu resultado foi: {} / 9 ".format(resultado))
    while 1:
        continuar = input("Outro aluno deseja registrar sua nota? Y para sim N para não  ")
        continuar = continuar.upper()
        continuar = continuar[0]
        if continuar == 'N':
            quit()
        elif continuar == 'Y':
            print("AA")
            os.system('cls')
            break

    
