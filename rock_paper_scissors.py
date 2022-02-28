import random
#[0]

user_wins = 0
computer_wins = 0
ties_number = 0
choices = ["paper", "rock", "scissors"]


print("Welcom to Rock Paper Scissors game")
player = input("wahat is you name: ")

while True:
    player_choice = input(player+ " enter paper, rock, scissors to play or Q to quit ").lower()
    if player_choice == "q":
        break
    
    if player_choice not in choices:
        continue

    random_number = random.randint(0, 2)

    computer_choice = choices[random_number]
    print("the computer choose " + computer_choice)

    if player_choice == "rock" and computer_choice == "scissors":
        print("you win!!!!!")
        user_wins += 1

    elif player_choice == "rock" and computer_choice == "rock":
        print("it's a tie!!!!")
        ties_number += 1

    elif player_choice == "paper" and computer_choice == "rock":
        print("you win!!!!!")
        user_wins += 1

    elif player_choice == "paper" and computer_choice == "paper":
        print("it's a tie!!!!")
        ties_number += 1

    elif player_choice == "scissors" and computer_choice == "paper":
        print("you win!!!!!")
        user_wins += 1

    elif player_choice == "scissors" and computer_choice == "scissors":
        print("it's a tie!!!!!")
        ties_number += 1

    else:
        print("you lost!!!!")
        user_wins += 1


print("you won", user_wins, "times")
print("the compurt won", computer_wins, "times")
print("you were tied", ties_number, "times")