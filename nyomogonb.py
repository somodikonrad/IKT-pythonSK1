from tkinter import*

ablak1 = Tk()

def masikablak():
    ablak2 = Toplevel(ablak1)
    uzenet = Message(ablak2, text = 'Készítette: Gipsz Jakab\nPiripócs\n2009.06.04', width = 300)
    gomb2 = Button(ablak2, text = 'Kilép', command = ablak2.destroy)
    uzenet.pack()
    gomb2.pack()
    ablak2.mainloop()

szoveg1 = Label(ablak1, text = 'Kattints a gombra!')
gomb1 = Button(ablak1, text = 'Névjegy', command = masikablak)

szoveg1.pack()
gomb1.pack()

ablak1.mainloop()