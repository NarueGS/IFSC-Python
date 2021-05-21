"""
27. Faça um programa que calcule o número médio de alunos por turma.  Para isto, peça a quantidade de turmas e a quantidade de alunos para cada  turma.
 As turmas não podem ter mais de 40 alunos.
"""
quantidade = 0
turmas = int(input("Quantas turmas você tem?  "))
for x in range(turmas):
    alunos = int(input("Quantos alunos a {}° turma tem?  ".format(x+1)))
    quantidade += alunos
print("Você tem em média {} alunos".format(int(quantidade/turmas)))