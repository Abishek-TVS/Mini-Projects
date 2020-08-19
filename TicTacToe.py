from IPython.display import clear_output

def Printboard(Board_stat_list):
    
    clear_output()
    
    print ('Tic Tac Toe Board\n')
    
    for i in range(0,(len(Board_stat_list)),3):
        
        print ('   '+Board_stat_list[i]+' | '+Board_stat_list[i+1]+' | '+Board_stat_list[i+2])
        if i<6:
            print ('  ---+---+---')
     
    
    #print (' '+Board_stat_list[1]+' | '+Board_stat_list[2]+' | '+Board_stat_list[3])
    #print ('---+---+---')
    #print (' '+Board_stat_list[4]+' | '+Board_stat_list[5]+' | '+Board_stat_list[6])
    #print ('---+---+---')
    #print (' '+Board_stat_list[7]+' | '+Board_stat_list[8]+' | '+Board_stat_list[9])
    #Board_stat_list=['x','o','s','x',' ','6',' ','x','x'] 
    #Board_stat_list = [' ']*9
    #Printboard(Board_stat_list)


def player_symbol():
    
    player_1 = ('')
    
    # allow player 1 to choose X or O
    
    while player_1 != 'x' and player_1 != 'o':
        
        player_1 = (input ('Player 1, Choose either X or O : ')).lower()
    
    if player_1 == 'x':
        player_1 = 'x'
        player_2 = 'o'
    else:
        player_2 = 'x'
    
    return (player_1, player_2)
    
#player_symbol()


def place_marker(Board_stat_list,position,symbol):
    
    Board_stat_list[position-1] = symbol

#place_marker(Board_stat_list,1,'x')


def win_check(Board_stat_list,mark):
    
   
    for i in [0,3,6]:
    
        a=(Board_stat_list[i]+Board_stat_list[i+1]+Board_stat_list[i+2])
        if a == mark+mark+mark:
            return True
    
    for i in [6,7,8]:
        
        b=(Board_stat_list[i]+Board_stat_list[i-3]+Board_stat_list[i-6])
        if b == mark+mark+mark:
            return True
    
    
    return (Board_stat_list[2]+Board_stat_list[4]+Board_stat_list[6])== mark+mark+mark or (Board_stat_list[0]+Board_stat_list[4]+Board_stat_list[8])== mark+mark+mark
         

import random

def choose_first():
    
    Random = random.randint(0,100)
    if Random >= 50:
        return "player 1"
    else:
        return "player 1"

#choose_first()


def space_check(Board_stat_list , position):
    
    return Board_stat_list[position]==' '
        
#space_check(Board_stat_list , 8)


def full_board_check(Board_stat_list):
    
    for i in range(len(Board_stat_list)):
        if space_check(Board_stat_list , i):
            return False

    else:
        return True

#full_board_check(Board_stat_list)


def player_position_choice (Board_stat_list):
    
    '''    
    mark = (input('  Enter a position number (1-9) to mark your symbol : '))
    
    if mark not in [int(i) for i in list(range(1,10))] :
        print (' \n  Wrong input\n  Enter the value between (1-9) ')
        player_position_choice(Board_stat_list)
    else:
        if space_check(Board_stat_list , mark):
            print('j')
        else:
            player_position_choice(Board_stat_list)

    if mark in ('1','2','3','4','5','6','7','8','9') :
        if space_check(Board_stat_list ,int(mark)-1 ):
            return int(mark)
        else:
            player_position_choice(Board_stat_list)
    else:
        print (' \n  Wrong input\n  Enter the value between (1-9) ')
        player_position_choice(Board_stat_list)
    '''        

    while True:
        position = (input('Choose your next position: (1-9)'))
        try:
            isinstance(position,int)
        except:
            continue
        else:
            if 1 <= int(position) <= 9:
                if space_check(Board_stat_list, int(position)-1):
                    return int(position)

#player_position_choice(Board_stat_list)


# In[9]:


def replay():
    
    grab_input = input(' Do you wish to play game? yes or no? : ').lower()
    
    replay_info = ['yes','y','no','n']
    
    if  grab_input in replay_info[:2]:
        return True
        
    elif grab_input in replay_info[2:]:
        return False
        
    else:
        replay()

#replay()


print (' Welcome to Tic Tac Toe \n Enjoy the game\n  ')


while True :
    #Reset Board
    Board_stat_list = [' ']*9

    symbol_player1, symbol_player2 = player_symbol()
    turn = choose_first()
    print(turn + ' will go first.')
    
    # To enter game loop
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'player 1':
            Printboard (Board_stat_list)
            po = player_position_choice(Board_stat_list)
            place_marker(Board_stat_list, po, symbol_player1)
            
            if win_check(Board_stat_list, symbol_player1):
                Printboard(Board_stat_list)
                print('\nCongratulations! Player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(Board_stat_list):
                    Printboard(Board_stat_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 2'

        else:
            # Player2's turn.
            
            Printboard(Board_stat_list)
            po = player_position_choice(Board_stat_list)
            place_marker(Board_stat_list, po, symbol_player2)

            if win_check(Board_stat_list, symbol_player2):
                Printboard(Board_stat_list)
                print('\nPlayer 2 has won!')
                game_on = False
            else:
                if full_board_check(Board_stat_list):
                    Printboard(Board_stat_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 1'

    
    if not replay():
        break
    else:
        continue
