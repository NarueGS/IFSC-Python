"""1. SIMULADOR DE DADO 
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e  permitir que o usuário rode o script quantas vezes quiser. 
Habilidades praticas a aplicar: 
o Tratamento de exceções 
o Condicionais If/Else 
o Input de dados 
o Geração de valores 
o Print 
"""
import random

#variaveis auxiliares
IsRunning = True
dado = 0


print("Simulador de DADO \n\n")
while (1):
    tipo = int(input("Se você souber quantas vezes quer executar o código digite 0, se você não sabe ainda digite 1:  "))
    if tipo == 1 or tipo == 0:
        break

if tipo == 0:
    tentativas = int(input("Digite quantas vezes quer tentar adivinhar o valor do dado:  "))
    for cont in range(tentativas):
        chute = int(input("Digite qual valor você achar que deu ao rolar o dado:  "))
        dado = random.randint(1,6)
        if chute == dado:
            print("Você ganhou")
            continuar = input("Você deseja continuar Y para sim e N para não:  ")
            while (1):
                verificador = continuar.upper()
                if verificador[0] == 'N':
                    quit()
                elif verificador[0] == 'Y':
                    break
                else:
                    continuar = input("Você deseja continuar Y para sim e N para não  ")
        print("Tentativas restantes: {}".format(tentativas-cont))

elif tipo == 1:
    while IsRunning:
        chute = int(input("Digite qual valor você acha que deu ao rolar o dado:  "))
        dado = random.randint(1,6)
        if chute == dado:
            while(1):
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
