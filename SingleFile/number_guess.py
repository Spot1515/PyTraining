import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please pick a number that is grater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

r = random.randint(0,top_of_range)
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == r:
            print("You got it!")
            print("The number was", r)
            break
        elif user_guess > r:
            print("You were above the number!")
        elif user_guess < r:
            print("You were below the number!")
    else:
        print("Please type a number next time.")
        continue

