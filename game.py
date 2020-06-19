from src.mastermind import Mastermind
from tkinter import *

game = Mastermind()

ROOT = Tk()

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs)) 

Button(ROOT, text = "Test the line", command = game.test_row).place(relx = 0.45, rely = 0.3)
Button(ROOT, text = "Erase the line", command = game.backspace_row).place(relx = 0.45, rely = 0.4)

def define_number() :
    array = []
    for i in range(10) :
        array.append(Canvas(ROOT, background = "#B2C2BB"))
        array[i].place(relx = 0.1, y = 100 + 52 * i, height = 50, width = 50)
        array[i].create_text(25, 25, text = str(game.board_game[i][0]))
    return array




ROOT.mainloop()

