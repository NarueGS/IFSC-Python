"""
4) Faça uma função que receba um texto e verifique se o texto é um palíndromo
 (possui a  mesma sequência de letras nos dois sentidos) Exemplo: arara, osso
"""
lista = list(input("Digite uma frase  "))
lista2 = []
lista2 = lista.copy()
lista2.reverse()
print(lista)
if lista2 == lista:
    print("A")
else: 
    print("B")