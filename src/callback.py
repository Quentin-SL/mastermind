from tkinter import Canvas

class Callback():
    def __init__(self, game):
        self.test = 1
        self.game = game
        self.counter_paw = 0
        self.victory = False

    
    def define_number(self, window) :
        array = []
        for i in range(10) :
            array.append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
            array[i].place(relx = 0.1, y = 100 + 52 * i, height = 50, width = 50)
            array[i].create_text(25, 25, text = str(self.game.get_board_game()[i][0]))
        return array

    def define_color(self, window) :
        array = []
        for i in range(10) :
            array.append([])
            for j in range(4) :
                array[i].append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
                array[i][j].place(relx = 0.135 + 0.035 * j, y = 100 + 52 * i, height = 50, width = 50)
                array[i][j].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#000000")
        return array

    def define_hint(self, window) :
        array = []
        for i in range(10) :
            array.append([])
            for j in range(5) :
                if j == 0:
                    array[i].append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
                    array[i][j].place(relx = 0.2755, y = 100 + 52 * i, height = 50, width = 50)
                if j == 1:
                    array[i].append(Canvas(array[i][0], background = "#B2C2BB", highlightthickness= 0))
                    array[i][j].place(x = 0, y = 0, height = 25, width = 25)
                    array[i][j].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
                if j == 2:
                    array[i].append(Canvas(array[i][0], background = "#B2C2BB", highlightthickness= 0))
                    array[i][j].place(x = 0, y = 25, height = 25, width = 25)
                    array[i][j].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
                if j == 3:
                    array[i].append(Canvas(array[i][0], background = "#B2C2BB", highlightthickness= 0))
                    array[i][j].place(x = 25, y = 0, height = 25, width = 25)
                    array[i][j].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
                if j == 4:
                    array[i].append(Canvas(array[i][0], background = "#B2C2BB", highlightthickness= 0))
                    array[i][j].place(x = 25, y = 25, height = 25, width = 25)
                    array[i][j].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
        return array

    def button_color(self, window, color_block):
        array = []
        for i in range(6) :
            array.append(Canvas(window, background = "#050A02", highlightthickness= 0))
            array[i].place(relx = 0.1 + 0.035 * i, y = 37.5, height = 50, width = 50)
            if i == 0 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "red")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 1, "red", color_block))
            if i == 1 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "blue")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 2, "blue", color_block))
            if i == 2 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "yellow")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 3, "yellow", color_block))
            if i == 3 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "purple")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 4, "purple", color_block))
            if i == 4 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "orange")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 5, "orange", color_block))
            if i == 5 :
                array[i].create_oval(25+10, 25+10, 25-10, 25-10, fill = "green")
                array[i].bind('<Button-1>', lambda event: self.add_color(event, 6, "green", color_block))
        return array

    def erase_row(self, color_block):
        self.game.backspace_row()
        for i in range(4):
            color_block[self.game.get_actual_pos()-1][i].delete("all")
            color_block[self.game.get_actual_pos()-1][i].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#000000")
        self.counter_paw = 0

    def add_color(self, event, color, hexa, color_block):
        if(self.counter_paw<4):
            self.game.add_color_row(color,self.counter_paw+1)
            color_block[self.game.get_actual_pos()-1][self.counter_paw].delete("all")
            color_block[self.game.get_actual_pos()-1][self.counter_paw].create_oval(25+10, 25+10, 25-10, 25-10, fill = hexa)
            self.counter_paw+=1

    def test_row(self, hint_block):
        if self.counter_paw == 4:
            self.game.test_row()
            for i in range(5,9):
                hint_block[self.game.get_actual_pos()-1][i-4].delete("all")
                if self.game.get_board_game()[self.game.get_actual_pos()-1][i] == 1 :
                    hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "red")
                elif self.game.get_board_game()[self.game.get_actual_pos()-1][i] == -1 :
                    hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "white")
                else :
                    hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
            self.counter_paw = 0
            self.victory = self.game.victory_condition()