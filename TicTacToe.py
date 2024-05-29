import random
import sys

def initialize_game():
    turn_count = 0
    global available_tiles
    available_tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("Welcome to Tic-Tac-Toe")
    num_players, player_names = number_of_players()
    print(initialize_board())
    if num_players == 1:
        print("Single-player mode")
    elif num_players == 2:
        print("Two player mode")
    print('{} is X. {} is O.'.format(player_names[0], player_names[1]))
    gameplay(num_players, turn_count, player_names[0], player_names[1])

def number_of_players():
    num_players = input("Will you be playing with 1 human or 2?\n")
    valid_number = False
    while valid_number == False:
        if num_players == "1":
            player_names = one_player()
            valid_number = True
        elif num_players == "2":
            player_names = two_player()
            valid_number = True
        else:
            num_players = input("Please enter the number 1 or 2\n")
    return int(num_players), player_names

def one_player():
    print("Starting game with 1 human player\n")
    ai_name = "Computer"
    player_name = input("Enter your name or press enter to default to 'Player'\n")
    if player_name == "":
        player_name = "Player"
    return [player_name, ai_name]

def two_player():
    print("Starting game with 2 human players\n")
    p1_name = input("Enter player 1's name or press enter to default to 'Player 1'\n")
    if p1_name == "":
        p1_name = "Player 1"
    p2_name = input("Enter player 2's name or press enter to default to 'Player 2'\n")
    if p2_name == "":
        p2_name = "Player 2"
    return[p1_name, p2_name]

def initialize_board():
    global gameboard
    gameboard = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
    grid = (" " + gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + " \n" +
          "___________\n" +
          " " + gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + " \n" +
          "___________\n" +
          " " + gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] + " \n")
    return(grid)

def update_board():
    grid = (" " + gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + " \n" +
          "___________\n" +
          " " + gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + " \n" +
          "___________\n" +
          " " + gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] + " \n")
    return(grid)

def player_turn(turn_count):
    player_move = input("Chose which grid tile (1-9) to place in\n")
    valid_tile = False
    while valid_tile == False:
        if player_move in available_tiles:
            player_move_int = int(player_move) - 1
            if turn_count%2 == 1:
                gameboard[player_move_int] = "X"
                available_tiles.remove(player_move)
                valid_tile = True
            elif turn_count%2 == 0:
                gameboard[player_move_int] = "O"
                available_tiles.remove(player_move)
                valid_tile = True
        else:
            print("Please pick a valid tile space to play in. Available tiles:\n")
            player_move = input(available_tiles)

def ai_turn(turn_count):
    ai_move = random.choice(available_tiles)
    ai_move_int = int(ai_move) - 1
    gameboard[ai_move_int] = "O"
    available_tiles.remove(ai_move)
    turn_count += 1
    return(turn_count)
    
def win_con_check():
    if gameboard[0] == gameboard[1] == gameboard[2]:
        return(gameboard[0])
    elif gameboard[2] == gameboard[5] == gameboard[8]:
        return(gameboard[2])
    elif gameboard[6] == gameboard[7] == gameboard[8]:
        return(gameboard[6])
    elif gameboard[0] == gameboard[3] == gameboard[6]:
        return(gameboard[0])
    elif gameboard[1] == gameboard[4] == gameboard[7]:
        return(gameboard[1])
    elif gameboard[3] == gameboard[4] == gameboard[5]:
        return(gameboard[3])
    elif gameboard[0] == gameboard[4] == gameboard[8]:
        return(gameboard[0])
    elif gameboard[2] == gameboard[4] == gameboard[6]:
        return(gameboard[2])
    else:
        return("No winner")
    
def game_over_check(turn_count, win_con_check_var, player1_name, player2_name):
    if win_con_check_var == "X":
        print("{} has won!".format(player1_name))
        game_over_bool = True
    elif win_con_check_var == "O":
        print("{} has won!".format(player2_name))
        game_over_bool = True
    elif (win_con_check_var == "No winner" and turn_count == 9):
        print("The game is a tie.")
        game_over_bool = True
    else:
        game_over_bool = False
    return(game_over_bool)

def gameplay(num_players, turn_count, player1_name = None, player2_name = None):
    game_over_bool = False
    if game_over_bool == False:
        if num_players == 1:
            while game_over_bool == False:
                turn_count += 1
                player_turn(turn_count)
                print(update_board())
                win_con_check_var = win_con_check()
                game_over_bool = game_over_check(turn_count, win_con_check_var, player1_name, player2_name) 
                if game_over_bool == False:
                    turn_count = ai_turn(turn_count)
                    print(update_board())
                    win_con_check_var = win_con_check()
                    game_over_bool = game_over_check(turn_count, win_con_check_var, player1_name, player2_name)
        elif num_players == 2:
            while game_over_bool == False:
                turn_count += 1
                player_turn(turn_count)
                print(update_board())
                win_con_check_var = win_con_check()
                game_over_bool = game_over_check(turn_count, win_con_check_var, player1_name, player2_name)
        else:
            raise ValueError("Something went wrong with player number validation")
    if game_over_bool == True:
        play_again = input("Type Y to play again or anything else to quit\n")
        if play_again.capitalize() == "Y":
            initialize_game()
        else:
            print(play_again)
            sys.exit("Thanks for playing!")

if __name__ == "__main__":
    initialize_game()