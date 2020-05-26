class Mastermind:
    def __init__(self):
        self.board_color = [1,2,3,4,5,6]
        self.board_game = Mastermind.new_board()
        self.board_hidden = []
        self.actual_pos = 1

    @staticmethod
    def new_board():
        board = []
        for i in range(10):
            board.append([])
            for j in range(9):
                if j == 0:
                    board[i].append(i+1)
                else:
                    board[i].append(0)
        return board
    
    def backspace_row(self):
        self.board_game[self.actual_pos-1][1:5] = 0
    
    def test_row(self):
        for i in range(1,5):
            while j < len(self.board_hidden):
                if self.board_game[self.actual_pos-1][i] == self.board_hidden[i-1]:
                    self.board_game[self.actual_pos-1][i+4] = 1
                    break
                elif self.board_game[self.actual_pos-1][i] == self.board_hidden[j]:
                    self.board_game[self.actual_pos-1][i+4] = -1
                    break
                j+=1
    
    def add_color_row(self,color,pos):
        self.board_game[self.actual_pos-1][pos] = color