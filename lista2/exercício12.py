"""
12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de  
qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero  ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: o Tabuada de 5: 
o 5 X 1 = 5 
o 5 X 2 = 10 
o ... 
o 5 X 10 = 50
"""
while 1:
    num = int(input("Digite o número que quer ver a tabuada:  "))
    if num > 0 and num <11:
        break
for x in range(1,11,1):
    print(num*x)
