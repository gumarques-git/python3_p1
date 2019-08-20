# -*- coding: UTF-8 -*-

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 5
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    print('Tentativa {} de {}.'.format(rodada, tentativas)) #String Interpolation
    chute = int(input("Digite um número entre 1 e 10: "))
    print("Você digitou " , chute)
    if chute not in range(1,10):
        print("Número incorreto!!!", "\n")
        continue # pula o codigo abaixo e volta ao inicio do loop

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!", "\n")
        exit() # sai do loop se acertar
    elif(maior):
            print("O seu chute foi maior do que o número secreto!", "\n")
    elif(menor):
            print("O seu chute foi menor do que o número secreto!", "\n")
    rodada += 1


print("Fim do jogo")