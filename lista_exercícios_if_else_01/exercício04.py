num = int(input("Digite quantas maçãs deseja comprar: "))
if num < 12:
    print("O valor da compra é: {}R$".format(num*0.3))
else:
    print("O valor da compra é: {} Reais".format(num*0.25))