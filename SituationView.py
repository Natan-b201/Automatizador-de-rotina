from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from time import sleep


class SituationView:
    def __init__(self, master):
        self.inst = master

        self.inst.title("Automatizador - NBO2001")
        self.inst.geometry('400x300')

        self.div_1 = Frame(self.inst)
        self.div_1['width'] = 350
        self.div_1['height'] = 100
        self.div_1['pady'] = 10
        self.div_1.pack(side=TOP)

        self.div_2 = Frame(self.inst)
        self.div_2['width'] = 350
        self.div_2['height'] = 100
        self.div_2['pady'] = 10
        self.div_2.pack(side=TOP)

        self.div_3 = Frame(self.inst)
        self.div_3['width'] = 350
        self.div_3['height'] = 100
        self.div_3['pady'] = 10
        self.div_3.pack(side=TOP)

        self.exit = Button(self.div_3)
        self.exit['text'] = "Sair"
        self.exit['command'] = self.inst.destroy

        self.loc = Label(self.div_1, text="")     
        self.loc.pack()   

        # self.buttonAlert = Button(self.div_1)
        # self.buttonAlert['command'] = self.alert
        # self.buttonAlert['text'] = "Aviso"
        # self.buttonAlert['pady'] = 5
        # self.buttonAlert.pack()

        # self.progress = Progressbar(self.div_2, orient=HORIZONTAL, length= 100, mode='determinate')
        
    
    def situation(self, text):
        self.loc['text'] = text
        self.loc.update_idletasks()

    def ext(self):
        self.inst.destroy()

    def buttonExit(self):
        self.exit.pack()
        self.exit.update_idletasks()
    
    # def alert(self):
    #     self.progress.pack()
    #     for i in range(1,110,10):    
    #         self.progress['value'] = i
    #         self.div_2.update_idletasks()
    #         sleep(0.5)

    #     self.exit.pack()
    #     # messagebox.showinfo(title='Alerta', message="Preencha todas as informações")
