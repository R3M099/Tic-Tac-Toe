theBoard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}
#function to print the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
#End of print board function

#function that contains all game requirements
def game():    
    turn='X'
    c=0
    for i in range(9):
        printBoard(theBoard)
        while(True):
            print('turn for '+turn+'.Which place you want to put '+turn+':')
            move=input()
            #to check that the user does not put 'X' and 'O' in same positions
            if move not in theBoard.keys():
                print('Wrong input. Try again!')
                continue
            else:
                if theBoard[move]==' ':
                    theBoard[move]=turn
                    c+=1
                else:
                    print('That position is already filled.')
                    print('try another position:')
                    continue
            break   
        #to check for the winner of the game.
        if c>4:
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')
                break
            elif theBoard['1']==theBoard['4']==theBoard['7']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')    
                break
            elif theBoard['2']==theBoard['5']==theBoard['8']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')    
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')    
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')
                break
            elif theBoard['3']==theBoard['5']==theBoard['7']!=' ':
                printBoard(theBoard)
                print('Game Over')
                print(turn+' wins,congrats!!')
                break
        #if the game ends in a tie        
        if c==9:
            print('Game Over')
            print('The game ended in a tie.')
        #for changing the turn of players after each move
        if turn=='X':
            turn='O'
        else:           
            turn='X'      
    #to restart the game.
    board_keys=[]
    for key in theBoard:
        board_keys.append(key)
    res=input('Do you want to continue?(Y/N):')
    if res=='Y' or res=='y':
        for key in board_keys:
            theBoard[key]=" "
        game()

#main function
if __name__=="__main__":            
    game()                                                  