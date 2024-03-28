print("--------------Welcome to rock,paper and scissor game-------------------")
import random
computer_wins = 0
player_wins = 0
def user_choice():
    while True:
        user_input = input("Enter your choice (rock,paper,scissor):").lower()
        if user_input in ["rock","paper","scissor"]:
            return user_input
        else:
            print("Invalid input")
def computer_choice():
    return random.choice(["rock","papaer","scissor"])
def determine_winner(user_choice,computer_choice):
    global player_wins,computer_wins
    if user_choice == computer_choice:
        print("It's a tie game.")
    elif (user_choice =="rock" and computer_choice == "scissor") or  (user_choice =="paper" and computer_choice == "rock") or (user_choice =="scissor" and computer_choice == "paper"): 
        player_wins +=1
        print("Player wins")
    else:
        computer_wins += 1 
        print("Computer wins")  
def play_game():
    while True:
        users_choice = user_choice()
        computers_choice = computer_choice()
        print(f"you choose {users_choice} and computer choose {computers_choice}")  
        determine_winner(users_choice,computer_choice)
        play_again = input("Do you want to play again (Y or N):").upper()
        if play_again != "Y":
            break
if __name__ == "__main__":
    play_game()
    print(f"Player wins {player_wins} times")  
    print(f"Computer wins {computer_wins} times")

