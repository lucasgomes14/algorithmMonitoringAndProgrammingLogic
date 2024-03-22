entrada1 = input()
entrada2 = input()
entrada3 = input()

if(entrada1.lower() == "vertebrado"):
    if(entrada2.lower() == "ave"):
        if(entrada3.lower() == "carnivoro"):
            print("aguia")
        elif(entrada3.lower() == "onivoro"):
            print("pomba")
        else:
            print("Terceira entrada nao encontrada")
    elif(entrada2.lower() == "mamifero"):
        if (entrada3.lower() == "onivoro"):
            print("homem")
        elif (entrada3.lower() == "herbivoro"):
            print("vaca")
        else:
            print("Terceira entrada nao encontrada")
    else:
        print("Segunda entrada nao encontrada")
elif(entrada1.lower() == "invertebrado"):
    if(entrada2.lower() == "inseto"):
        if (entrada3.lower() == "hematofago"):
            print("pulga")
        elif (entrada3.lower() == "herbivoro"):
            print("lagarta")
        else:
            print("Terceira entrada nao encontrada")
    elif(entrada2.lower() == "anelideo"):
        if (entrada3.lower() == "hematofago"):
            print("sanguessuga")
        elif (entrada3.lower() == "onivoro"):
            print("minhoca")
        else:
            print("Terceira entrada nao encontrada")
    else:
        print("Segunda entrada nao encontrada")

else:
    print("Primeira entrada nao encontrada")
