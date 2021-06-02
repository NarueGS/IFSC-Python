"""
5) Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da  outra. 
Escreva uma função chamada is_anagram que tome duas strings e retorne True  se forem anagramas 
ou False caso contrário. Ex: Roma, Amor 
"""
def is_anagram(palavra1,palavra2):
    check = True
    final = len(palavra2) - 1
    inicial = 0
    for cont in range(len(palavra2)):
        if check == True:
            if inicial <= final:
                if palavra1[inicial] != palavra2[final]:
                    check = False
        inicial +=1
        final -=1
    return check

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
check = is_anagram(palavra1,palavra2)
if check == True:
    print("É um anagrama")
else:
    print("Não é um anagrama")
