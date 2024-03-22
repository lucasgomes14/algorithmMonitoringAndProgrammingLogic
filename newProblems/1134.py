alcool = 0
gasolina = 0
diesel = 0
while(True):
    tipoCombustivel = int(input())

    if(tipoCombustivel == 1):
        alcool += 1
    elif(tipoCombustivel == 2):
        gasolina += 1
    elif(tipoCombustivel == 3):
        diesel += 1
    elif(tipoCombustivel == 4):
        break

print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(alcool, gasolina, diesel))