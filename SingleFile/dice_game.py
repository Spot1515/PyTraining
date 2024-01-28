import random

def roll():
    min_value = 1
    max_vale = 10
    roll = [random.randint(min_value, max_vale),random.randint(min_value, max_vale)]
    return roll




while True:
    players = input("Please enter player count 2 to 4.")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("\nPlease entere a valide count\n")
    else:
        print("please enter a number")

max_score = 100
player_scores = [0 for _ in range(players)]

#print(player_scores)

while max(player_scores) < max_score:
    for i in range(players):
        should_roll = input(f"\nWould you like to roll player {i + 1} (y)?").lower()
        if should_roll == 'q':
            quit()
        elif should_roll != 'y':
            continue

        if should_roll != 'y':
            break
        value = roll()
        print(f"You rolled a {value}")
        
