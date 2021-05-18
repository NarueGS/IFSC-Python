idade = int(input("Digite sua idade: "))
if idade >= 16 and idade < 18:
    print("Pode votar mas não dirigir")
elif idade < 16:
    print("Não pode votar nem dirigir")
else:
    print("Pode votar e dirigir")
