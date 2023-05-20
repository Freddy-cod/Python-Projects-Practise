import math


class Piece(object):
    '''This class initialises a letter to be used in the TicTacToe game .'''
    def __init__(self, letter):
        '''A constructor instatiating an objects with one instance variable'''

        self.letter = letter

    def get_move(self, game):
        '''This methods handles turns , it prompts the user to enter a position in
        the displayed board game . Checks wether the number is acceptable ,
        while the number is not accepted it continues prompting.It uses methods
        from TicTacToe class ,represented here by its object 'game' to check
        available moves (to play,put the value in screen and display the
        board).'''

        print(self.letter + "'s turn.")
        position = input("Choose a position from (1-9): ")
        valid = False
        accepted_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while not valid:
            while position not in accepted_positions:
                position = input("Choose a position from 1-9: ")
            position = int(position) - 1
            valid = game.available_moves(position)
        game.put_onboard(position, self.letter)
        game.print_board()

    def change_player(self):
        '''This methods flips the player(X or O) and allocates another .'''

        if self.letter == "x":
            self.letter = "o"
        elif self.letter == "o":
            self.letter = "x"


class X(Piece):
    '''This is a subclass inheriting the properties and methods of Piece .
    Initialisation belongs to the parent .'''
    def __init__(self, letter):
        Piece.__init__(self, letter)


class O_(Piece):
    '''This is a subclass inheriting the properties and methods of Piece .
    Initialisation belongs to the parent .'''
    def __init__(self, letter):
        Piece.__init__(self, letter)


class TicTacToeBoard(object):
    '''This is a TicTacToe class , it creates the board and the general
    functionality and logic of the game .'''

    def __init__(self):
        '''An object is instatiated here , it has properties winner(to
        determine the winner ), game_on(to check wether game is still on or not
        ) and board which creates positions of the board .'''

        self.winner = None
        self.game_on = True
        self.board = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-",
        ]

    def print_board(self):
        '''Displays the board'''
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])

    def available_moves(self, position):
        '''Checks wether or position or moves are available to the
        player and returns a boolean .'''

        if self.board[position] == "-":
            return True
        else:
            return False

    def put_onboard(self, position, player):
        '''Puts player(X or O) in the board and the specified position .'''

        self.board[position] = player

    def check_if_gamover(self):
        '''Checks if game is over or not ,it makes its decision through
        two methods which belong to self .'''

        self.check_winner()
        self.check_tie()

    def check_winner(self):
        '''Method checks the winner , it relies on three methods which checks
        wether there has been a match in a row ,colum or match diagonally .'''

        row_win = self.check_row()
        col_win = self.check_col()
        diagonal_win = self.check_diagonals()
        if row_win:
            self.winner = row_win
        elif col_win:
            self.winner = col_win
        elif diagonal_win:
            self.winner = diagonal_win
        else:
            self.winner = None

    def check_tie(self):
        '''It checks wether the board is full and there is no winner .
        It returns True or False .'''

        if "-" not in self.board:
            self.game_on = False
            return True
        return False

    def check_row(self):
        '''Checks wether there is a math in a row and its values are not "-"
        If there is a math , the game is over , it returns the player who won
        (X or O) .'''

        row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "-"

        if row_1 or row_2 or row_3:
            self.game_on = False
        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]
        else:
            return None

    def check_col(self):
        '''Checks wether there is a match in a column and its values are not "-"
        If there is a match , the game is over , it returns the player who won
        (X or O) .'''

        column_1 = self.board[0] == self.board[3] == self.board[6] != "-"
        column_2 = self.board[1] == self.board[4] == self.board[7] != "-"
        column_3 = self.board[2] == self.board[5] == self.board[8] != "-"

        if column_1 or column_2 or column_3:
            self.game_on = False
        if column_1:
            return self.board[0]
        elif column_2:
            return self.board[1]
        elif column_3:
            return self.board[2]
        return None

    def check_diagonals(self):
        '''Checks wether there is a match  diagonally and its values are not "-"
        If there is a match , the game is over , it returns the player who won
        (X or O) .'''

        diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "-"
        diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "-"
        if diagonal_1 or diagonal_2:
            self.game_on = False
        if diagonal_1:
            return self.board[0]
        elif diagonal_2:
            return self.board[2]
        return None

    def print_results(self):
        '''Method prints the results of the game .'''
        if self.winner == "x" or self.winner == "o":
            print(self.winner + " won.")
        else:
            print("Tie.")


# This function plays the game .
def play_game():
    print("\n Lets play TicTacToe\n")
    game = TicTacToeBoard()
    game.print_board()

    while game.game_on:
        turns = X("x")
        turns.get_move(game)
        game.check_if_gamover()
        turns.change_player()
    game.print_results()


play_game()