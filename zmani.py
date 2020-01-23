from tkinter import *

root = Tk()
root.geometry('1352x652+0+0')
root.configure(background = 'black')
words_list = list()
board_dict = {(0, 0): 'A', (0, 1): 'A', (0, 2): 'A', (0, 3): 'O', (1, 0): 'M', (1, 1): 'L', (1, 2): 'D', (1, 3): 'I', (2, 0): 'G', (2, 1): 'L', (2, 2): 'S', (2, 3): 'T', (3, 0): 'E', (3, 1): 'T', (3, 2): 'E', (3, 3): 'M'}
background = Frame(root,bg = 'black')
background.grid()
empty_frame = board_frame = Frame(root,bd = 20,bg = 'red',width = 100,height= 600 )
board_frame.grid(row = 0, column = 0)
board_frame = Frame(root,bd = 20,bg = 'yellow',width = 440,height= 600 )
board_frame.grid(row = 0, column = 1)
timer_frame = Frame(root,bd = 20,bg = 'blue' ,width = 440,height= 600 )
timer_frame.grid(row = 0, column = 2)
############################################################### board frame ##############################################################################################
submit_frame = Frame(board_frame,bg = 'grey',bd = 20,width = 100,height= 100 )
submit_frame.grid(row = 1, column = 0)
letter_frame = Frame(board_frame,bg = 'green',bd = 20,width = 440,height= 200)
letter_frame.grid(row = 0, column = 0)