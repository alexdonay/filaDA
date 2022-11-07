# !/usr/bin/python3
import filaprioridade2
from tkinter import *

nova = filaprioridade2.fila([{"prioridade": 3, "dado": "estudar"}])
nova.append(1, "estudar")
nova.append(4, "viajar")
nova.append(2, "trabalhar")

class janela:
    def __init__(self, topLevel):
        self.fr1 = Frame(topLevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', command=self.call)
        self.botao.pack()
    def call(self):
        print("oi")
raiz = Tk()
janela(raiz)
raiz.mainloop()