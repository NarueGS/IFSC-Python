"""
1) Faça um programa que conta quantos caracteres únicos existem em uma string. A  string 'Hello, world!' tem dez caracteres únicos,
 enquanto a string 'zzz' tem apenas um.  Utilize um dicionário para resolver esse problema. 

Exemplos de entrada Exemplos de saída 
Tuplas e Dicionários 
15 
Curso de Python 
13 
A próxima aula é sobre aninhamento 
19 

"""
palavra = input("Digite a sua frase ou palavra:  ")
dic = {'a': [False], 'b': [False], 'c': [False], 'd': [False], 'e': [False], 'f': [False], 'g': [False], 'h': [False], 'i': [False], 'j': [False], 'k': [False], 'l': [False], 'm': [False],
'n': [False], 'o': [False] ,'p': [False] ,'q': [False] ,'r': [False] ,'s': [False] ,'t': [False] ,'u': [False] ,'v': [False] ,'w': [False] ,'x': [False] ,'y': [False] ,'z': [False]}
cont = 0
lista = []
lista [:] = palavra.lower()
for letter in lista:
    print(letter)
    if letter != ' ':
        if dic[letter][0] == False:
            dic[letter][0] = True
print(cont)