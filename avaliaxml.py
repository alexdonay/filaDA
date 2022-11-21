import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from xml.dom import minidom
from tkinter import messagebox

# Tags
tagTipoEmissao = "tpEmis"
tagCNPJ = "CNPJ"
tagRazaoSocial = "xNome"
tagCodigoProduto = "cProd"
tagDescricaoProduto = "xProd"
tagTipoPagamento = "tPag"
tagCFOP = "CFOP"


window = tk.Tk()
window.title("Analizador NFe de entrada")

lblAviso = tk.Label(window, text="Escolha o Arquivo para análise")
lblAviso.pack(expand=True)
filename = ""
lblname = None
btnAnalise = None

tagEmissao = {
    "01": "01 - Dinheiro",
    "02": "02 - Cheque",
    "03": "03 - Cartão de Crédito",
    "04": "04 - Cartão de Débito",
    "05": "05 - Crédito Loja",
    "10": "10 - Vale Alimentação",
    "11": "11 - Vale Refeição",
    "12": "12 - Vale Presente",
    "13": "13 - Vale Combustível",
    "14": "14 - Duplicata Mercantil",
    "15": "15 - Boleto Bancário",
    "90": "90 - Sem Pagamento",
    "99": "99 - Outros"
}


def analise():
    global filename
    file = minidom.parse(file=filename)
    tpEmissao = "Emissão propria" if (file.getElementsByTagName(tagTipoEmissao)[
                                      0].firstChild.data) == 1 else "Emissão de terceiros"
    tipoPagamento = tagEmissao[file.getElementsByTagName(tagTipoPagamento)[
        0].firstChild.data]
    cnpjEmitente = file.getElementsByTagName(tagCNPJ)[0].firstChild.data
    emitente = (file.getElementsByTagName(tagRazaoSocial)[0].firstChild.data)
    cnpjDestinatario = file.getElementsByTagName(tagCNPJ)[1].firstChild.data
    destinatario = (file.getElementsByTagName(
        tagRazaoSocial)[1].firstChild.data)
    produtos = file.getElementsByTagName(tagCodigoProduto)
    string = "Tipo de Pagamento: " + tipoPagamento + "\n" + tpEmissao + "\nEmitente:\n" + "CNPJ: " + cnpjEmitente + \
        "\nRazao Social: " + emitente + "\n" + "Destinatario:" + \
        "\nCNPJ: " + cnpjDestinatario + "\nRazao Social: " + destinatario
    index = 0

    for i in produtos:
        string = string + "\nCódigo do produto " + i.firstChild.data + "\nDescrição: " + file.getElementsByTagName(
            tagDescricaoProduto)[index].firstChild.data + "\nCFOP :" + file.getElementsByTagName(tagCFOP)[index].firstChild.data
        index += 1
    messagebox.showinfo("showinfo", string)


def select_file():
    global filename
    global lblname
    global btnAnalise
    filetypes = (
        ('text files', '*.xml'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Selecione o arquivo',
        initialdir='/Users/SUPORTE03/Downloads',
        filetypes=filetypes
    )

    if lblname != None:
        lblname.destroy()
        lblname = tk.Label(window, text=filename)
        lblname.pack(expand=True)
    else:
        lblname = tk.Label(window, text=filename)
        lblname.pack(expand=True)
    if btnAnalise != None:
        btnAnalise.destroy()
        btnAnalise = tk.Button(
            window, text='Analise o arquivo', command=analise)
        btnAnalise.pack(expand=True)
    else:
        btnAnalise = tk.Button(
            window, text='Analise o arquivo', command=analise)
        btnAnalise.pack(expand=True)
    if filename == "":
        lblname.destroy()
        btnAnalise.destroy()


open_button = tk.Button(
    window,
    text='NF-e Arquivo XML',
    command=select_file
)

open_button.pack(expand=True)
window.mainloop()
