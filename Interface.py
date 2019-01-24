#-*- coding: utf-8 -*-
from math import ceil
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.item_1 = Frame(master)
        self.item_1.pack()

        self.item_2 = Frame(master)
        self.item_2.pack()

        self.item_3 = Frame(master)
        self.item_3.pack()

        self.item_4 = Frame(master)
        self.item_4.pack()

        self.item_5 = Frame(master)
        self.item_5.pack()

        self.lblap1 = Label(self.item_1, text="AP1", width=10)
        self.lblap1.pack(side=LEFT)

        self.txtap1 = Entry(self.item_1)
        self.txtap1["width"] = 25
        self.txtap1.pack(side=LEFT)

        self.lblap2 = Label(self.item_2, text="AP2", width=10)
        self.lblap2.pack(side=LEFT)

        self.txtap2 = Entry(self.item_2)
        self.txtap2["width"] = 25
        self.txtap2.pack(side=LEFT)

        self.lblap3 = Label(self.item_3, text="AP3", width=10)
        self.lblap3.pack(side=LEFT)

        self.txtap3 = Entry(self.item_3)
        self.txtap3["width"] = 25
        self.txtap3.pack(side=LEFT)

        self.lblmsg = Label(self.item_4, text=" ")
        self.lblmsg.pack()

        self.bt_media = Button(self.item_5, text="Media", width=10)
        self.bt_media["command"] = self.CalcularMedia
        self.bt_media.pack(side=LEFT)

        self.bt_quetoes = Button(self.item_5, text="Questões para fazer", width=20)
        self.bt_quetoes["command"] = self.Quest_pra_fazer_ap3
        self.bt_quetoes.pack(side=LEFT)

    def CalcularMedia(self):
        ap1= float(self.txtap1.get())
        ap2= float(self.txtap2.get())
        ap3= float(self.txtap3.get())

        media = float(ap1 * 0.3 + ap2 * 0.3 + ap3 * 0.4)

        if media >= 5:
            self.lblmsg["text"] = "Está aprovado!!! Nota: {:.2f}".format(media)
        else:
            self.lblmsg["text"] = "Não está aprovado!!! Nota: {:.2f}".format(media)

    def Quest_pra_fazer_ap3(self):
        ap1 = float(self.txtap1.get())
        ap2 = float(self.txtap2.get())

        questoes = float((5 - (ap1*0.3 + ap2*0.3))/0.4)/0.4

        self.lblmsg["text"] = "Terá que fazer {} questões pra atingir a média!!!".format(ceil(questoes))

tela = Tk()
tela.title("Calcular Notas")
Application(tela)
tela.mainloop()
