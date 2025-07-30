# rock paper scissors game
import random

options=("rock","paper","scissors")
playing=True

while playing:
    player=None
    computer= random.choice(options)

    while player not in options:
        player=input("enter your choice rock,paper,scissors:")

    print(f"players choice:{player}")
    print(f"computers choice:{computer}")

    if(player==computer):
        print("its a draw!")                               
    elif(player=="rock" and computer=="scissors"):
            print("you win!")
    elif(player=="paper" and computer=="rock"):
        print("you win!")
    elif(player=="scissors" and computer=="paper"):
        print("you win!")
    else:
        print("you lose !")
        
    play_again=input("play_again? (y/n):").lower()
    if not play_again=="y":
         playing=False
print("thanks for playing:) ")




