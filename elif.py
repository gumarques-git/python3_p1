print("*********************************")
print("Guess a number games!")
print("*********************************")

secret = 5

guess = input("Type a number from 0 to 10: ")

your_guess = int(guess)

acertou = your_guess == secret
maior = your_guess > secret
menor = your_guess < secret

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")