'''
Created on Sep 17, 2021

@author: gulma
'''
'''1. Create a dictionary by assigning ' ' to the cells of the board.
   2. Create a function for printing the border of the board
   3. Write the body of the program
   
'''

board={   '7':' ', '8':' ', '9': ' ' ,
          '4':' ', '5':' ', '6': ' ',
          '1':' ', '2':' ', '3': ' '
          }
boardKeys=[]

print("Below are the positions of the keys on the board: ")
print("\n7 8 9")
print("4 5 6")
print("1 2 3\n")

for key in board:
    boardKeys.append(key)


def printBorder(board):
    
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def ticTacToe():
    gameTurn='X'
    cnt=0
    for k in range(1000): 
        print("It is turn of "+gameTurn+". Please specify the position you want to play: ")
        printBorder(board) #empty board
        position=input() # a number between 1 and 9
        while position=='':
            position=input()
        if board[position]==' ':
            board[position]=gameTurn
            cnt=cnt+1
        else:
            print("Sorry, this place is not empty! Please choose another cell!")
            continue
        if cnt>=5:
            if board['7']==board['8']==board['9']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")
                break
            if board['4']==board['5']==board['6']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")
                break
            if board['7']==board['4']==board['1']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")   
                break
            if board['8']==board['5']==board['2']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(+gameTurn+" won the game!")   
                break
            if board['9']==board['6']==board['3']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")   
                break
            if board['1']==board['5']==board['9']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")   
                break
            if board['3']==board['5']==board['7']!=' ':
                printBorder(board)
                print("\nGame over!\n")
                print(gameTurn+" won the game!")   
                break
                
        if cnt==9:
            print("\nGame over!\n")
            print("\nNo one won! It is a tie!\n")
            break;
        if gameTurn=="X":
            gameTurn="O"
        else:
            gameTurn="X"
    restart=input("\nDo you want to restart the game: ")
    print("\n")
    if restart.lower()=="yes":
        for key in boardKeys:
            board[key]=' '
        ticTacToe()
if __name__=="__main__":
    ticTacToe()