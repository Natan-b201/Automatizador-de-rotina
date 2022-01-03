from tkinter import *
import tkinter as tk

class SituationView:
    def __init__(self):
        self.inst = tk.Tk()

        self.inst.title("Automatizador - NBO2001")
        self.inst.geometry('400x150')

        self.div_1 = Frame(self.inst)
        self.div_1['width'] = 350
        self.div_1['height'] = 100
        self.div_1['pady'] = 10
        self.div_1.pack(side=TOP)

        self.div_2 = Frame(self.inst)
        self.div_2['width'] = 350
        self.div_2['height'] = 100
        self.div_2['pady'] = 10
        self.div_2.pack()

        self.exit = Button(self.div_2)
        self.exit['text'] = "Sair"
        self.exit['command'] = self.inst.destroy

        self.loc = Label(self.div_1, text="")   
        self.loc['width'] = 350
        self.loc['height'] = 100 
        


    def situation(self, text):
        self.loc['text'] = text
        self.loc.pack() 
        self.loc.update_idletasks()
        self.inst.update()

    def ext(self):
        self.inst.destroy()

    def buttonExit(self):
        self.exit.pack()
        self.exit.update_idletasks()
        self.inst.update()

    def update(self):
        self.inst.update()

    def start(self):
        self.inst.mainloop()
        