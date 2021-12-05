#tic-tac-toe game

#create new grid 
grid = [' ' for x in range(10)]

#print grid to the console
def print_Grid(grid):
    print('   |   |')
    print(' ' + grid[1] + ' | ' + grid[2] + ' | ' + grid[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[4] + ' | ' + grid[5] + ' | ' + grid[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[7] + ' | ' + grid[8] + ' | ' + grid[9])
    print('   |   |')

#insert 'X' or 'O' to grid
def insert_Move(position, letter):
    grid[position] = letter

#check if this position is free, if yes return True
def is_SpaceFree(position):
    return grid[position] == ' '

#check if the grid is full or not
def is_gridFull(grid):
    return not(grid.count(' ') > 1)

#check if player or computer win
def is_Winner(grid, letter):
    return ((grid[1] == letter and grid[2] == letter and grid[3] == letter) or \
    (grid[4] == letter and grid[5] == letter and grid[6] == letter) or \
    (grid[7] == letter and grid[8] == letter and grid[9] == letter) or \
    (grid[1] == letter and grid[4] == letter and grid[7] == letter) or \
    (grid[2] == letter and grid[5] == letter and grid[8] == letter) or \
    (grid[3] == letter and grid[6] == letter and grid[9] == letter) or \
    (grid[1] == letter and grid[5] == letter and grid[9] == letter) or \
    (grid[3] == letter and grid[5] == letter and grid[7] == letter))

#get position input from console and insert 'X' to grid
def player_Move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if (move > 0 and move < 10):
                if is_SpaceFree(move):
                    insert_Move(move, 'X')
                    return False
                else:
                    print("Choose another position !!!")
            else:
                print("Please type a number in range 1-9 !!!")
        except:
            print("Please type a number !!!")

#select random number from list
def select_Random(list):
    import random
    ln = len(list)
    rd = random.randrange(0, ln)
    return list[rd]

#guide computer how to play against player (A.I)
def computer_Move():
    possible_Moves = [x for x, letter in enumerate(grid) if x != 0 and letter == ' ' ]
    move = 0

    #check if there is a wining move
    for letter in ['O', 'X']:
        for i in possible_Moves:
            gridCopy = grid[:]
            gridCopy[i] = letter
            if is_Winner(gridCopy, letter):
                move = i
                return move

    #take any corner
    corners = [1, 3, 7, 9]
    cornersOpen = []
    for i in possible_Moves:
        for i in corners:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = select_Random(cornersOpen)
        return move
    
    #take any center
    if 5 in possible_Moves:
        move = 5
        return move

    #take any edge
    edges = [2, 4, 6, 8]
    edgesOpen = []
    for i in possible_Moves:
        for i in edges:
            edgesOpen.append[i]
    if len(edgesOpen) > 0:
        move = select_Random(edgesOpen)
    return move

#main part of this game
def main():
    print('Welcome to tic tac toe game !!!')
    print_Grid(grid)

    while not(is_gridFull(grid)):
        if not(is_Winner(grid, 'O')):
            player_Move()
            print_Grid(grid)
        else:
            print("Sorry, computer win this time !!!")
            break

        if not(is_Winner(grid, 'X')):
            move = computer_Move()
            if move == 0:
                print("Tie game !!!")
            else:
                insert_Move(move, 'O')
                print("Computer place 'O' at position ",move)
                print_Grid(grid)
        else:
            print("Player win this time !!!")
            break
    
    if is_gridFull(grid):
        print("Tie game !!!")

while True:
    answer = input('Do you want to play again? (Y/N): ')
    if answer.lower() == 'y' or answer.lower == 'yes':
        grid = [' ' for x in range(10)]
        print('-----------------------------------')
        main() 
    else:
        break