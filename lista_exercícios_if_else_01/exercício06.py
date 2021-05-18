altura = float(input("Digite a sua altura \n"))
sexo = int(input("Digite 1 se seu sexo for feminino e digite 2 se for masculino \n"))
if sexo == 2:
    peso_ideal = 72.7*altura-58
elif sexo == 1:
    peso_ideal = (62.1*altura)-44.7
print("Seu peso ideal é: {}".format(peso_ideal))
