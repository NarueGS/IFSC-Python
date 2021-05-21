"""
41. Faça um programa que receba o valor de uma dívida e mostre uma  tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade  de parcelas e valor da parcela. 
o Os juros e a quantidade de parcelas seguem a tabela abaixo: o Quantidade de Parcelas % de Juros sobre o valor inicial  da dívida 
o 1 0 
o 3 10 
o 6 15 
o 9 20 
12 25 
Exemplo de saída do programa: 
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor  da Parcela 
R$ 1.000,00 0 1 R$  1.000,00 
R$ 1.100,00 100 3 R$  366,00 
R$ 1.150,00 150 6 R$  191,67 
"""
inicial = 1000
quant=[0,3,6,9,12]
juros = [0,10,15,20,25]
parcela = 0
jurosPrice = 0
parcelaPrice = 0
for x in range(len(quant)):
    valor = inicial * (1+(juros[x]/100))
    jurosPrice = valor-inicial
    if quant[x] != 0:
        parcelaPrice = valor/quant[x]
    else:
        parcelaPrice = inicial
    print("R${:.2f} {} {} {:.2f}".format(valor,int(jurosPrice),quant[x],parcelaPrice))
