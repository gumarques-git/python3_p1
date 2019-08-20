print("*********************************")
print("Guess a number games!")
print("*********************************")

secret = 8

your_guess = input("Type a number from 0 to 10: ")

print('Your guess: ', your_guess)

if(secret == int(your_guess)):
    print('Very good!')
else:
    print('Oops, not this time!')