while(True):
    valores = input().split(" ")

    x = int (valores[0])
    y = int (valores[1])

    if(x > y):
        print("Decrescente")
    elif(y > x):
        print("Crescente")
    else:
        break