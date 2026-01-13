import random

options = ("rock", "paper", "scissors")
player = None
player = input("Enter your choice: 'rock', 'paper', 'scissors': ")
computer = random.choice(options)

print(f"You chose", player)
print(f"CPU chose", computer)
if(computer == 'rock' and player == 'scissors'):
    print("CPU Wins")
if(computer == 'paper' and player == 'rock'):
    print("CPU Wins")
if(computer == 'scissors' and player == 'paper'):
    print("CPU Wins")

if(player == 'rock' and computer == 'scissors'):
    print("YOU WIN")
if(player == 'paper' and computer == 'rock'):
    print("YOU WIN")
if(player == 'scissors' and computer == 'paper'):
    print("YOU WIN")




