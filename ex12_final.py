from tkinter import *
import boggle_board_randomizer
import tkinter.messagebox
import os
import winsound

FILEPATH = 'boggle_dict.txt'
BOARD_SIZE = 4
WELCOME_AND_INSTRUCTIONS_MSG_TITLE = "Welcome"
WELCOME_AND_INSTRUCTIONS_MSG = "Hello and Welcome to Boggle game! a few words about this game: " \
                               "The goal of the game is to find as many words as possible on the " \
                               "board in 3 minutes. A valid word is a word that appears in the " \
                               "dictionary and consists of a trip on the board that starts with " \
                               "one of the letters and moves to neighboring letters. A neighboring " \
                               "letter is considered to be a letter that is adjacent to the current " \
                               "letter in one of the eight directions (up, down, right, " \
                               "left or one of the four diagonals). SO! Let's play Boggle!"
TIMES_UP_MSG_TITLE = "OH OH!"
TIMES_UP_MSG = "Time's up! would you like to play again?"
QUIT_MSG_TITLE = "Quit"
QUIT_MSG = "Are you sure you want to quit?"
BACKGROUND_COLOR = 'black'
root = Tk()

root.geometry('1350x700')
root.configure(background="gray31")


class Splash(Toplevel):
    """
    Welcome message
    """

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title("")
        self.update()


class StartingScreen(Tk):
    """
    """

    def __init__(self):
        Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)
        tkinter.messagebox.showinfo(WELCOME_AND_INSTRUCTIONS_MSG_TITLE, WELCOME_AND_INSTRUCTIONS_MSG)
        splash.destroy()


##################################################### Game ########################################################

class Boogle:
    """
    """

    def __init__(self, master):

        photo = PhotoImage(file="boggle.png")
        label = Label(master, image=photo)
        label.image = photo
        label.grid(row=0, column=0, columnspan=20, rowspan=20)

        self.background = Frame(master)
        self.background.grid()

        self.empty_frame = Frame(master, bg=BACKGROUND_COLOR, width=200, height=600)
        self.empty_frame.grid(row=0, column=0)

        self.board_frame = Frame(master, bg=BACKGROUND_COLOR, width=440, height=800)
        self.board_frame.grid(row=0, column=1)

        self.score_frame = Frame(master, bd=20, bg=BACKGROUND_COLOR, width=80, height=80)
        self.score_frame.place(x=872, y=70)


        ############################################################### board frame ##############################################################################################

        self.timer_frame = Frame(self.board_frame, bd=20, bg=BACKGROUND_COLOR, width=100, height=100)
        self.timer_frame.grid(row=0, column=0)

        self.screen_frame = Frame(self.board_frame)
        self.screen_frame.grid(row=1, column=0)

        self.letters_frame = Frame(self.board_frame, bd=20, bg=BACKGROUND_COLOR, width=600, height=600)
        self.letters_frame.grid(row=2, column=0)

        self.empty_space = Frame(self.board_frame, bd=20, bg=BACKGROUND_COLOR, width=440, height=30)
        self.empty_space.grid(row=3, column=0)

        self.submit_frame = Frame(self.board_frame, bd=20, bg=BACKGROUND_COLOR, width=90, height=50)
        self.submit_frame.grid(row=4, column=0)



        ################################################ empty_side  ##########################################################################

        self.empty_space1 = Frame(self.empty_frame, bd=20, bg=BACKGROUND_COLOR, width=120, height=50)
        self.empty_space1.grid(row=0, column=0)

        self.end_game_menu = Frame(self.empty_frame, bd=20, bg=BACKGROUND_COLOR, width=50, height=100)
        self.end_game_menu.place(x=0, y=0)

        ###################################################################### variavle################################################

        self.coor_list = list()
        self.board = boggle_board_randomizer.randomize_board()
        self.board_dict = convert_to_dict(self.board)
        self.screen_input = StringVar()
        self.word_list = words_list(FILEPATH)
        self.score_output = IntVar()
        self.score_output.set(0)
        self.used_word_list = []
        self.num_of_word = 0

        ###################################################################### objects ###############################################

        self.scroll = ScrollBar()
        self.screen = Screen(self.screen_frame, self.screen_input)
        self.score = Score(self.score_frame, self.score_output)
        self.exit_button = Button(self.end_game_menu, text='Quit', font='Courier 15', command=self.quit_game)
        self.exit_button.grid(row=1, column=0, sticky=N)
        self.submit_button = Button(self.submit_frame, text='Submit', font='Courier 15', command=self.end_of_word)
        self.submit_button.place(x=-15, y=-15)
        # initiates the board
        for col in range(BOARD_SIZE):
            for row in range(BOARD_SIZE):
                if os.name == 'nt':
                    button = Button(self.letters_frame, text=self.board_dict[(col, row)], fg='red', font='Courier', width=2,
                                    height=2, command=lambda x=col, y=row: self.button_clicked(x, y))
                else:
                    button = Button(self.letters_frame, text=self.board_dict[(col, row)], fg='red', font='Courier',
                                    width=9,
                                    height=7, command=lambda x=col, y=row: self.button_clicked(x, y))
                button.grid(row=col, column=row)
        ############################################################ Timer ##################################################

        self.label = Label(self.timer_frame, bg='mint cream', font='Courier 40')
        self.label.place(x=-10, y=15)
        self.countdown(180)

    #######################################################################################################################

    def time_is_up(self):
        """
        :return:
        """
        user_answer = tkinter.messagebox.askquestion(TIMES_UP_MSG_TITLE, TIMES_UP_MSG)
        if user_answer == 'yes':
            Boogle(root)
        else:
            quit()

    def quit_game(self):
        """
        :return:
        """
        user_answer = tkinter.messagebox.askquestion(QUIT_MSG_TITLE, QUIT_MSG)
        if user_answer == 'yes':
            quit()
        else:
            pass

    def countdown(self, count):
        """
        Timer for game - checks if 180 sec passed
        :param count:
        :return:
        """
        self.label['text'] = count

        if count > 0:
            self.timer_frame.after(1000, self.countdown, count - 1)
        else:
            self.time_is_up()

    def end_of_word(self):
        """
        :return:
        """
        word = convert_to_word(self.coor_list, self.board_dict)
        if check_word(word, self.used_word_list):
            if word in self.word_list:
                self.screen.right_answer()
                score_temp = self.score_output.get() + calculate_score(word)
                self.score_output.set(score_temp)
                self.used_word_list.append(word)
                self.scroll.add_word(word)
                self.coor_list.clear()
                return
            else:
                self.not_valid()
        else:
            self.not_valid()

        self.coor_list.clear()

    def not_valid(self):
        """
        :return:
        """
        self.screen.not_valid()
        self.coor_list.clear()

    def button_clicked(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        self.coor_list.append((x, y))
        self.add_letter(self.coor_list)
        if not check_if_valid(self.coor_list):  # here we can do some sign
            self.not_valid()

    def add_letter(self, coor_list):
        """
        :param coor_list:
        :return:
        """
        if len(coor_list) == 1:
            self.screen.new_word()
        display = ""
        for word in coor_list:
            display = display + self.board_dict[word]
        self.screen_input.set(display)


class ScrollBar:
    def __init__(self):
        table_frame = Frame(bd=30, bg='black', width=20, height=100)
        table_frame.place(x=800, y=130)
        self.table = Scrollbar(table_frame)
        self.table.pack(side=RIGHT, fill=Y)
        self.list_of_words = Listbox(table_frame, yscrollcommand=self.table.set, bg='white', bd=20, width=10, height=10,
                                     font='helvetica 15')
        self.num_of_word = 0
        for i in range(100):
            self.list_of_words.insert(END, '' + str(i + 1))

        self.list_of_words.pack(side=LEFT)
        self.table.config(command=self.list_of_words.yview)

    def add_word(self, word):
        self.list_of_words.delete(self.num_of_word)
        self.list_of_words.insert(self.num_of_word, '' + str(self.num_of_word + 1) + ' ' + word)
        self.num_of_word = self.num_of_word + 1


class Screen:
    def __init__(self, master, screen_input):
        self.bg = 'powder blue'
        self.text_display = Label(master, font='david 20', textvariable=screen_input,
                                  bg='white', justify='center')
        self.text_display.grid()

    def right_answer(self):
        if os.name == 'nt':
            winsound.PlaySound('sweet-notification-alert_C#_major.wav',winsound.SND_ASYNC)
        # Available only for Windows users
        self.text_display.config(bg='green')

    def not_valid(self):
        if os.name == 'nt':
            winsound.PlaySound('wrong-answer_F#_major.wav', winsound.SND_ASYNC)
        # Available only for Windows users
        self.text_display.config(bg='red')

    def new_word(self):
        self.text_display.config(bg='white')


class Score:
    """
    """

    def __init__(self, master, score):
        self.score = score
        score_frame = Label(master, textvariable=self.score, bg='white', font='Times 25')
        score_frame.pack()

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score


def words_list(file):
    """
    Creates a list of words from boggle_dict.txt file
    :param file: boggle_dict.txt
    :return: list of the words
    """
    with open(file) as boogle_dict:
        words = []
        for line in boogle_dict:
            words.append(line.strip())
        return words


def convert_input_to_coor_lst(input):
    """
    Converts chosen latter to coordinate in order to keep on valid moves
    (according to game rules)
    :param input: string
    :return: list of coordinates
    """
    lst = list()
    for i in range(0, len(input), 2):
        lst.append((int(input[i]), int(input[i + 1])))
    return lst


def convert_to_word(user_input, dict_board):
    """
    :param user_input:
    :param dict_board:
    :return:
    """
    word = ''
    for coor in user_input:
        word = word + dict_board[coor]
    # word = ''.join(str(i) for i in lst)

    return word


def convert_to_dict(board):
    """
    :param board:
    :return:
    """
    coor_lst = [(i, j) for i in range(4) for j in range(4)]
    coor_lst = [coor_lst[x:x + 4] for x in range(0, len(coor_lst), 4)]
    dict_letter_coor = {}
    for i in range(4):
        for j in range(4):
            if board [i][j] == 'Qu':
                board[i][j] = 'QU'
            dict_letter_coor[coor_lst[i][j]] = board[i][j]
    return dict_letter_coor


def check_if_valid(coor_lst):
    """
    Checks if users move is valid according to game rules
    :param coor_lst: list of coordinates that equal to letters
    :return: True if move is valid, False if not
    """
    if len(coor_lst) < 2:
        return True
    if compare_last(coor_lst[-1], coor_lst[-2]) == 1:
        if len(coor_lst) == len(set(coor_lst)):
            return True
        else:
            return False
    else:
        return False


def compare_last(last_coor, before_last):
    """
    :param last_coor:
    :param before_last:
    :return:
    """
    if abs(last_coor[0] - before_last[0]) <= 1 and abs(last_coor[1] - before_last[1]) <= 1:
        return True
    else:
        return False


def check_word(word, used_word_list):
    """
    Checks if user already found the word he just found, in order
    to avoid repetition
    :param word: current word
    :param used_word_list: list of word he already found
    :return: True if word isn't used before, False if yes
    """
    if word in used_word_list:
        return False
    return True


def calculate_score(word):
    """
    Calculates points for each word according to game rules
    :param word: word in string
    :return: points
    """
    amount = len(word) ** 2
    return amount


def number_of_words(used_word_list):
    """
    Counts how many words user found
    :param used_word_list: list of the words he found
    :return: the number of the words he found
    """
    return len(used_word_list)


StartingScreen()
Boogle(root)
root.mainloop()



