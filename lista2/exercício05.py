"""
5. Altere o programa anterior permitindo ao usuário informar as  populações e as taxas de crescimento iniciais. Valide a entrada e permita  repetir a operação. 
"""
anos = 0
A = int(input("Digite quantos habitantes a cidade A possui: "))
B = int(input("Digite quantos habitantes a cidade B possui: "))
while 1:
    A = int(A*1.03)
    B = int(B*1.015)
    anos+= 1
    if A >= B:
        break
print("Demorou {} anos para a cidade A ultrapassar a cidade B em população".format(anos))
