num = int(input("Digite um número de 3 algarismos: "))
tempnum = num % 10
tempnum2 = ((num-tempnum)//10)%10 
tempnum3 = (num // 100)
print("O valor de {} invertido é: {}{}{}".format(num,tempnum,tempnum2,tempnum3))