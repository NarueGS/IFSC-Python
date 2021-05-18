num = int(input("Digite um valor inteiro maior que 0 e menor que 32 "))
if num < 32 and num >0:
    array = [0,0,0,0,0]
    tempnum = num
    for bit in range(1,6,1):
        if tempnum >= (2**(5-bit)):
            array[bit-1] = 1
            tempnum -=  (2**(5-bit))
        else:
            array[bit-1] = 0
    print("O valor em binário é: {}".format(array))