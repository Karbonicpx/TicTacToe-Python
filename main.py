from os import system


inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Values that will be replaced by "X"or "O"
gameEnd = False
# Function that will show the visual part of the project
def interface():
    
    # Generating a grid interface in terminal
    # Each grid holds a number that matches with the grid "square" position
    print(f" {inputs[1]} | {inputs[2]} | {inputs[3]}")
    print("---|---|---")
    print(f" {inputs[4]} | {inputs[5]} | {inputs[6]}")
    print("---|---|---")
    print(f" {inputs[7]} | {inputs[8]} | {inputs[9]}")
    print("---|---|---")


# Function of player behaviour
def player(name = "", pinput = ""):

        print(f"\n== PLAYER {name} TURN ==")
        playerinput = int(input("\nType the position: ")) # Position in the grid which the player will change to "X" or "O"


        # Using while to avoid input errors
        while True:

            # If the position which the player choose already has an O or X, the application will make him choose a new one
            if inputs[playerinput] == "O" or inputs[playerinput] == "X":
                print("\n\n\n\n\n")
                interface()
                print("\nPosition is already taken")
                playerinput = int(input("\nType new position: "))
            else: 
                inputs[playerinput] = pinput
                break

        print("\n\n\n\n")
        interface()


def checkvictory(userinput = "", pname = "", startindex = 1, endindex = 9, step = 1):

    global gameEnd
    inputcount = 0
    for i in range(startindex, endindex, step):

        if inputs[i] == userinput:
            inputcount += 1

            if inputcount == 3:
                
                print("\n== GAME FINISHED ==")
                print(f"\nPlayer {pname} has won!")
                gameEnd = True

            


def winpossibilities(pname = "", userinput = ""):

    # Horizontal
    checkvictory(userinput, pname, 1, 4)
    checkvictory(userinput, pname, 4, 7)
    checkvictory(userinput, pname, 7, 10)
    
    # Vertical
    checkvictory(userinput, pname, 1, 8, 3)
    checkvictory(userinput, pname, 2, 9, 3)
    checkvictory(userinput, pname, 3, 10, 3)

    # Diagonal
    checkvictory(userinput, pname, 1, 10, 4)
    checkvictory(userinput, pname, 3, 8, 2)

    # Draw
    inputcount = 0
    for items in inputs:

        if items == "X" or items == "O":
            inputcount += 1
    
    if inputcount == 9:
        print("\n== GAME FINISHED ==")
        print(f"DRAW! No player won!")
        global gameEnd
        gameEnd = True
    
# Main function which will run the tictac-toe game
def game():

    player1name = input("Player 1 name: ")
    player2name = input("\nPlayer 2 name: ")
    p1input = "X"
    p2input = "O"
    replay = ""
    player1turn = True
    global gameEnd

    print("\n\n\n\n")
    interface()
    

    # Using while to assure the game will only end when player 1 or 2 wins
    while gameEnd == False:

        # In player 1 turn, will execute the behaviour of player 1
        if player1turn == True:

            player(player1name, p1input)
            winpossibilities(player1name, p1input)
            player1turn = False # Changing the turn to player 2

        # In player 2 turn, will execute the behaviour of player 2
        else:
            player(player2name, p2input)
            winpossibilities(player2name, p2input)
            player1turn = True # Changing the turn to player 1

    while True:
        
        replay = input("\nWanna play again? [Y/N]: ")
        replay = replay.upper()

        if replay == "Y":
            global inputs
            inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            gameEnd = False
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            game()
            break
        
        elif replay == "N":
            print("\nThanks for playing !")
            break

        else:
            continue
    


# using \n so the application is not glued with the terminal codes
print("\n")
game()
print()






