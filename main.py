# TicTac-Toe, Started at 08/06/2024 and finished at 08/08/2024

inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Values that will be replaced by "X" or "O"
gameEnd = False # Global boolean that determines when a player wins or a draw happens
notadraw = False # Global boolean that will only be used when a player wins at the last position, which will trigger the win and draw screens

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
def player(name = "", pinput = ""): # Name parameter holds the player 1/2 name, and pinput defines if the player input is "X" or "O"

        print(f"\n== PLAYER {name} TURN ==") # Showing player name
        while True:
            try:
                playerinput = int(input("\nType the position: ")) # Position in the grid which the player will change to "X" or "O"

                # If the value is out of index, the program will make you type a new one in the range of 1 to 9
                if playerinput > 9 or playerinput < 1:
                    print("\n" * 500)
                    interface()
                    print("\nType a position in the range of 1-9.")
                    continue
                else:
                    break
            
            # If the player types a value which is not an int, it will make you type a valid int value
            except (ValueError):
                print("\n" * 500)
                interface()
                print("\nThis position does not exist. Type a new position.")
    
            
        # Using while to avoid input errors
        while True:

            # If the position which the player choose already has an O or X, the program will make him choose a new one
            if inputs[playerinput] == "O" or inputs[playerinput] == "X":
                print("\n" * 500)
                interface()
                print("\nPosition is already taken")
                playerinput = int(input("\nType new position: "))
            else: 
                inputs[playerinput] = pinput # assigning the position the player choose with his correspondent input (X or O)
                break

        print("\n" * 500)
        interface()


# Function that will serve as a template to read all possible outcomes for winning
def checkvictory(userinput = "", pname = "", startindex = 1, endindex = 9, step = 1):

    global gameEnd
    global notadraw
    inputcount = 0 # Variable that will tell how many times X or O was found in the loop range


    # A loop range which will be chosen it's startindex, endindex and step, so it can read a specified sequence
    # Example if you choose 1 as the startindex, 4 as the endindex, and step as 1, it will read the 1 2 3 horizontal line
    # Then, if it finds 3 identical userinputs (3 Xs or 3 Os), it determines as a win for the player that hit this sequence, and ends the game
    # If not, then it just go to the next turn
    for i in range(startindex, endindex, step):

        if inputs[i] == userinput:
            inputcount += 1

            if inputcount == 3:
                
                print("\n== GAME FINISHED ==")
                print(f"\nPlayer {pname} has won!")
                gameEnd = True
                notadraw = True

            


# A function that will read all possible sequences that determines as a win in tictactoe
def winpossibilities(pname = "", userinput = ""):

    global notadraw

    # Horizontal
    checkvictory(userinput, pname, 1, 4) # 1 2 3
    checkvictory(userinput, pname, 4, 7) # 3 5 6
    checkvictory(userinput, pname, 7, 10) # 7 8 9
    
    # Vertical
    checkvictory(userinput, pname, 1, 8, 3) # 1 4 7
    checkvictory(userinput, pname, 2, 9, 3) # 2 5 8
    checkvictory(userinput, pname, 3, 10, 3) # 3 6 9

    # Diagonal
    checkvictory(userinput, pname, 1, 10, 4) # 1 5 9
    checkvictory(userinput, pname, 3, 8, 2) # 3 5 7

    # The code belows makes the game end as a draw when all the values in the grid are Xs or Os
    inputcount = 0
    for items in inputs:

        if items == "X" or items == "O":
            inputcount += 1
    
    if inputcount == 9 and notadraw == False:
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

    print("\n" * 500)
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

    # This loop will make the player choose if he wants to continue playing or wants to end the session
    while True:
        
        replay = input("\nWanna play again? [Y/N]: ")
        replay = replay.upper()

        # If player responds with a YES, all the values are resetted and the game restarts
        if replay == "Y":
            global inputs
            inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            gameEnd = False
            print("\n" * 500)
            game()
            break
        
        # If the player responds with NO, the game ends and the application closes
        elif replay == "N":
            print("\nThanks for playing !")
            break
        
        # If the player responded with anything different, it will make him choose again between Y or N.
        else:
            continue
    


# using \n so the application is not glued with the terminal codes
print("\n")
game()
print()






