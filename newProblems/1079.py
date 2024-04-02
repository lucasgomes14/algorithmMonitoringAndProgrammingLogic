n = int(input())

for i in range(n):
    valor = input().split(" ")
    mediaPoderada = float (valor[0]) * 2 + float (valor[1]) * 3 + float (valor[2]) * 5
    mediaPoderada /= 10
    print("{:.1f}".format(mediaPoderada))