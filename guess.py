# -*- coding: UTF-8 -*-
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #Procedure utilizando dictionary simulando um Swith Case
    def retorna(x):
        return {'1': 20, '2': 12, '3': 8, '4': 2}[x]     #.get(x, 9)   # para usar default, 9 is default if x not found

    print('Escolha o nivel de dificuldade:')
    nivel  = input('(1) Facil (2) Medio (3) Dificil (4) Nightmare: ')

    tentativas = retorna(nivel)
    numero_secreto = random.randrange(1,101)
    pontos = 1000

    for rodada in range(1,tentativas + 1):
        print('Tentativa {} de {}.'.format(rodada, tentativas)) #String Interpolation
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou " , chute)
        if (chute < 1 or chute >100):
            print("Número incorreto!!!", "\n")
            continue # pula o codigo abaixo e volta ao inicio do loop

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos), "\n")
            break # sai do loop se acertar
        elif(maior):
            print("O seu chute foi maior do que o número secreto!", "\n")
        else:
            print("O seu chute foi menor do que o número secreto!", "\n")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim do jogo.\n")

if __name__ == "__main__":
    jogar()