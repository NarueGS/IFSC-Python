"""
2. CHUTE O NÚMERO 
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor, e pergunta  repetidamente para o usuário chutar o valor gerado até que ele acerte. 
Habilidades praticas a aplicar: 
o Random 
o Comparadores matemáticos 
o Controle de Fluxo 
o Entrada de dados 
o Saida de dados 

"""
import random

print("Gerador de valores aleatórios")
while (1):
    valor = random.randint(10,540)
    while(1):
        chute = int(input("Digite um valor aleatório"))
        if chute == valor:
                continuar = input("Você acertou, deseja continuar? Y para sim e N para não  ")
                verificador = continuar.upper()
                if verificador[0] == 'N':
                    quit()
                elif verificador[0] == 'Y':
                    break
                else:
                    continuar = input("Você acertou, deseja continuar? Y para sim e N para não  \n \n")
        else:
            continuar = input("Você errou, deseja continuar? Y para sim e N para não  ")
            verificador = continuar.upper()
            if verificador[0] == 'N':
                quit()
            elif verificador[0] == 'Y':
                continue
            else:
                continuar = input("Você errou, deseja continuar? Y para sim e N para não  \n \n")