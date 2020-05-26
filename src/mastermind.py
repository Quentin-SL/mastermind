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