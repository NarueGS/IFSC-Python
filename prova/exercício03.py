for x in range(100,1000,1):
    array = [0,0,0]
    array[0] = x // 100
    array[1] = (x - (array[0]*100)) //10
    array[2] = (x- (array[0]*100)) - (array[1]*10)
    a = array[0]**3
    b = array[1]**3
    c = array[2]**3
    if (a+b+c) == x:
        print("O número {} é um número de armstrong".format(x))