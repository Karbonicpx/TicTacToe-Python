import databaseCore
from colorama import Fore, Style

inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Values that will be replaced by "X" or "O"
gameEnd = False # Global boolean that determines when a player wins or a draw happens
notadraw = False # Global boolean that will only be used when a player wins at the last position, which will trigger the win and draw screens


# Defining global variables to the colors for better understanding
redcolor = Fore.RED
bluecolor = Fore.BLUE
greencolor = Fore.GREEN
yellowcolor = Fore.YELLOW
resetstyle = Style.RESET_ALL

# Function that will show the visual part of the project
def interface():
    
    # Generating a grid interface in terminal
    # Each grid holds a number that matches with the grid "square" position
    print(f" {inputs[1]} | {inputs[2]} | {inputs[3]}")
    print(f"---|---|---")
    print(f" {inputs[4]} | {inputs[5]} | {inputs[6]}")
    print(f"---|---|---")
    print(f" {inputs[7]} | {inputs[8]} | {inputs[9]}")
    print(f"---|---|---")

# Function that will register the name typed by the players
# pnumber only exists so it shows 1 or 2 in the input
def databaseregister(pnumber):

    global bluecolor
    global redcolor
    global yellowcolor
    global resetstyle

    while True:

        if pnumber == "1":
            pname = input(f"\n{redcolor}Player {pnumber} name: {resetstyle}")
        
        else:
            pname = input(f"\n{bluecolor}Player {pnumber} name: {resetstyle}")
        
        pname = pname.capitalize().strip()
        
        # If name is empty, it will ask to type a new name
        if pname in "":
            print(f"{yellowcolor}\nType your name.{resetstyle}")
            continue
        
        # Calling the recordexists function to determine wether the name typed already exists or not in the database
        pname_exists = databaseCore.recordexists("playername", f"{pname}")

        # If name doesn't exist in the database, it will just add to the database
        if pname_exists == False:
            databaseCore.insertinfo(pname)
            break
        
        # If name exists, it will ask wether the player wants to continue or not, and the name is not added again to the database
        # I created this so the player knows that his playing in an already registered user
        else:
            print(f"\n{yellowcolor}Username is already registered. All matches won will be associated to the username. Continue?{resetstyle}")
            answer = input("\n[Y/N]: ")
            answer = answer.upper()

            if answer == "Y":
                break
            elif answer == "N":
                continue;

            # If he doesn't responds with Y or N, the loop resets
            else:
                print(f"\n{redcolor}Answer not valid. Asking again.{resetstyle}\n")
                continue

    return pname


# Function of player behaviour
def player(name, pinput): # Name parameter holds the player 1/2 name, and pinput defines if the player input is "X" or "O"

        global yellowcolor
        global redcolor
        global bluecolor
        global resetstyle


        print(f"\n{yellowcolor}== PLAYER {name} TURN =={resetstyle}") # Showing player name
        while True:

            # Treatments of errors
            try:

                playerinput = int(input(f"\n{yellowcolor}Type the position: {resetstyle}")) # Position in the grid which the player will change to "X" or "O"

                # Checking if in the position the player typed in, already exists a X or O
                if inputs[playerinput] == f"{redcolor}X{resetstyle}" or inputs[playerinput] == f"{bluecolor}O{resetstyle}":

                    print("\n" * 200)
                    interface()
                    print(f"\n{yellowcolor}Position is already taken.{resetstyle}")
                    playerinput = int(input(f"\n{yellowcolor}Type new position: {resetstyle}"))
                    continue
                
                # If the position is not taken, the application will substitute the position with X or O
                else:
                    inputs[playerinput] = pinput # assigning the position the player choose with his correspondent input (X or O)
                    break
            
            # If the player types any value that does not match with the positions, the loop resets
            except:
                print("\n" * 200)
                interface()
                print(f"\n{yellowcolor}This position does not exist. Type a new position.{resetstyle}") 

        print("\n" * 200)
        interface()


# Function that will serve as a template to read all possible outcomes for winning
def checkvictory(userinput, pname, color, startindex = 1, endindex = 9, step = 1):

    global gameEnd
    global notadraw
    global resetstyle
    global yellowcolor
    global redcolor
    global bluecolor
    inputcount = 0 # Variable that will tell how many times X or O was found in the loop range


    # A loop range which will be chosen it's startindex, endindex and step, so it can read a specified sequence
    # Example if you choose 1 as the startindex, 4 as the endindex, and step as 1, it will read the 1 2 3 horizontal line
    # Then, if it finds 3 identical userinputs (3 Xs or 3 Os), it determines as a win for the player that hit this sequence, and ends the game
    # If not, then it just go to the next turn
    for i in range(startindex, endindex, step):

        if inputs[i] == userinput:
            inputcount += 1

            if inputcount == 3:
                
                print(f"\n{yellowcolor}== GAME FINISHED =={resetstyle}")

                if color == redcolor:
                    print(f"\n{redcolor}Player {pname} has won!{resetstyle}")
                
                else:
                    print(f"\n{bluecolor}Player {pname} has won!{resetstyle}")

                gameEnd = True
                notadraw = True
                break

# A function that will read all possible sequences that determines as a win in tictactoe
def winpossibilities(pname = "", userinput = "", color = Fore.BLACK):

    global notadraw
    global yellowcolor
    global resetstyle

    # Horizontal
    checkvictory(userinput, pname, color, 1, 4) # 1 2 3
    checkvictory(userinput, pname, color, 4, 7) # 3 5 6
    checkvictory(userinput, pname, color, 7, 10) # 7 8 9
    
    # Vertical
    checkvictory(userinput, pname, color, 1, 8, 3) # 1 4 7
    checkvictory(userinput, pname, color, 2, 9, 3) # 2 5 8
    checkvictory(userinput, pname, color, 3, 10, 3) # 3 6 9

    # Diagonal
    checkvictory(userinput, pname, color, 1, 10, 4) # 1 5 9
    checkvictory(userinput, pname, color, 3, 8, 2) # 3 5 7

    # The code belows makes the game end as a draw when all the values in the grid are Xs or Os
    inputcount = 0
    for items in inputs:

        if items == f"{redcolor}X{resetstyle}" or items == f"{bluecolor}O{resetstyle}":
            inputcount += 1
    
    if inputcount == 9 and notadraw == False:
        print(f"\n{yellowcolor}== GAME FINISHED =={resetstyle}")
        print(f"{yellowcolor}DRAW! No player won!{resetstyle}")
        global gameEnd
        gameEnd = True
    
# Main function which will run the tictac-toe game
def game():

    global redcolor
    global bluecolor
    global yellowcolor
    global resetstyle
    global gameEnd

    print(f"{Fore.GREEN}==================== TIC-TACTOE ===================={resetstyle}")
    player1name = databaseregister("1") # Defining the names with the database register
    player2name = databaseregister("2")

    # This loop exists to check if the players have the same name
    # If they have, the register process happens again
    while True:

        if player2name == player1name:
            print(f"\n{yellowcolor}Players have the same username. Register again\n{resetstyle}")
            player1name = databaseregister("1")
            player2name = databaseregister("2")
        else:
            break;

    p1input = f"{redcolor}X{resetstyle}" # X with red color
    p2input = f"{bluecolor}O{resetstyle}" # O with blue color
    replay = ""
    player1turn = True
    

    print("\n" * 200)
    interface()
    

    # Using while to assure the game will only end when player 1 or 2 wins
    while True:

        # In player 1 turn, will execute the behaviour of player 1
        if player1turn == True:

            player(player1name, p1input)
            winpossibilities(player1name, p1input, redcolor)

            # If the game ends and is not a draw, the database increments 1 in the player wins column
            if gameEnd == True and notadraw == True:
                databaseCore.updatewinmatches(player1name, True)
                break
            
            # But if the game is a draw, the loop ends, and nothing happens
            elif gameEnd == True and notadraw == False : break

            # If the game doesn't ends:
            else:
                player1turn = False # Changing the turn to player 2

        # In player 2 turn, will execute the behaviour of player 2
        else:

            player(player2name, p2input)
            winpossibilities(player2name, p2input, bluecolor)

            # If the game ends and is not a draw, the database increments 1 in the player wins column
            if gameEnd == True and notadraw == True:
                databaseCore.updatewinmatches(player2name, True)
                break
            
            # But if the game is a draw, the loop ends, and nothing happens
            elif gameEnd == True and notadraw == False: break
            
            # If the game doesn't ends:
            else:
                player1turn = True # Changing the turn to player 1

    # Does not matter the result of the game: Everytime the matches column will be updated by 1 for both players
    databaseCore.updatewinmatches(player1name, False)
    databaseCore.updatewinmatches(player2name, False)

    # This loop will make the player choose if he wants to continue playing or wants to end the session
    while True:
        
        replay = input(f"\n{yellowcolor}Wanna play again? [Y/N]: {resetstyle}")
        replay = replay.upper()

        # If player responds with a YES, all the values are resetted and the game restarts
        if replay == "Y":
            global inputs
            inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            gameEnd = False
            print("\n" * 200)
            game()
            break
        
        # If the player responds with NO:
        elif replay == "N":

            # The program will ask if he wants to see the leaderboard
            # If YES, the leaderboards will be shown, if NO, the game ends
            while True:
                showranking = input(f"\n{yellowcolor}Do you want to see the leaderboard? [Y/N] {resetstyle}")
                showranking = showranking.upper()

                if showranking == "Y":
                    print("\n")
                    databaseCore.printranking()
                    break
                    
                elif showranking == "N": break

                else: continue
            
            break;
        
        # If the player responded with anything different, it will make him choose again between Y or N.
        else: continue
    


# using \n so the application is not glued with the terminal codes
print("\n")
game()
print(f"\n{Fore.GREEN}Thanks for playing!{Style.RESET_ALL}")
print()