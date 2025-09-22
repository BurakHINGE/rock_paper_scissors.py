import random
import json

username = input("Enter your username: ")

try:
    with open("scores.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

if username not in data:
    data[username] = {"score": 0, "games_played": 0, "wins_against_bot": 0, "draws_against_bot": 0, "losses_against_bot": 0}

while True:  
    start = input("\nPress ENTER to play Rock Paper Scissors (q to quit): ").lower()
    if start == "q":
        print("Exited. See you next time!")
        break 
    
    lives = 3
    score = 0
    moves = ["rock", "paper", "scissors"]

    while lives != 0:
        move = input("Rock, paper, scissors? ").lower()
        
        if move not in moves:
            print("Invalid move, try again!")
            continue

        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")

        if computer_move == move:
            print("Draw!")

        elif (move == "rock" and computer_move == "scissors") or \
             (move == "paper" and computer_move == "rock") or \
             (move == "scissors" and computer_move == "paper"):
            score += 10
            print(f"You win! Total score: {score}")

        else:
            lives -= 1
            print(f"You lose! Remaining lives: {lives}")

    print(f"Congratulations, game over! You earned a total of {score} points!")

    data[username]["score"] += score
    data[username]["games_played"] += 1

    if score > 30:
        data[username]["wins_against_bot"] += 1
    
    elif score == 30:
        data[username]["draws_against_bot"] += 1

    else:
        data[username]["losses_against_bot"] += 1

    with open("scores.json", "w") as file:
        json.dump(data, file, indent=4)

    stats = data[username]

    print(f"{username} \nTotal Score: {stats['score']}"
      f"\nGames Played: {stats['games_played']}"
      f"\nWins vs Bot: {stats['wins_against_bot']}"
      f"\nDraws vs Bot: {stats['draws_against_bot']}"
      f"\nLosses vs Bot: {stats['losses_against_bot']}")
