while(True):
    quantidade = int(input())

    if(quantidade == 0):
        break
    else:
        for i in range(1, quantidade + 1):
            if(i < quantidade):
                print(i, end=" ")
            else:
                print(i)