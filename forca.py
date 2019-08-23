# -*- coding: UTF-8 -*-

def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

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

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letras_acertadas

        print(letras_acertadas, '\n')

    if acertou:
        print('Parabéns! Você ganhou!')
    else:
        print('Você perdeu.')

    print("Fim do jogo.\n")


if __name__ == "__main__":
    jogar()