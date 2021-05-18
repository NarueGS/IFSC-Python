a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
lista = [a,b,c]
lista.sort()
print("O maior valor é: ",lista[(len(lista)-1)])