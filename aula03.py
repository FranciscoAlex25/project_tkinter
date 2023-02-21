from tkinter import *

root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root 

        self.tela()
        self.frames()
        self.botoes()
        self.entrys_and_labels()

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

    def botoes(self):
        self.btnlipar = Button(self.frame1, text='limpar', bg='purple', activeforeground='purple')
        self.btnlipar.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.15)

        self.btnbuscar = Button(self.frame1, text='buscar', bg='orange', activeforeground='orange')
        self.btnbuscar.place(relx=0.21, rely=0.05, relwidth=0.15, relheight=0.15)

        self.btncadastrar = Button(self.frame1, text='cadastrar', bg='lightgreen', activeforeground='green')
        self.btncadastrar.place(relx=0.42, rely=0.05, relwidth=0.15, relheight=0.15)

        self.btnatualizar = Button(self.frame1, text='atualizar', bg='blue', activeforeground='blue')
        self.btnatualizar.place(relx=0.58, rely=0.05, relwidth=0.15, relheight=0.15)

        self.btnapagar = Button(self.frame1, text='apagar', bg='red', activeforeground='red')
        self.btnapagar.place(relx=0.74, rely=0.05, relwidth=0.15, relheight=0.15)

    def entrys_and_labels(self):
        self.labelnome = Label(self.frame1, text='Nome', bg='white')
        self.labelnome.place(relx=0.05, rely=0.34)

        self.entrynome = Entry(self.frame1)
        self.entrynome.place(relx=0.16, rely=0.3, relwidth=0.5, relheight=0.15)

        self.labeltelefone = Label(self.frame1, text='Telefone', bg='white')
        self.labeltelefone.place(relx=0.05, rely=0.52)

        self.entrytelefone = Entry(self.frame1)
        self.entrytelefone.place(relx=0.16, rely=0.52, relwidth=0.5, relheight=0.15)

        self.labelcidade = Label(self.frame1, text='Cidade', bg='white')
        self.labelcidade.place(relx=0.05, rely=0.75)

        self.entrycidade = Entry(self.frame1)
        self.entrycidade.place(relx=0.16, rely=0.72, relwidth=0.5, relheight=0.15)

        self.labelcodigo = Label(self.frame1, text='Código', bg='white')
        self.labelcodigo.place(relx=0.70, rely=0.55)

        self.entrycodigo = Entry(self.frame1)
        self.entrycodigo.place(relx=0.70, rely=0.67, relwidth=0.25, relheight=0.15)


Application()
