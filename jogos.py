# -*- coding: UTF-8 -*-
import forca
import guess


jogo = None

while jogo != '0':
    print("************************************")
    print("******     ESCOLHA O JOGO     ******")
    print("************************************")

    jogo = input("(1) Forca (2) Adivinhação (0) Sair :")

    if jogo == '1':
        forca.jogar()
    elif jogo == '2':
        guess.jogar()

print("Saindo dos jogos...")
