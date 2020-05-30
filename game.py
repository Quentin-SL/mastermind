from src.mastermind import Mastermind
from tkinter import *
from tkinter import ttk

game = Mastermind()

ROOT = Tk()

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs))

Button(ROOT, text = "Test the line").place(relx = 0.8, rely = 0.3)
Button(ROOT, text = "Erase the line").place(relx = 0.8, rely = 0.4)

def define_number():
    array = []
    for i in range(10):
        array.append(ttk.Label(ROOT, text = str(game.board_game[i][0]), background = "#B2C2BB", 
                anchor = "center").place(relx = 0.1, y = 100 + 52*i, height = 50, width = 50))
    return array

array = define_number()

ROOT.mainloop()