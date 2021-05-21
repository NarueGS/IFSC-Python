"""
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma  mensagem caso o valor seja inválido e continue pedindo até que o usuário  informe um valor válido.
"""
nota = int(input("Digite um valor de 0 a 10: "))
while (1):
    if nota >= 0 and nota < 11:
        print("Nota valida, obrigado por usar o programa")
        break
    else:
        nota = int(input("Digite um valor de 0 a 10: "))
print("Nota {} é uma nota valida, obrigado por usar o programa".format(nota))