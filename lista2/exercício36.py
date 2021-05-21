"""
36. Desenvolva um programa que faça a tabuada de um número qualquer  inteiro que será digitado pelo usuário, mas a tabuada não deve  necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem  ser informados também pelo usuário, conforme exemplo abaixo: 
o Montar a tabuada de: 5 
o Começar por: 4 
o Terminar em: 7 
o 
o Vou montar a tabuada de 5 começando em 4 e terminando em  7: 
o 5 X 4 = 20 
o 5 X 5 = 25 
o 5 X 6 = 30 
o 5 X 7 = 35 
Obs: Você deve verificar se o usuário não digitou o final menor que o  inicial. 
"""
num = int(input("Digite o número que quer ver a tabuada:  "))
while 1:
    inicio = int(input("Digite o primeiro multiplicador: "))
    final = int(input("Digite o ultimo multiplicador"))
    if inicio <= final:
        break
for x in range(inicio,final,1):
    print(num*x)
