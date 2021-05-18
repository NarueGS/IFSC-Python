dias = int(input("Quantos dias de vida você tem?  "))
anos = (dias // 365)
meses = (dias - anos * 365) // 30
dias = (dias - anos * 365) % 30
print(anos)
print(meses)
print(dias)
