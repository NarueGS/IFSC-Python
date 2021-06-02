"""
3) Crie um programa que leia um texto e faça a contagem das palavras. Você deve  eliminar os sinais de pontuação do texto.
 Exemplo: Maria foi ao mercado e ao dentista.  Maria comprou um refrigerante! 
Saída:  
Maria 2 
Ao 2 
Foi 1 
"""
palavra = input("Digite uma frase: ")
values = []
for letter in palavra:
    values.append(ord(letter))

spaces = 1
for cont in range(len(values)):
    if values[cont] == 32:
        spaces += 1
print(spaces)