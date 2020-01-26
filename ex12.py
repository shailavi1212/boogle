from tkinter import *
import boogle_main
import boggle_board_randomizer
import time
import winsound
import tkinter.messagebox


root = Tk()
root.geometry('1352x652+0+0')
root.configure(background = 'white' )

coor_list = list()
board = boggle_board_randomizer.randomize_board()
board_dict = boogle_main.convert_to_dict(board)
screen_input = StringVar()
word_list = boogle_main.words_list(boogle_main.FILEPATH)
score_output = IntVar()
score_output.set(0)
used_word_list = []
num_of_word = 0
##################################################### commands ###################################################################



background = Frame(root)
background.grid()
empty_frame = Frame(root,bg = 'white',width = 200,height= 600)
empty_frame.grid(row = 0, column = 0)
board_frame = Frame(root,bg = 'yellow',width = 440,height= 800 )
board_frame.grid(row = 0, column = 1)

score_frame =Frame(root ,bd = 20, bg = 'white',width = 80,height= 80 )
score_frame.place(x = 872, y = 70)

############################################################### board frame ##############################################################################################
timer_frame = Frame(board_frame,bd = 20,bg = 'white',width = 100,height= 100 )
timer_frame.grid(row = 0, column = 0)
screen_frame = Frame(board_frame)
screen_frame.grid(row = 1, column = 0)
letters_frame = Frame(board_frame,bd = 20,bg = 'white',width = 440,height= 400)
letters_frame.grid(row = 2, column = 0)
empty_space = Frame(board_frame,bd = 20,bg = 'white',width = 440,height= 30)
empty_space.grid(row = 3, column = 0)
submit_frame = Frame(board_frame,bd = 20,bg = 'white',width = 90,height= 50 )
submit_frame.grid(row = 4, column = 0)
################################################ empty_side  ##########################################################################
empty_space1 = Frame(empty_frame,bd = 20,width = 200,height= 500)
empty_space1.grid(row = 0,column = 0)
end_game_menu = Frame(empty_frame,bd = 20,width = 100,height= 100)
end_game_menu.place(x = 0, y = 450)
###################################################################### objects ###############################################
scroll = boogle_main.Scroll_bar()
screen = boogle_main.Screen(screen_frame,screen_input)
score = boogle_main.Score(score_frame,score_output)

###############################################################################################################################3
def time_is_up():

    answer = tkinter.messagebox.askquestion('','would you like to play again')
    if answer == 'yes':
        pass
        #new game
    else:
        pass
        #back to main menu
def back_to_main():
    pass
    #back to main menu
def countdown(count):
    label['text'] = count

    if count > 0:
        timer_frame.after(1000, countdown, count-1)
    else:
        time_is_up()
def end_of_word():
    word = boogle_main.convert_to_word(coor_list, board_dict)
    if boogle_main.check_word(word, used_word_list):
        if word in word_list:
            screen.right_answer()
            score_temp = score_output.get() + boogle_main.calculate_score(word)
            score_output.set(score_temp)
            used_word_list.append(word)
            scroll.add_word(word)
            coor_list.clear()
            return
        else:
            not_valid()
    else:
        not_valid()

    coor_list.clear()
def not_valid():
    screen.not_valid()
    coor_list.clear()

def button_clicked(x,y):
    coor_list.append((x,y))
    add_letter(coor_list)
    if boogle_main.check_if_valid(coor_list) == False:#here we can do some sign
        not_valid()


    print(coor_list)
def add_letter(coor_list):
    if len(coor_list) == 1:
        screen.new_word()
    display = ""
    for word in coor_list:
        display = display + board_dict[word]
    screen_input.set(display)
################################################# words_table #################################################################


#################################################################### buttons ####################################################
exit_button = Button(end_game_menu,text = 'main menu',command = back_to_main)
exit_button.grid(row = 1, column = 0,sticky = N)
submit_button = Button(submit_frame,text = 'submit',font = 'david 14',command = end_of_word)
submit_button.place(x = -10,y = -15)
for col in range (4):
    for row in range(4):
        button = Button(letters_frame, text = board_dict[(col,row)],fg = 'red',width = 2, height= 2,
                         command = lambda x = col,y = row:button_clicked(x,y))
        button.grid(row = col,column = row)
############################################################ display #######################################################
label = Label(timer_frame,text = '30',bg = 'white', font = 'ariel 25')
label.place(x = 10, y = 15)
countdown(180)


#################################################################### END ####################################################3
root.mainloop()