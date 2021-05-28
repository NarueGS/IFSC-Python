import random

with open(r'lista.txt','r') as temp:
    lista = temp.readlines()
temp.close()
randomic = random.randint(0,len(lista)-1)
linha = lista[randomic]
palavra,hint = linha.split()
palavraArray = []
palavraArray [:] = palavra
chances = len(palavraArray)
if chances > 26:
    chances = 25
escondido = []
acerto = False
for cont in range(len(palavraArray)):
    escondido.append('_')
while 1:
    print(escondido, " Dica: ",hint, "Você tem {} chances".format(chances))
    chute = input("")
    character = []
    character [:0] = chute
    for k in range(len(palavraArray)):
        if character[0] == palavraArray[k].lower():
            escondido[k] = palavraArray[k]
            acerto = True
    if acerto == False:
        chances-= 1
    else:
        acerto = False
    if chances == 0:
        print("Você perdeu")
        quit()
    elif escondido == palavraArray:
        print("Você ganhou, a palavra era: ",palavra)
        quit()