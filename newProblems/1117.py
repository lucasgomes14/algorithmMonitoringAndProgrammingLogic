quantidadeNota = 0
soma = 0

while(quantidadeNota < 2):
    nota = float(input())

    if(nota >= 0 and nota <= 10):
        soma += nota
        quantidadeNota += 1
    else:
        print("nota invalida")

print("media = {:.2f}".format(soma / 2))