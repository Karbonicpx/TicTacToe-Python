
import mysql.connector
from colorama import Fore, Style
from tabulate import tabulate

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='ranking'
); # Acessing mysql server

mycursor = mydb.cursor() # Object that will comunicate with the database


# Function that will register the name in the database
def insertinfo(name):

    name = repr(name) # Transform to `name``
    query = f"INSERT INTO players (id, playername, wins, matches) VALUES (DEFAULT,{name}, DEFAULT, DEFAULT)"
    mycursor.execute(query) # Executing the query
    mydb.commit() # Making changes to the database


# This function will check if a value exists in an specified column
def recordexists(column, value):

    try:
        query = f"SELECT COUNT(*) FROM players WHERE {column} = %s"
        mycursor.execute(query, (value,)) # Executing query with the value as parameter

        result = mycursor.fetchone() # Receiving the information from the execution of the query

        exists = result[0] > 0 # Checking if the value exists, if the tuple stored has at least 1 value (name)

        return exists # Return true or false
    
    # Exception if the sql server doesn't connect
    except mysql.connector.Error as err:
        print(f"Value: {err}")
        return False
    
# This function will print the ranking in an organized table in the terminal
def printranking():
    query = "SELECT playername, wins, matches FROM players ORDER BY wins desc, matches asc;"
    mycursor.execute(query)

    ranking = mycursor.fetchall() # Receiving all instances of information from the sql server

    # Fields where the ranking will be separated into, with colors (colorama library)
    fields = [f"{Fore.YELLOW}Player{Style.RESET_ALL}", 
                    f"{Fore.GREEN}Wins{Style.RESET_ALL}", 
                    f"{Fore.CYAN}Matches{Style.RESET_ALL}"]

    # Coloring each row with informations
    colored_fields = [[f"{Fore.BLUE}{player}{Style.RESET_ALL}", 
                        f"{Fore.GREEN}{wins}{Style.RESET_ALL}", 
                        f"{Fore.CYAN}{matches}{Style.RESET_ALL}"] 
                        for player, wins, matches in ranking]


    # Using tabulate library to generate the ranking table
    rankingtable = tabulate(colored_fields, headers = fields, tablefmt='grid')
    print(f"\n{rankingtable}\n")

# This function will increment the win/matches column based on the game results
# updatewin parameter determines if it will update the win column or matches column
def updatewinmatches(playername, updatewin = True):
     
    playername = repr(playername)

    if updatewin == True:
        updatewins = f"UPDATE players SET wins = COALESCE(wins, 0) + 1 WHERE playername = {playername};"
        mycursor.execute(updatewins)
        mydb.commit()

    elif updatewin == False:

        updateonlymatches = f"UPDATE players SET matches = COALESCE(matches, 0) + 1 WHERE playername = {playername};"
        mycursor.execute(updateonlymatches)
        mydb.commit()
