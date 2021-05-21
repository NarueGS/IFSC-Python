"""
2. Faça um programa que leia um nome de usuário e a sua senha e não  aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro  e voltando a pedir as informações. 
"""

while (1):
    usuario = input("Digite um usuario:  ")
    senha = input("Digite uma senha:  ")
    if senha != usuario:
        print("Usuario registrado, obrigado por usar o programa")
        quit()
    else:
        print("O seu usuario não pode ser igual a sua senha")