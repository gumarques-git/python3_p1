# -*- coding: UTF-8 -*-
import random

def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")

    palavras = []

    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]  #Usando o List Comprehension

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))

        enforcou = erros == 7 # 7 é a quantidade de letras para formar o boneco.
        acertou = '_' not in letras_acertadas

        print(letras_acertadas, '\n')

    if acertou:
        print('Parabéns! Você ganhou!')
    else:
        print('Você perdeu.')

    print("Fim do jogo.\n")


if __name__ == "__main__":
    jogar()