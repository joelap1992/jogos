print("****************************")
print("Bem vindo Python Adivinhação")
print("****************************")

numero_secreto = 500
tentativa      = 4

# rodada         = 9 tirando para fazer o laço FOR

for rodada in range(1,tentativa + 1):
    print("Tentativas {} de {}".format(rodada, tentativa))
    chute =int(input("Digite um número entre 1 e 100: "))
    print("Você digitou o número: ",chute)
    
    if(chute < 0 or chute > 100):
      break 

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!!!")
    else:
        if(maior):
            print("Errou! O número foi maior que o número Secret!!!")
        elif(menor):
            print("Errou! O número foi menor que o número Secret!!!")
#    rodada    = rodada    + 1
