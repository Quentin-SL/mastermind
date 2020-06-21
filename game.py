from src.mastermind import Mastermind
from tkinter import *

game = Mastermind()

ROOT = Tk()

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs)) 

Button(ROOT, text = "Test the line", command = lambda : game.test_row()).place(relx = 0.45, rely = 0.3)
Button(ROOT, text = "Erase the line", command = lambda : game.backspace_row()).place(relx = 0.45, rely = 0.4)

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

def button_color():
    array = []
    for i in range(6) :
        array.append([])
        array[i].append(Canvas(ROOT, background = "#050A02",highlightthickness= 0))
        array[i].place(relx = 0.1, y = 37.5, height = 50, width = 50)
        array[i].create_oval(25+10,25+10,25-10,25-10, fill = "red")
        array[i].bind('<Button-1>', lambda event: test_switch_color(event,color,test_button))
        #if i == 0 :
            #buttons[i].create_oval(fill = "red")    
        #if i == 1 :
            
        #if i == 2 :
            
        #if i == 3 :
            
        #if i == 4 :
               
        #if i == 5 :
    return array[i]

number = define_number()
color = define_color()
hint = define_hint()
buttons = button_color()

color[0][0].create_oval(25+10,25+10,25-10,25-10, fill = "red")

def test_switch_color(event,color,test_button):
    color[0][0].delete("all") # detruit toute les formes 
    color[game.actual_pos-1][0].create_oval(25+2,25+2,25-2,25-2, fill = "#000000")
    test_button.destroy() #disparait le button
    

test_button = Button(ROOT, text = "test_couleur", command = lambda : test_switch_color(color,test_button))
test_button.place(relx = 0.45, rely = 0.6)

#red_button = Canvas(ROOT, background = "#050A02",highlightthickness= 0)
#red_button.place(relx = 0.1, y = 37.5, height = 50, width = 50)
#red_button.create_oval(25+10,25+10,25-10,25-10, fill = "red")
#red_button.bind('<Button-1>', lambda event: test_switch_color(event,color,test_button))

ROOT.mainloop()

""" TODO
placer les pions de couleur et les rendre interagissable
fonction callback pour placer en back et en front un pion dans le plateau 
fonction callback pour effacer en back et en front les pions dans le plateau 
fonction callback qui test en back la ligne et en front placer les pions d'indice 
fonction callback de victoire et de defaite 
"""