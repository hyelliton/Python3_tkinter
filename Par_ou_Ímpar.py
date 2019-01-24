from tkinter import *

class Impar_Par:

    def __init__(self, master=None):
        #Frame na ordem de exibição dos elementos
        self.Item_1 = Frame(master)
        self.Item_1["bg"] = "red"
        self.Item_1.place(x=130, y=111.584, width=40, height=40)

        self.Item_2 = Frame(master)
        self.Item_2.place(x=114.158, y=144.940, width=71.683, height=20.198)

        self.Item_3 = Frame(master)
        self.Item_3["bg"] = "red"
        self.Item_3.pack(side=BOTTOM)

        #Label, Entry e Button
        self.NumEntrada = Entry(self.Item_1)
        self.NumEntrada.pack()

        self.bt_Verificar = Button(self.Item_2, text="Verificar", width=10)
        self.bt_Verificar["command"] = self.Par_Impar
        self.bt_Verificar.pack()

        self.lb_Resultado = Label(self.Item_3, text="Resultado", bg="red")
        self.lb_Resultado.pack()

    #Funções
    def Par_Impar(self):
        numero = self.NumEntrada.get()

        if int(numero) % 2 == 0:
            self.lb_Resultado["text"] = """Esse número é "PAR": {}""".format(numero)
        else:
            self.lb_Resultado["text"] = """Esse número é "ÍMPAR": {}""".format(numero)

tela = Tk()
tela.title("Par ou Ímpar?")
tela.geometry("300x300")
tela["bg"] = "red"
Impar_Par(tela)
tela.mainloop()