condicao = 1
vitoriaInter = 0
vitoriaGremio = 0
empate = 0
quantidade = 0

while(condicao == 1):
    placar = input().split(" ")

    inter = int (placar[0])
    gremio = int (placar[1])


    if(inter > gremio):
        vitoriaInter += 1
    elif(gremio > inter):
        vitoriaGremio += 1
    else:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    condicao = int(input())
    quantidade += 1

print("{} grenais".format(quantidade))
print("Inter:{}".format(vitoriaInter))
print("Gremio:{}".format(vitoriaGremio))
print("Empates:{}".format(empate))

if(empate > vitoriaInter and empate > vitoriaGremio):
    print("Nao houve vencedor")
elif(vitoriaGremio > vitoriaInter):
    print("Gremio venceu mais")
else:
    print("Inter venceu mais")

