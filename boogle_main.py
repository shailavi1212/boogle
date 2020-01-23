import sys
import boggle_board_randomizer
import time

START_MSG = "Let's play Boogle!"
SEC_MSG = "Great job! keep going :)"
LOS_MSG = "There is no word like this, try again"
QUIT_MSG = "Thanks for playing! hope to see you soon"
BOARD_SIZE = 4
FILEPATH = 'boggle_dict.txt'

def main():
    """"""
    board = boggle_board_randomizer.randomize_board()
    dict_board = convert_to_dict(board)
    word_list = words_list(FILEPATH)
    used_word_list = []
    score = 0
    coor_input = input() # list of coor
    coor_input = convert_input_to_coor_lst(coor_input)
    word = convert_to_word(coor_input,dict_board)
    start = time.time()

    while time.time() - start < 30:
        if check_if_valid(coor_input):
            if check_word(word, used_word_list):
                if word in word_list:
                    score += calculate_score(word)
                    used_word_list.append(word)
                    print(SEC_MSG)
                else:
                    print(LOS_MSG)
            else:
                print("You already found this word")
        else:
            print("Invalid move")
        coor_input = input("Insert again: ")
        coor_input = convert_input_to_coor_lst(coor_input)
    print("Finish msg + score")
    play_again = input("Would you like to play again?")
    if play_again == "Y":
        main()
    else:
        print(QUIT_MSG)
        quit()

def words_list(file):
    """"""
    with open(file) as boogle_dict:
        words = []
        for line in boogle_dict:
            words.append(line.strip())
        return words

def convert_input_to_coor_lst(input):
    """"""
    lst = list()
    for i in range(0,len(input),2):
        lst.append((int(input[i]),int(input[i+1])))
    return lst

def convert_to_word(user_input,dict_board):
    """"""
    word = ''
    print(user_input)
    for coor in user_input:
        word = word + dict_board[coor]
    #word = ''.join(str(i) for i in lst)

    return word

def convert_to_dict(board):
    """"""
    coor_lst = [(i, j) for i in range(4) for j in range(4)]
    coor_lst = [coor_lst[x:x + 4] for x in range(0, len(coor_lst), 4)]
    dict_letter_coor = {}
    for i in range(4):
        for j in range(4):
            dict_letter_coor[coor_lst[i][j]] = board[i][j]
    return dict_letter_coor

def check_if_valid(coor_lst):
    """"""
    if compare_last(coor_lst[-1],coor_lst[-2]):
        if len(coor_lst) == len(set(coor_lst)):
            return True
    else:
        return False
def compare_last(last_coor,before_last):
    if abs(last_coor[0] - before_last[0]) <= 1 and abs(last_coor[1] - before_last[1]) <= 1:
        return True
    else:
        return False

def check_word(word, used_word_list):
    """"""
    if word in used_word_list:
        return False
    return True

def calculate_score(word):
    """"""
    amount = len(word) ** 2
    return amount

def number_of_words(used_word_list):
    """"""
    return len(used_word_list)

if __name__ == '__main__':
    main()