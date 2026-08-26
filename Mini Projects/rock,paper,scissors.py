#Rock, paper, scissors game.
import random as R
choices = R.choice(['rock', 'paper', 'scissors'])
guess = input("Enter your choice (rock, paper, scissors): ").lower()
if guess == choices:
    print("It is a tie! Both chose", choices)
elif guess == 'rock' and choices == 'paper':
    print("You lose! I chose paper")
elif guess == 'rock' and choices == 'scissors':
    print("You win! I chose scissors")
elif guess == 'paper' and choices == 'rock':
    print("You win! I chose rock")
elif guess == 'paper' and choices == 'scissors':
    print("You lose! I chose scissors")
elif guess == 'scissors' and choices == 'rock':
    print("You lose! I chose rock")
elif guess == 'scissors' and choices == 'paper':
    print("You win! I chose paper")
else:
    print("Error occured, please recheck!")