print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 5

chute_str = input("Digite um número entre 0 e 10: ")
print("Você digitou " , chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Parabéns! Você acertou!")
elif(maior):
        print("O seu chute foi maior do que o número secreto!")
elif(menor):
        print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")