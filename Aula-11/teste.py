from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def result():
    text = cb_esportes.get()
    messagebox.showinfo(title="Escolha", message=text)

janela = Tk()
janela.title('Mensagem')
janela.geometry('400x400')
janela.configure(background= '#dde')

Label(janela, text='Esportes', background= '#dde').pack(padx=20, pady=20)
vresult = StringVar()
listEsportes=['Futebol','Vôlei','Basquete']

cb_esportes = ttk.Combobox(janela, values=listEsportes)
cb_esportes.set('Futebol')
cb_esportes.pack(padx=20, pady=20)

botao = ttk.Button(janela, text='Mensagem', command=result, width=20)
botao.pack(padx=20, pady=20)



janela.mainloop()