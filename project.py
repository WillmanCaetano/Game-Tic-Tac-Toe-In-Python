import os

#Initializing game grid
grid = [['| |', '| |', '| |'],
        ['| |', '| |', '| |'],
        ['| |', '| |', '| |']]


#Initializing game variables
player = "X"
winner = None
gameRunning = True
player_scores = {}

#Function to print the game grid
def printGrid(grid):
    for i in grid:
        print(*i)
    print()


#Function for player's move
def play(grid):
    while True:
        try:
            inp = int(input(f"Player {player}, choose from (1-9): "))

            if inp >= 1 and inp <= 9:
                row = (inp - 1) // 3
                column = (inp - 1) % 3
                if grid[row][column] == '| |':
                    grid[row][column] = f'|{player}|'
                    break
                else:
                    print("Sorry, this position is no longer available. Try another!")
            else:
                print("Please choose a number from 1-9: ")
        except ValueError:
            print("Invalid input. Please enter a number!")


#Function to check for a winning line
def checkLine(grid):
    global winner
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != '| |':
            winner = grid[row][0]
            return True
    return False

#Function to check for a winning column
def checkColumn(grid):
    global winner
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '| |':
            winner = grid[0][col]
            return True
    return False

#Function to check for a winning diagonal
def checkDiagonal(grid):
    global winner
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '| |':
        winner = grid[0][0]
        return True

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '| |':
        winner = grid[0][2]
        return True

    return False


#Function to update player scores
def update_scores(player_scores, player, points):
    if player in player_scores:
        player_scores[player] += points
    else:
        player_scores[player] = points


#Function to check for a tie
def checkTie(grid):
    global gameRunning
    if all(cell != '| |' for row in grid for cell in row) and winner is None:
        printGrid(grid)
        print("It's a tie!")
        update_scores(player_scores, player1_name, 1)
        update_scores(player_scores, player2_name, 1)
        gameRunning = False

#function to check for a winner
def checkWinner():
    global gameRunning
    global winner
    if checkColumn(grid) or checkDiagonal(grid) or checkLine(grid):
        printGrid(grid)
        winner_symbol = f'|{player}|'
        winner_name = player2_name if winner_symbol == '|X|' else player1_name
        loser_name = player1_name if winner_symbol == '|X|' else player2_name
        print(f"The winner is {winner_name}")
        update_scores(player_scores, winner_name, 2)
        update_scores(player_scores, loser_name, 0)
        gameRunning = False



#function to switch player
def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# Get player's names
player1_name = input("Enter the name of Player 1: ")
while player1_name.isdigit():
    print("Invalid name. Please enter a valid name for Player 1.")
    player1_name = input("Enter the name of Player 1: ")

player2_name = input("Enter the name of Player 2: ")
while player2_name.isdigit():
    print("Invalid name. Please enter a valid name for Player 2.")
    player2_name = input("Enter the name of Player 2: ")

#Clean up player's names
player1 = player1_name.strip()
player2 = player2_name.strip()

#Function to load player's scores from a file
def load_scores(file_name):
    player_scores = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                player, score_text = line.strip().split(':')
                score = int(score_text.split()[0])
                player_scores[player] = score
    return player_scores


#File to save player scores
file_name = "scores.txt"

#load existing scores from the file
player_scores = load_scores(file_name)

#Function to save player scores to a file   
def save_scores(file_name, player_scores):
    with open(file_name, 'w') as file:
        for player, score in player_scores.items():
            file.write(f"{player}: {score} points\n")


#Function to ask if players want to play again
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
while True:

#Main game loop
    while gameRunning:
        printGrid(grid)
        play(grid)
        switchPlayer()
        checkTie(grid)
        checkWinner()

    #Display final scores
    print("Final Scores:")
    for player, score in player_scores.items():
        print(f"{player}: {score} points")

    save_scores(file_name, player_scores)  

    #Ask if players want to play again
    if play_again():

        #Reset game state
        grid = [['| |', '| |', '| |'],
                ['| |', '| |', '| |'],
                ['| |', '| |', '| |']]
        player = "X"
        winner = None

        # Get player names
        player1_name = input("Enter the name of Player 1: ")
        while player1_name.isdigit():
            print("Invalid name. Please enter a valid name for Player 1.")
            player1_name = input("Enter the name of Player 1: ")

        player2_name = input("Enter the name of Player 2: ")
        while player2_name.isdigit():
            print("Invalid name. Please enter a valid name for Player 2.")
            player2_name = input("Enter the name of Player 2: ")

        #Clean up player names
        player1 = player1_name.strip()
        player2 = player2_name.strip()
        gameRunning = True
    else: 
        break
