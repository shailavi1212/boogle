import sys
import boggle_board_randomizer
import time
import Graphics

START_MSG = "Let's play Boogle!"
SEC_MSG = "Great job! keep going :)"
LOS_MSG = "There is no word like this, try again"
QUIT_MSG = "Thanks for playing! hope to see you soon"
BOARD_SIZE = 4
FILEPATH = ()

def main():
    board = boggle_board_randomizer.randomize_board()
    dict_board = convert_to_coor(board)
    word_list = words_list(FILEPATH)
    used_list = []
    score = 0
    coor_input = input() # list of coor
    word_input = convert_to_word(user_input,dict_board)
    seconds = time.time()
    while seconds:
        if check_if_valid(coor_input):
            if check_word(word, used_word_list):
                if word in word_list:
                    score += cauculate_score(score, word)
                    used_list.append(word)
                    print(SEC_MSG)
                else:
                    print(LOS_MSG)
            else:
                print("You already found this word")
        else:
            print("Invalid move")
    print("Finish msg + score")
    play_again = input("Would you like to play again?")
    if play_again == "Y":
        main()
    else:
        print(QUIT_MSG)
        quit()

def words_list(file):
    with open(file) as boogle_dict:
        words = []
        for line in boogle_dict:
            words.append(line.strip())
        return words

def convert_to_word(user_input,dict_board):
    word = ''
    for coor in user_input():
        word = word + dict_board[coor]
    return word

def convert_to_dict(board):
    coor_lst = [(i, j) for i in range(4) for j in range(4)]
    coor_lst = [coor_lst[x:x + 4] for x in range(0, len(coor_lst), 4)]
    dict_letter_coor = {}
    for i in range(4):
        for j in range(4):
            dict_letter_coor[coor_lst[i][j]] = self.board[i][j]
    return dict_letter_coor

def check_if_valid(coor_lst):

    if len(coor_lst) == len(set(coor_lst)):
        return True
    else:
        return False

def check_word(word, used_word_list):
    # make sure word is on the board
    # make sure word is in the dictionary
    if word in used_word_list:
        return False
    return True

def calculate_score(word):
    amount = len(word) ** 2
    return amount

def number_of_words(used_word_list):
    return len(used_word_list)

if __name__ == '__main__':
    main()



