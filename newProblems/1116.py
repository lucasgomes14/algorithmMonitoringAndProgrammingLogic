quantidade = int(input())

for i in range(quantidade):
    entradas = input().split(" ")

    x = int (entradas[0])
    y = int (entradas[1])

    if(y == 0):
        print("divisao impossivel")
    else:
        print("{:.1f}".format(x / y))