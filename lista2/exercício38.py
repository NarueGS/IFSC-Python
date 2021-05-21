"""
38. Um funcionário de uma empresa recebe aumento salarial anualmente:  Sabe-se que: 
. Esse funcionário foi contratado em 1995, com salário inicial de  R$ 1.000,00; 
a. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; b. A partir de 1997 (inclusive), os aumentos salariais sempre  correspondem ao dobro do percentual do ano anterior.
 Faça um  programa que determine o salário atual desse funcionário. 
 Após  concluir isto, altere o programa permitindo que o usuário digite o  salário inicial do funcionário. 
"""
inicial = float(input("Digite o salario inicial: "))
inical = inicial*1.015
percentual = 0.015
for ano in range(1,25,1): # 25 porque 21 +3 é 24 e ele precisa executar 24 vezes
    percentual =percentual * 2
    print(percentual)
    inicial = inicial*(1+(percentual))
print(inicial)
"""
professor a conta esta certa mas os valores são exorbitantes porque é 1.5% ou 0.015 * 2^24 porque são 24 anos e a cada ano multiplico por 2,
 isso da um valor muito muito muito alto, mas acreidto estar correto 
"""