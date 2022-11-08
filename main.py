# !/usr/bin/python3
from filaprioridade2 import *
from tkinter import *
from tkinter import ttk

def preencheWindow():
    
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Prioridade")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Ação")

    for i in range(len(nova.arr)):
        tree.insert("", "end", text=i, values=(
            nova.arr[i]["prioridade"], nova.arr[i]["dado"]))

def atualizaWindow():
    for i in tree.get_children():
        tree.delete(i)
    preencheWindow()

def removerFila():
    nova.remove()
    atualizaWindow()

def incluirFila():
    nova.append((int)(textPrioridade.get()), textDado.get())
    atualizaWindow()

nova = fila([{"prioridade": 1, "dado": "estudar"},{"prioridade": 1, "dado": "estudar"},{"prioridade": 1, "dado": "estudar"},{"prioridade": 1, "dado": "estudar"}])

window = Tk()
window.title("Estrutura de dados - Fila")
tree = ttk.Treeview(window, column=("c1", "c2"), show='headings', height=10)
preencheWindow()
btnRemover = ttk.Button(text="Remover", command=removerFila)
btnIncluir = ttk.Button(text="Incluir", command=incluirFila)
lblPrioridade = ttk.Label(text="Prioridade")
textPrioridade = ttk.Entry()
lblDado = ttk.Label(text="Dado")
textDado = ttk.Entry()



tree.pack()
btnRemover.pack()
lblPrioridade.pack()
textPrioridade.pack()
lblDado.pack()
textDado.pack()
btnIncluir.pack()

window.mainloop()
