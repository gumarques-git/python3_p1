# -*- coding: UTF-8 -*-

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 5
tentativas = 4

for rodada in range(1,tentativas + 1):
    print('Tentativa {} de {}.'.format(rodada, tentativas)) #String Interpolation
    chute = int(input("Digite um número entre 1 e 10: "))
    print("Você digitou " , chute)
    if (chute < 1 or chute >10):
        print("Número incorreto!!!", "\n")
        continue # pula o codigo abaixo e volta ao inicio do loop

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!", "\n")
        break # sai do loop se acertar
    elif(maior):
            print("O seu chute foi maior do que o número secreto!", "\n")
    elif(menor):
            print("O seu chute foi menor do que o número secreto!", "\n")

print("Fim do jogo")