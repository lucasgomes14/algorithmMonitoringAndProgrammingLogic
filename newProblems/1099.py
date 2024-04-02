quantidade = int(input())

for i in range(quantidade):
    entradas = input().split(" ")

    x = int (entradas[0])
    y = int (entradas[1])

    soma = 0

    if(x < y):
        for j in range(x + 1, y):
            if(j % 2 != 0):
                soma += j
    else:
        for j in range(y + 1, x):
            if(j % 2 != 0):
                soma += j
    print(soma)