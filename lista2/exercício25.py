"""
25. Faça um programa que peça para n pessoas a sua idade, ao final o  programa devera verificar se a média de idade da turma varia entre 0 e 25,26  e 60 e maior que 60;
 e então, dizer se a turma é jovem, adulta ou idosa,  conforme a média calculada. 
"""
result = 0
n = int(input("Digite quantas pessoas tem na sua turma:  "))
array = [0 for _ in range (n)]
for cont in range(n):
    array[cont] = int(input("Digte a idade do {}° aluno  ".format(cont+1)))
    result += array[cont]
result = result/n
result = round(result)
if result >59:
    print("Sua turma é uma turma idosa")
elif result >25:
    print("Sua turma é adulta")
else:
    print("Sua turma é jovem")

