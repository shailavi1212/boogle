import sys
import boggle_board_randomizer
import time
from tkinter import *

START_MSG = "Let's play Boogle!"
SEC_MSG = "Great job! keep going :)"
LOS_MSG = "There is no word like this, try again"
QUIT_MSG = "Thanks for playing! hope to see you soon"
BOARD_SIZE = 4
FILEPATH = 'boggle_dict.txt'
class Loading_game():
    def __init__(self,master):
        self.photo = PhotoImage(file = 'opening_loading.gif')
        self.label = Label(master, image = self.photo)
        self.label.grid()


class Scroll_bar():
    def __init__(self,master):
        table_frame = Frame(master, bd=100, bg='blue', width=100, height=600)
        table_frame.grid(row=0, column=3)
        self.table = Scrollbar(table_frame)
        self.table.pack(side=RIGHT, fill=Y)
        self.list_of_words = Listbox(table_frame, yscrollcommand = self.table.set,bg = 'grey',bd = 20,width = 20,height= 20,font = 'helvetica 15')
        self.num_of_word = 0
        for i in range(100):
            self.list_of_words.insert(END, '' + str(i + 1))
        self.list_of_words.pack(side=LEFT)
        self.table.config(command=self.list_of_words.yview)


    def add_word(self,word):
        self.list_of_words.delete(self.num_of_word)
        self.list_of_words.insert(self.num_of_word,'' + str(self.num_of_word + 1) + ' ' + word)
        self.num_of_word = + 1

class Screen():
    def __init__(self, master,screen_input):

        self.text_display = Entry(master, font='ariel 20', textvariable=screen_input, insertwidth=40,
                                    bg='powder blue', justify='center')
        self.text_display.grid()
    def right_answer(self):
        self.text_display.after(0,self.text_display.config(bg='green'))

    def after(self,time):
        self.text_display.after(time, self.text_display.config(bg='powder blue'))
class Score():
    def __init__(self,master,score):
        self.score = score
        score_frame = Label(master, textvariable = score, bg='white', font='ariel 25')
        score_frame.place(x=40, y=50)
    def get_score(self):
        return self.score
    def set_score(self,new_score):
        self.score = new_score
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
    if len(coor_lst) < 2:
        return True
    if compare_last(coor_lst[-1],coor_lst[-2]) == 1:
        if len(coor_lst) == len(set(coor_lst)):
            return True
        else:
            return False
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