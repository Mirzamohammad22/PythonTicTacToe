def win_checker(box):
    '''
    Doc String:
    This function checks the win conditions of Tic Tac Toe and return the winner or None.
    Takes the Tic Tac Toe list as input
    '''

    if (box[0] == box[1] == box[2] or box[0] == box[3] == box[6] or box[0] == box[4] == box[8] ):
        return box[0]
    elif (box[0] == box[1] == box[2] or box[2] == box[4] == box[6] or box[2] == box[5] == box[8]):
        return box[2]
    elif (box[1] == box[4] == box[7] or box[3] == box[4] == box[5]):
        return box[4]
    else:
        return None
        
        


    

def tic_tac_toe(value):
    '''
    Doc String: This function takes in the first players choice (X or O) and then 
    declares the tic tac toe list to begin.
    '''
    player1 = value.lower()
    player2 = 'o' if(player1 == 'x') else 'x'
    playerstr = 'player 1'
    win = None
    box = list(range(9))
    print(box)
    chance=1
    print("pre to while loop all clear " )
    
    while(win == None and chance < 10) :
        print(f"player {playerstr}'s turn:")
        print(box[0],'|',box[1],'|',box[2])
        print('-----------')
        print(box[3],'|',box[4],'|',box[5])
        print('-----------')
        print(box[6],'|',box[7],'|',box[8])
        position=int(input('Please enter the number for the position you want to insert your marking \n'))
        if(chance%2!=0):
            box[position] = player1
            playerstr = 'player 2'
        else:
            box[position] = player2
            playerstr = 'player 1'
        chance+=1
        win = win_checker(box)
    if(win==None):
        print('Game is a Tie')
    else:
        print('Winner is',win) 
    print(box[0],'|',box[1],'|',box[2])
    print('-----------')
    print(box[3],'|',box[4],'|',box[5])
    print('-----------')
    print(box[6],'|',box[7],'|',box[8])


def main():
    
    print("Welcome to tic tac toe")
    choice = input("Please choose X or O:")
    print('all clear with choice',choice)
    tic_tac_toe(choice)



if __name__ == "__main__":
    main()
