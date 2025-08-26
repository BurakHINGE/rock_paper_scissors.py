import random

while True:
    lives = 3
    score = 0
    moves = ["rock", "paper", "scissors"]

    while lives != 0:
        x = random.randint(0, 2)
        computer_move = moves[x]
        player_move = input("Rock, paper, scissors?\n")
        
        if computer_move == player_move:
            print("It's a draw!")

        elif player_move == "rock":
            if computer_move == "paper":
                lives -= 1
                print(f"You lost, {lives} lives left!")
            else:
                score += 10
                print(f"You won, your total score is {score}!")

        elif player_move == "paper":
            if computer_move == "scissors":
                lives -= 1
                print(f"You lost, {lives} lives left!")
            else:
                score += 10
                print(f"You won, your total score is {score}!")

        elif player_move == "scissors":
            if computer_move == "rock":
                lives -= 1
                print(f"You lost, {lives} lives left!")
            else:
                score += 10
                print(f"You won, your total score is {score}!")    

    print(f"Congratulations, you finished the game with a total of {score} points!")
