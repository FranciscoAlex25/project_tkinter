import tkinter as tk
from tkinter import messagebox

import sqlite3


class Main:
   
    def limpar_entries(self):
        self.entrynome.delete(0, tk.END)
        self.entrycidade.delete(0, tk.END)
        self.entrytelefone.delete(0, tk.END)
        self.entrycodigo.delete(0, tk.END)

    def conecta_db(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()

    def desconecta_db(self):
        self.conn.close()

    def criar_tabela(self):
        self.conecta_db()
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS clientes (
                                cod INTEGER PRIMARY KEY, 
                                nome CHAR(40) NOT NULL, 
                                cidade CHAR(40) NOT NULL,
                                telefone CHAR(40) NOT NULL 
                                );''')
            self.conn.commit()
            print('Tabela criada')

            self.desconecta_db()
        except Exception as e:
            print(e)

    def inserir_clientes(self):

        self.nome = self.entrynome.get()
        self.cidade = self.entrycidade.get()
        self.telefone = self.entrytelefone.get()

        if self.nome != '' and self.cidade != '' and self.telefone != '':
            try:
                self.conecta_db()
                self.cursor.execute('''
                                INSERT INTO clientes (nome, cidade, telefone) VALUES(
                                    ?, ?, ?
                                );''', (self.nome, self.cidade, self.telefone))
                self.conn.commit(); print('cadastrado com sucesso!')
            except Exception as e:
                print(e)
            finally:
                self.limpar_entries()
                self.listar_clientes()
        else:
            messagebox.showinfo('campo vazio', 'Existem campos vazio')

    def listar_clientes(self):
        self.tabela.delete(*self.tabela.get_children())

        try:
            self.conecta_db()
            dados = self.cursor.execute('''
                SELECT cod, nome, cidade, telefone FROM clientes ORDER BY cod ASC;
            ''')

            for i in dados:
                self.tabela.insert('', tk.END, values=i)

            self.conn.commit()
        except Exception as e:
            print(e)  

    def doubleclick(self, event):
        self.limpar_entries()

        for i in self.tabela.selection():
            col1, col2, col3, col4 = self.tabela.item(i, 'values')
        
        self.codigo = self.entrycodigo.insert(tk.END, col1)
        self.nome = self.entrynome.insert(tk.END, col2)
        self.cidade = self.entrycidade.insert(tk.END, col3)
        self.telefone = self.entrytelefone.insert(tk.END, col4)

    def deletar_cliente(self):
        self.codigo = self.entrycodigo.get()
        self.conecta_db()
        self.cursor.execute('''
            DELETE FROM clientes WHERE cod = (?);
         ''', (self.codigo))
        self.conn.commit()

        self.limpar_entries()
        self.listar_clientes()

    def atualizar_registro(self):
        self.codigo = self.entrycodigo.get()
        self.nome = self.entrynome.get()
        self.cidade = self.entrycidade.get()
        self.telefone = self.entrytelefone.get()

        self.conecta_db()
        self.cursor.execute('''UPDATE clientes SET
            cod = (?), nome = (?), cidade = (?), telefone = (?)
        WHERE cod = (?);''', (self.codigo, self.nome, self.cidade, self.telefone, self.codigo))

        self.conn.commit()

        self.limpar_entries()
        self.listar_clientes()
