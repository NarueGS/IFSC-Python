"""
43. O cardápio de uma lanchonete é o seguinte: 
o Especificação Código Preço 
o Cachorro Quente 100 R$ 1,20 
o Bauru Simples 101 R$ 1,30 
o Bauru com ovo 102 R$ 1,50 
o Hambúrguer 103 R$ 1,20 
o Cheeseburguer 104 R$ 1,30 
o Refrigerante 105 R$ 1,00 
Faça um programa que leia o código dos itens pedidos e as  quantidades desejadas. 
Calcule e mostre o valor a ser pago por item  (preço * quantidade) e o total geral do pedido.
 Considere que o cliente  deve informar quando o pedido deve ser encerrado. 
"""
Arraycodigo = [100, 101, 102, 103, 104, 105]
ArrayValor = [1.2,1.3,1.5,1.2,1.3,1.0]
continuar = 0

while 1:
    if continuar == 0:
        x = input("Deseja iniciar um novo pedido? Y  para sim N para não  ")
        x = x.upper()
        x = x[0]
        total = 0
    else:
        x = 'Y'
    valido = False
    cont = 0

    if x == 'Y':
        while 1:
            codigo = int(input("Digite um código válido   "))
            for x in range(len(Arraycodigo)):
                if codigo ==Arraycodigo[x]:
                    valido = True
                    cont = x
                    break
            if valido == True:
                break
        while 1:
            if valido == True:
                quant = int(input("Digite a quantidade que deseja incluir desse produto:  "))
                if quant >= 1:
                    valido = False
                    break
        total += ArrayValor[cont]*quant
        while 1:
            verificador = input("Deseja adicionar outro produto? Y  para sim N para não  ")
            verificador = verificador.upper()
            verificador = verificador[0]
            if verificador == 'Y':
                continuar = 1
                break
            elif verificador == 'N':
                continuar = 0
                print("O preço total é: {:.2f}".format(total))
                break

        
    else:
        quit()