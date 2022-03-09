import random
def win():
    print("THE GAME: you win")
def lost():
    print("THE GAME: you lost")
def draw():
    print("THE GAME: it is a draw")
    
def the_game():
    moves=["rock","paper","scissors"]
    
    print("THE GAME: Rock, Paper, Scissors")
    attempts=3
    while attempts>0:
        if attempts==0:
            print("THE GAME: you fail to provide the correct option to play the game,goodbye")
            
        player=str(input("player:")).lower()
        if player.lower() not in moves:
            print(f"THE GAME:invalid option! you have {attempts} attempts left.")
            attempts-=1
        else:
            computer=random.choice(moves)
            print(f"computer: {computer}")
            
            if player==computer:
                draw()
            elif player=="rock" and computer=="scissors":
                win()
            elif player=="rock" and computer=="paper":
                lost()
            elif player=="scissors" and computer=="paper":
                win()
            elif player=="scissors" and computer=="rock":
                lost()
            elif player=="paper" and computer=="rock":
                win()
            elif player=="paper" and computer=="scissors":
                lost()
            else:
                pass
            
        attempts-=1
win()
lost()
draw()
the_game()