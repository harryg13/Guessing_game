Secret_number = 8
Guess_count = 0
Guess_Limit = 3

while Guess_count<Guess_Limit:
    Guess = int(input('Guess: '))
    Guess_count += 1
    if Guess == Secret_number:
        print("Yay!You Won...")
        break
else:
    print("Sorry!You lose...")



