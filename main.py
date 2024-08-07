inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Values that will be replaced by "X"or "O"


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
    
# using \n so the grid is not glued with the terminal codes
print("\n")
interface()
print("\n")