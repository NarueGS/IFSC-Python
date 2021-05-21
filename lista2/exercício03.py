"""
3. Faça um programa que leia e valide as seguintes informações: a. Nome: maior que 3 caracteres; 
b. Idade: entre 0 e 150; 
c. Salário: maior que zero; 
d. Sexo: 'f' ou 'm'; 
e. Estado Civil: 's', 'c', 'v', 'd'; 
Use a função len(string) para saber o tamanho de um texto (número de  caracteres). 

"""
#variaveis:
nome = 'A'
idade = -1
salario = 0
sexo = 'N'
eCivil = 'b'
aux = 'A'
aux = [0,0,0,0,0]
while (1):
    if aux[0] == 0 or aux[1] == 0 or aux[2] == 0 or aux[3] == 0 or aux[4] == 0:
        if len(nome)<3:
            nome = input("Digite seu nome, o nome deve conter pelo menos três letras:  ")
        else:
            aux[0] = 1
        if idade<0 or idade > 150:
            idade = int(input("Digite sua idade em anos, ela deve estar entre 0 e 150 anos:  "))
        else:
            aux[1] = 1
        if salario <= 0:
            salario = int(input("Digite o seu salario, ele deve ser maior que 0:  "))
        else:
            aux[2] = 1
        if sexo != 'F' and sexo != 'M':
            sexo = input("Digite seu sexo, ele deve ser F para feminino e M para masculino:  ")
            sexo = sexo.upper()
            sexo = sexo[0]
        else:
            aux[3] = 1
        if eCivil != 'S' and eCivil != 'C' and eCivil != 'V' and eCivil != 'D':
            eCivil = input("Digite seu estado civil, sendo s, c, v ou d:  ")
            eCivil = eCivil.upper()
            eCivil = eCivil[0]
        else:
            aux[4] = 1
    else:
        break
print("Seu nome é: ",nome)
print("Sua idade é: ",idade)
print("Seu salario é: ",salario)
print("Seu sexo é: ",sexo)
print("Seu estado civil é: ",eCivil)