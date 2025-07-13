#Kido Douglas
#COMP112-01
#12-03-22
#Battle Ship Simulator

import random

#the boards for the ships and cpu/player guess
player_board = [[' ']* 9 for x in range (9)]#hidden
player_guess_board = [[' ']* 9 for x in range (9)]
opponent_board = [[' ']* 9 for x in range (9)]#hidden
opponent_guess_board = [[' ']* 9 for x in range (9)]
#Used to prevent coordinate repeats and terminate the game"""
guessed_coords = []
opponent_guessed_coords = []
player_ship_coords = []
opponent_ship_coords = []

def print_board(b):
    """str[][]->Nonetype
    prints a formatted version of the game board"""
    n = 1
    
    print('    A B C D E F G H I')
    print('    -----------------')

    for x in b:
        print(n, '|', *x)
        n += 1
    print('                      ')

def  add_singles(board,coords):
    """str[][],int[]->str[][]
    adds ships that take up a single space"""
    for i in range(4):
        shiprow = random.randint(0,8)
        shipcol = random.randint(0,8)
        
        while board[shiprow][shipcol] != ' ':
            shiprow = random.randint(0,8)
            shipcol = random.randint(0,8)
            
        board[shiprow][shipcol] = 'x'
        coords.append([shiprow,shipcol])#adds the used coords to the a list 
    
    return board

def  add_double(board,coords):
    """str[][],int[]->str[][]
    adds ships that take up a two spaces"""
    orientation = random.randint(0,1)

    if orientation == 0:
        for i in range(3):
            shiprow = random.randint(0,7)
            shipcol = random.randint(0,7)
            while board[shiprow][shipcol] != ' ' or board[shiprow][shipcol+1] != ' ':
                shiprow = random.randint(0,7)
                shipcol = random.randint(0,7)
            board[shiprow][shipcol] = 'x'
            board[shiprow][shipcol+1] = 'x'
            coords.append([shiprow,shipcol])#adds the used coords to the a list
            coords.append([shiprow,shipcol+1])#adds the used coords to the a list
        return board
    else:
        for i in range(3):
            shiprow = random.randint(0,7)
            shipcol = random.randint(0,7)
            while board[shiprow][shipcol] != ' ' or board[shiprow+1][shipcol] != ' ':
                shiprow = random.randint(0,7)
                shipcol = random.randint(0,7)
            board[shiprow][shipcol] = 'x'
            board[shiprow+1][shipcol] = 'x'
            coords.append([shiprow,shipcol])#adds the used coords to the a list
            coords.append([shiprow+1,shipcol])#adds the used coords to the a list
        return board

def  add_triple(board,coords):
    """str[][],int[]->str[][]
    adds ships that take up three spaces"""
    orientation = random.randint(0,1)

    if orientation == 0:
        for i in range(2):
            shiprow = random.randint(0,6)
            shipcol = random.randint(0,6)
            while board[shiprow][shipcol] != ' ' or board[shiprow][shipcol+1] != ' ' or board[shiprow][shipcol+2] != ' ':
                shiprow = random.randint(0,6)
                shipcol = random.randint(0,6)
            board[shiprow][shipcol] = 'x'
            board[shiprow][shipcol+1] = 'x'
            board[shiprow][shipcol+2] = 'x'
            coords.append([shiprow,shipcol])#adds the used coords to the a list
            coords.append([shiprow,shipcol+1])#adds the used coords to the a list
            coords.append([shiprow,shipcol+2])#adds the used coords to the a list
        return board
    else:
        for i in range(2):
            shiprow = random.randint(0,6)
            shipcol = random.randint(0,6)
            while board[shiprow][shipcol] != ' ' or board[shiprow+1][shipcol] != ' ' or board[shiprow+2][shipcol] != ' ':
                shiprow = random.randint(0,6)
                shipcol = random.randint(0,6)
            board[shiprow][shipcol] = 'x'
            board[shiprow+1][shipcol] = 'x'
            board[shiprow+2][shipcol] = 'x'
            coords.append([shiprow,shipcol])#adds the used coords to the a list
            coords.append([shiprow+1,shipcol])#adds the used coords to the a list
            coords.append([shiprow+2,shipcol])#adds the used coords to the a list
        return board


def guess_ship(board,guessed_coords):
    """str[][],int[]->int,int
    translates a players input column from letter to number and an input row is subtracted by one"""
    ltr2num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    column = input('Guess a column between A-I: ').upper()
    while column not in 'ABCDEFGHIJ' or len(column) != 1:
        column = input("Invaild guess, please enter a valid column\n").upper()
    row = input('Guess a row between 1-9: ')
    while row not in '123456789' or len(row) != 1:
        row = input("Invaild guess, please enter a valid row\n")
    if [int(row)-1,ltr2num[column]] in guessed_coords:
        print('Coords have already been chosen, try again\n')
        guess_ship(board,guessed_coords)#reruns fuction if the guess is already made
    else:
        return int(row)-1,ltr2num[column]
    return int(row)-1,ltr2num[column]

def opponent_random_guess(opp_guessed):
    """int[]->int,int
    allows the computer to randomly select a coordinate"""
    row = random.randint(0,8)
    column = random.randint(0,8)
    
    if[row,column] in opp_guessed:
        opponent_random_guess(opp_guessed)#reruns code if the coords are already used
    else:
        return row,column
    return row,column

def update_board(board,guess_board,opp_board,opp_guess,guessed_coords,opp_guessed_coords):
    """str[][],str[][],str[][],str[][],int[],int[]-> Nonetype
      """
    row,column = guess_ship(board,guessed_coords)
    print('                         ')
    print('       Game Status')
    print('-------------------------')
    if board[row][column] == 'x':
        guess_board[row][column] = 'x'
        print('     You Got A Hit!!\n')
    else:
        guess_board[row][column] = '0'
        print('     You Missed :(\n')
    guessed_coords.append([row,column])#adds the used coords to the a list
    opp_row,opp_col = opponent_random_guess(opponent_guessed_coords)
    if opp_board[opp_row][opp_col] == 'x':
        opp_guess[opp_row][opp_col] = 'x'
        print('     OH NO Your Opponent Got A Hit\n')
    else:
        opponent_guess_board[opp_row][opp_col] = '0'
        print('     Your Opponent Missed :(\n') 
    opp_guessed_coords.append([opp_row,opp_col])#adds the used coords to the a list
    print('Used Guesses:',guessed_coords,'\n')
    


def check_game_status(guesses,ships):
    """int[int[]],int[int[]]->bool
    verfiies if all the values in the ship list are within the guesses"""
    for x in guesses:
        if x in ships:
            gameover = True
        else:
            gameover = False
        return gameover



def run_game(hidden_board,guess_board,opp_board,opp_guess):
    """str[][],str[][],str[][],str[][]->Nonetype
    Runs the fgame all necessary functions to add values to the game boards,
    prints out a message depending on how the game end"""
    
    add_singles(player_board,player_ship_coords)
    add_double(player_board,player_ship_coords)
    add_triple(player_board,player_ship_coords)
    add_singles(opponent_board,opponent_ship_coords)
    add_double(opponent_board,opponent_ship_coords)
    add_triple(opponent_board,opponent_ship_coords)
    print('                        ')
    print('Welcome to BattleShip!')
    print('                     ')
    print('Take Your First Guess!!!')
    print('                     ')
    print('       Your Ships\n')
    print_board(opp_board)
    #print_board(player_board)
    print('      Your Guesses\n')
    print_board(guess_board)
    count_rounds = 1
    check_player_progress = False
    check_computer_progress = False
    while check_player_progress != True and check_computer_progress != True:
        print('              ')
        print('              ')
        print('              ')
        print('       Round: ',count_rounds)
        update_board(hidden_board,guess_board,opp_board,opp_guess,guessed_coords,opponent_guessed_coords)
        print('      Your Guesses\n')
        print_board(guess_board)
        print('   Opponents Guesses\n')
        print_board(opp_guess)
        print('key: 0 = miss, x = hit')
        count_rounds+=1
        check_player_progress = check_game_status(guessed_coords,player_ship_coords)
        check_computer_progress = check_game_status(opp_guess,opponent_guessed_coords)
    if check_game_status(guessed_coords,player_ship_coords) == True :
        print('CONGRATS YOU WIN!!!!')
    else:
        print('your ship has sunk, better luck next time -__-')


run_game(player_board,player_guess_board,opponent_board,opponent_guess_board)