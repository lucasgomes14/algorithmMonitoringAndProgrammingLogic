linha = int(input())
coluna = int(input())

if((linha % 2 == 0 and coluna % 2 == 0) or (linha % 2 != 0 and coluna % 2 != 0)):
    print(1)
else:
    print(0)