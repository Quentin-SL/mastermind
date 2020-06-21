from src.mastermind import Mastermind
from tkinter import *

game = Mastermind()

ROOT = Tk()
counter_paw = 0 #compteur de pions par ligne 0=>3
victory = False

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs)) 

Button(ROOT, text = "Test the line", command = lambda : test_row()).place(relx = 0.45, rely = 0.3)
Button(ROOT, text = "Erase the line", command = lambda : erase_row()).place(relx = 0.45, rely = 0.4)

def define_number() :
    array = []
    for i in range(10) :
        array.append(Canvas(ROOT, background = "#B2C2BB",highlightthickness= 0))
        array[i].place(relx = 0.1, y = 100 + 52 * i, height = 50, width = 50)
        array[i].create_text(25, 25, text = str(game.board_game[i][0]))
    return array


def define_color() :
    array = []
    for i in range(10) :
        array.append([])
        for j in range(4) :
            array[i].append(Canvas(ROOT, background = "#B2C2BB",highlightthickness= 0))
            array[i][j].place(relx = 0.135 + 0.035 * j, y = 100 + 52 * i, height = 50, width = 50)
            array[i][j].create_oval(25+2,25+2,25-2,25-2, fill = "#000000")
    return array

def define_hint() :
    array = []
    for i in range(10) :
        array.append([])
        for j in range(5) :
            if j == 0:
                array[i].append(Canvas(ROOT, background = "#B2C2BB",highlightthickness= 0))
                array[i][j].place(relx = 0.2755, y = 100 + 52 * i, height = 50, width = 50)
            if j == 1:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB",highlightthickness= 0))
                array[i][j].place(x = 0, y = 0, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 2:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB",highlightthickness= 0))
                array[i][j].place(x = 0, y = 25, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 3:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB",highlightthickness= 0))
                array[i][j].place(x = 25, y = 0, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 4:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB",highlightthickness= 0))
                array[i][j].place(x = 25, y = 25, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
    return array

def erase_row():
    global game
    global color_block
    global counter_paw
    game.backspace_row()
    for i in range(4):
        color_block[game.actual_pos-1][i].delete("all")
        color_block[game.actual_pos-1][i].create_oval(25+2,25+2,25-2,25-2, fill = "#000000")
    counter_paw = 0

def add_color(event,color,hexa):
    global game
    global color_block
    global counter_paw
    if(counter_paw<4):
        game.add_color_row(color,counter_paw+1)
        color_block[game.actual_pos-1][counter_paw].delete("all")
        color_block[game.actual_pos-1][counter_paw].create_oval(25+10,25+10,25-10,25-10, fill = hexa)
        counter_paw+=1

def test_row():
    global counter_paw
    global game
    global hint_block
    global victory
    game.test_row()
    for i in range(5,9):
        hint_block[game.actual_pos-1][i-4].delete("all")
        if game.board_game[game.actual_pos-1][i-4] == 1 :
            hint_block[game.actual_pos-1][i-4].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "red")
        else :
            hint_block[game.actual_pos-1][i-4].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "white")
    counter_paw = 0
    victory = game.victory_condition()


def button_color():
    array = []
    for i in range(6) :
        array.append(Canvas(ROOT, background = "#050A02",highlightthickness= 0))
        array[i].place(relx = 0.1 + 0.035 * i, y = 37.5, height = 50, width = 50)
        if i == 0 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "red")
            array[i].bind('<Button-1>', lambda event: add_color(event,1,"red"))
        if i == 1 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "blue")
            array[i].bind('<Button-1>', lambda event: add_color(event,2,"blue"))
        if i == 2 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "yellow")
            array[i].bind('<Button-1>', lambda event: add_color(event,3,"yellow"))
        if i == 3 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "purple")
            array[i].bind('<Button-1>', lambda event: add_color(event,4,"purple"))
        if i == 4 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "orange")
            array[i].bind('<Button-1>', lambda event: add_color(event,5,"orange"))   
        if i == 5 :
            array[i].create_oval(25+10,25+10,25-10,25-10, fill = "green")
            array[i].bind('<Button-1>', lambda event: add_color(event,6,"green"))
    return array

number_block = define_number()
color_block = define_color()
hint_block = define_hint()
buttons_block = button_color()

game.push_hidden_random()

def test_switch_color(event,color):
    color[0][0].delete("all") # detruit toute les formes 
    color[game.actual_pos-1][0].create_oval(25+2,25+2,25-2,25-2, fill = "#000000")
    #test_button.destroy() #disparait le button
    

#test_button = Button(ROOT, text = "test_couleur", command = lambda : test_switch_color(event,color,test_button))
#test_button.place(relx = 0.45, rely = 0.6)

ROOT.mainloop()

""" TODO
fonction callback qui test en back la ligne et en front placer les pions d'indice 
fonction callback de victoire et de defaite 
"""