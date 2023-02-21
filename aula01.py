from tkinter import *

root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root 

        self.tela()
        self.root.mainloop()

    def tela(self):
        self.root.title('janela principal')
        self.root.configure(background='blue')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)

Application()
