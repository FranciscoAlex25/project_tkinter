from tkinter import *

root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root 

        self.tela()
        self.frames()

        self.root.mainloop()

    def tela(self):
        self.root.title('janela principal')
        self.root.configure(background='gray')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)

    def frames(self):
        self.frame1 = Frame(self.root, bd=7, bg='white', highlightbackground='black', 
                            highlightthickness=2)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
                
        self.frame2 = Frame(self.root, bd=7, bg='white', highlightbackground='black', 
                            highlightthickness=2)
        self.frame2.place(relx=0.01, rely=0.52, relwidth=0.98, relheight=0.46)


Application()
