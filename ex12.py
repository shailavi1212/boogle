from tkinter import *
import boogle_main
import boggle_board_randomizer
import time
import winsound
import tkinter.messagebox


root = Tk()
root.geometry('1352x652+0+0')
root.configure(background = 'white' )


##################################################### commands ###################################################################


class Boogle:
    def __init__(self,master):
        self.background = Frame(master)
        self.background.grid()
        self.empty_frame = Frame(master,bg = 'white',width = 200,height= 600)
        self.empty_frame.grid(row = 0, column = 0)
        self.board_frame = Frame(master,bg = 'yellow',width = 440,height= 800 )
        self.board_frame.grid(row = 0, column = 1)

        self.score_frame =Frame(master ,bd = 20, bg = 'white',width = 80,height= 80 )
        self.score_frame.place(x = 872, y = 70)

############################################################### board frame ##############################################################################################
        self.timer_frame = Frame(self.board_frame,bd = 20,bg = 'white',width = 100,height= 100 )
        self.timer_frame.grid(row = 0, column = 0)
        self.screen_frame = Frame(self.board_frame)
        self.screen_frame.grid(row = 1, column = 0)
        self.letters_frame = Frame(self.board_frame,bd = 20,bg = 'white',width = 440,height= 400)
        self.letters_frame.grid(row = 2, column = 0)
        self.empty_space = Frame(self.board_frame,bd = 20,bg = 'white',width = 440,height= 30)
        self.empty_space.grid(row = 3, column = 0)
        self.submit_frame = Frame(self.board_frame,bd = 20,bg = 'white',width = 90,height= 50 )
        self.submit_frame.grid(row = 4, column = 0)
################################################ empty_side  ##########################################################################
        self.empty_space1 = Frame(self.empty_frame,bd = 20,width = 200,height= 500)
        self.empty_space1.grid(row = 0,column = 0)
        self.end_game_menu = Frame(self.empty_frame,bd = 20,width = 100,height= 100)
        self.end_game_menu.place(x = 0, y = 450)
###################################################################### variavle################################################
        self.coor_list = list()
        self.board = boggle_board_randomizer.randomize_board()
        self.board_dict = boogle_main.convert_to_dict(self.board)
        self.screen_input = StringVar()
        self.word_list = boogle_main.words_list(boogle_main.FILEPATH)
        self.score_output = IntVar()
        self.score_output.set(0)
        self.used_word_list = []
        self.num_of_word = 0

###################################################################### objects ###############################################
        self.scroll = boogle_main.Scroll_bar()
        self.screen = boogle_main.Screen(self.screen_frame,self.screen_input)
        self.score = boogle_main.Score(self.score_frame,self.score_output)
        self.exit_button = Button(self.end_game_menu, text='main menu', command=self.back_to_main)
        self.exit_button.grid(row=1, column=0, sticky=N)
        self.submit_button = Button(self.submit_frame, text='submit', font='david 14', command=self.end_of_word)
        self.submit_button.place(x=-10, y=-15)
        for col in range(4):
            for row in range(4):
                button = Button(self.letters_frame, text=self.board_dict[(col, row)], fg='red', width=2, height=2,
                                command=lambda x=col, y=row: self.button_clicked(x, y))
                button.grid(row=col, column=row)
        ############################################################ display #######################################################
        self.label = Label(self.timer_frame, text='30', bg='white', font='ariel 25')
        self.label.place(x=10, y=15)
        self.countdown(180)
###############################################################################################################################3
    def time_is_up(self):

        answer = tkinter.messagebox.askquestion('','would you like to play again')
        if answer == 'yes':
            pass
            #new game
        else:
            pass
            #back to main menu
    def back_to_main(self):
        pass
        #back to main menu
    def countdown(self,count):
        self.label['text'] = count

        if count > 0:
            self.timer_frame.after(1000, self.countdown, count-1)
        else:
            self.time_is_up()
    def end_of_word(self):
        word = boogle_main.convert_to_word(self.coor_list, self.board_dict)
        if boogle_main.check_word(word, self.used_word_list):
            if word in self.word_list:
                self.screen.right_answer()
                score_temp = self.score_output.get() + boogle_main.calculate_score(word)
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
        self.screen.not_valid()
        self.coor_list.clear()

    def button_clicked(self,x,y):
        self.coor_list.append((x,y))
        self.add_letter(self.coor_list)
        if boogle_main.check_if_valid(self.coor_list) == False:#here we can do some sign
            self.not_valid()

    def add_letter(self,coor_list):
        if len(coor_list) == 1:
            self.screen.new_word()
        display = ""
        for word in coor_list:
            display = display + self.board_dict[word]
        self.screen_input.set(display)
    ################################################# words_table #################################################################


    #################################################################### buttons ####################################################



#################################################################### END ####################################################3
boogle = Boogle(root)
root.mainloop()