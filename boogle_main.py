import boggle_board_randomizer as boo
board_let_lst = boo.randomize_board()
coor_lst = [(i,j)for i in range(4) for j in range(4)]
coor_lst = [coor_lst[x:x+4] for x in range(0, len(coor_lst), 4)]
dict_letter_coor = {}
for i in range(4):
    for j in range(4):
        dict_letter_coor[coor_lst[i][j]] = board_let_lst[i][j]


def check_if_valid(self,coor_lst):

    if len(coor_lst) == len(set(coor_lst)):
        return True
    else:
        return False
def cauculate_score(self):
    return len(self.word) ** 2
