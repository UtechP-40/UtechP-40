# guess the number
#dry principal
import random
winning_number = random.randint(1, 100)
for i in range(100):
    guess = int(input("Guess The Number : "))
    if guess == winning_number:
        print("YOU WIN")
        break
    else:
        if guess > winning_number:
            print("TOO HIGH")
        elif guess < winning_number:
            print("TOO LOW")
        elif guess > 100:
            print("THE NUMBER IS BETWEEN 1 TOO 100")
        elif guess < 0:
            print("THE NUMBER IS BETWEEN 1 TOO 100")
        else:
            print("wrong input ")
print(f"You have done this in {i} times")
    