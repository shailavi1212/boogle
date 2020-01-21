import sys
import boggle_board_randomizer as boo
import time
import Graphics

START_MSG = "Let's play Boogle!"
SEC_MSG = "Great job! keep going :)"
LOS_MSG = "There is no word like this, try again"
QUIT_MSG = "Thanks for playing! hope to see you soon"
BOARD_SIZE = 4


class Board(object):
    def __init__(self):
        self.board = boggle_board_randomizer
        self.words = self.words_list
        self.col_size = BOARD_SIZE
        self.row_size = BOARD_SIZE

    def generate_board(self):
        board = self.board
        return board

    def words_list(self, filepath):
        with open(filepath) as boogle_dict:
            words = []
            for line in boogle_dict:
                words.append(line.strip())
            return words

    def convert_to_coor(self):
        coor_lst = [(i, j) for i in range(4) for j in range(4)]
        coor_lst = [coor_lst[x:x + 4] for x in range(0, len(coor_lst), 4)]
        dict_letter_coor = {}
        for i in range(4):
            for j in range(4):
                dict_letter_coor[coor_lst[i][j]] = self.board[i][j]
        return dict_letter_coor

class Cube(object):
    def __init__(self, size, face, shape):
        self.size = size
        self.face = face
        self.shape = shape


class Player(object):
    """

    """
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.word_list = []

    def number_of_words(self):
        return len(self.word_list)

    def add_word(self, word):
        self.word_list.append(word)
        self.calculate_score(word)

    def calculate_score(self, word):
        return len(word) ** 2


# make sure word is valid
def check_word(word, player):
    # make sure word is on the board
    # make sure word is in the dictionary
    if word in player.word_list:
        return False
    return True


def main():
    input = None
    options = ['y', 'n']

    input = raw_input("Would you like to play a game? (y/n): ").strip()
    while (input not in options):
        print("you typed %s. Please type 'y' or 'n'" % input)
        input = None
        input = raw_input("Would you like to play a game? (y/n): ").strip()

    playing = input.lower().startswith('y')

    if playing:
        # game setup
        player = Player("Chad")
        board = Board()
    while (playing):
        board.display()
        # would be nice to highlight the letter(s) typed to go along with the user
        # input, and only allow letters that are on the board
        # so if there are multiple 'E's, then they are all highlighted when 'e' is typed
        # and if the next letter is 's', then only highlight the places on the board
        # where E-S are neighbours.
        # Then, if followed by another 'e', highlight only the E-S-E pattern (if it
        # exists) else do not allow another 'e' to be entered.
        word = raw_input("Enter a word you want to score: ").strip()
        if check_word(word, player):
            player.add_word(word, score_word(word))
        else:
            print("You've already scored that word. Try again.\n")

        if player.num_words() == 5:
            break
    if playing:
        player.print_score()

    exit_message()


if __name__ == '__main__':
    main()





def check_if_valid(self,coor_lst):

    if len(coor_lst) == len(set(coor_lst)):
        return True
    else:
        return False
def cauculate_score(self):
