"""
4 - Lei dos Grandes Números (Law of Large Numbers) 
A Lei dos Grandes Números tem origem na teoria da probabilidade. 
Para entender o que ela significa, sugiro que você leia esse artigo na Wikipedia. 
Em resumo, na Lei dos Grandes Números, “a média aritmética dos resultados da realização da  mesma experiência repetidas vezes tende a se aproximar do valor esperado à medida que mais  tentativas se sucederem”. 
É fácil de entender o que isso significa… 
Imagine um dado com 6 lados. 
A probabilidade de sair cada um dos 6 lados é de 1/6. 
Então, se você jogar o dado milhares de vezes, cada resultado possível saíra em 1/6 das vezes. A média aritmética desses resultados possíveis, (1 + 2 + 3 + 4 + 5 + 6)/6, é igual a 3,5. 
Perceba que 3,5 é a média dos resultados ao longo de muitos lançamentos, não a  probabilidade de sair um resultado e nem o valor de um lado do dado. 
Problema proposto: 
Crie um programa que simule N lançamentos de um dado de 6 lados e imprima a média  aritmética dos resultados. Verifique se a média se aproxima de 3,5 à medida que o valor de  N aumenta. 

"""
import random
#variaveis
result = 0.0

num = int(input("Digite quantos lançamentos deseja realizar:  "))
array = [0 for _ in range(num)]
for cont in range(num):
    dado = random.randint(1,6)
    array[cont] = dado
for cont in range(num):
    result += array[cont]
print("A média aritmética é: {:.4f}".format((result/num)))