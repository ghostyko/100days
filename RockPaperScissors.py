import random

print("Let's play Rock Paper Scissors together!")

# rock beats scissors
# scissors beats paper
# paper beats rock

rps = ["rock", "paper", "scissors"]


while True:
    player_1 = input("Do you choose Rock, Paper, or Scissors? ").lower()
    ai = random.choice(rps)
    print(f"Opponent chose {ai}")

    if player_1 == ai:
        print("Tie, try again.")
    elif player_1 == "rock" and ai == "scissors" or \
        player_1 == "scissors" and ai == "paper" or \
        player_1 == "paper" and ai == "rock":
        print("You Win")
    else:
        print("You Lose")
        exit()




