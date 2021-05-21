"""
37. Uma academia deseja fazer um senso entre seus clientes para  descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da  academia seu código, sua altura e seu peso. 
O final da digitação de dados  deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar  o programa também deve ser informados os códigos e valores do clente
 mais  alto, do mais baixo, do mais gordo e do mais magro, além da média das  alturas e dos pesos dos clientes 
"""
maisalto = 0.0
maisaltoCodigo = 0.0
maisbaixo = 1000.0
maisbaixoCodigo = 0.0
maisgordo = 0.0
maisgordoCodigo = 0.0
maismagro = 1000.0
maismagroCodigo = 0.0
cont = 0
ArrayAltura = []
ArrayPeso = []
ArrayCodigo = []
mediaAltura = 0
mediaPeso = 0
while 1:
    codigo = int(input("Digite o código de cliente:  "))
    if codigo == 0:
        break
    altura = float(input("Digite a altura do seu cliente: "))
    peso = float(input("Digite o peso do seu cliente: "))
    if altura > maisalto:
        maisalto = altura
        maisaltoCodigo = codigo
    if altura < maisbaixo:
        maisbaixo = altura
        maisbaixoCodigo = codigo
    if peso > maisgordo:
        maisgordo = peso
        maisgordoCodigo = codigo
    if peso < maismagro:
        maismagro = peso
        maismagroCodigo = codigo
        cont += 1
    ArrayAltura.append(altura)
    ArrayCodigo.append(codigo)
    ArrayPeso.append(peso)
for x in range(len(ArrayAltura)):
    mediaAltura += ArrayAltura[x]
for x in range(len(ArrayPeso)):
    mediaPeso += ArrayPeso[x]
print("O cliente {} é o mais alto com {} metros".format(maisaltoCodigo,maisalto))
print("O cliente {} é o mais baixo com {} metros".format(maisbaixoCodigo,maisbaixo))
print("O cliente {} é o mais gordo com {} kilos".format(maisgordoCodigo,maisgordo))
print("O cliente {} é o mais magro com {} kilos".format(maismagroCodigo,maismagro))
print("A média de altura dos seus clientes é: {:.2f} metros".format(mediaAltura/len(ArrayAltura)))
print("A média de peso dos seus cliente é: {:.2f} kilos".format(mediaPeso/len(ArrayPeso)))
