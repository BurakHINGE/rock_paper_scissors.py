import random

while True:  
    start = input("\nPress ENTER to play Rock Paper Scissors (or type 'q' to quit): ").lower()
    if start == "q":
        print("Exit. See you next time!")
        break 
    
    lives = 3
    score = 0
    choices = ["rock", "paper", "scissors"]

    while lives != 0:
        player_move = input("Rock, Paper, or Scissors? ").lower()
        
        if player_move not in choices:
            print("Invalid move, try again!")
            continue

        computer_move = random.choice(choices)
        print(f"Computer chose: {computer_move}")

        if computer_move == player_move:
            print("It's a tie!")

        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "paper" and computer_move == "rock") or \
             (player_move == "scissors" and computer_move == "paper"):
            score += 10
            print(f"You win! Total score: {score}")

        else:
            lives -= 1
            print(f"You lose! Remaining lives: {lives}")

    print(f"Game over! Your total score: {score}")
