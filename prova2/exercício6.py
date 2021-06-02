"""
6) Escreva uma função que receba um número menor que 1000 e retorne o valor por  extenso. Ex: 252 -> duzentos e cinquenta e dois
"""
import os

def function(inteiro):
    #variaveis de apoio
    inteiroAux = 0
    centenasAux = 0
    dezenasAux = 0
    unidadesAux = 0
    unidade = ["zero",'um',"dois","três","quatro","cinco","seis","sete","oito","nove"]
    dezena_unidade = ["dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
    dezena = ["vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
    centena = ["cento","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"]
    centena_perfeita = ["cem"]
    if inteiro/100 == 1:
        return(centena_perfeita[0])
    else:
        if inteiro%100 == 0:
            return(centena[inteiro//100 -1])
        else:
            if inteiro>99:        
                centenasAux = inteiro//100
            else:
                dezenasAux = inteiro//10
        if dezenasAux == 0:
            if inteiro >= 10:
                inteiroAux = inteiro-centenasAux*100
                dezenasAux = inteiroAux//10
        if inteiro%10 != 0:
            unidadesAux = inteiro%10
        if inteiro < 10:
            return(unidade[unidadesAux])
        elif inteiro < 100:
            if inteiro>19:
                if unidadesAux != 0:
                  return(dezena[dezenasAux-1], " e ",unidade[unidadesAux])
                else:
                    return(dezena[dezenasAux-2])
            else:
                return(dezena_unidade[unidadesAux])
        else:
                if dezenasAux == 0:
                    return(centena[centenasAux-1]," e ",unidade[unidadesAux])
                if dezenasAux < 2:
                    return(centena[centenasAux-1]," e ",dezena_unidade[unidadesAux])
                if dezena_unidade == 0:
                    return(centena[centenasAux-1]," e ",dezena[dezenasAux-2])
                return(centena[centenasAux-1], " e ", dezena[dezenasAux-2], " e ",unidade[unidadesAux])

                


inteiro = int(input("Digite um valor menor que 1000 \n"))
if inteiro >= 1000:
    while inteiro >= 1000:
        os.system('cls')
        inteiro = int(input("Digite um inteiro menor que 1000:  \n"))
lista = function(inteiro)
frase = "".join(lista)
print(frase)