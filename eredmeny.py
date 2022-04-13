from tkinter import*

def nevjegy():
    abl2 = Toplevel(foablak)
    uz2 = Message(abl2, text = 'Készítette: Gipsz Jakab\nPiripócs\n2009.06.04', width = 300)
    gomb2 = Button(abl2, text = 'Kilép', command = abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

def felszin():
    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        mezo4.delete(0,END)
        mezo4.insert(0,str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title('A téglatest felszíne')
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label (abl3, text='a:')
    szoveg2 = Label (abl3, text='b:')
    szoveg3 = Label (abl3, text='c:')
    szoveg4 = Label (abl3, text='Eredmény:')
    gomb1 = Button(abl3, text = 'Számítás', command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky = W)
    mezo1.grid(row=1, column=2, sticky = W)
    mezo2.grid(row=2, column=2, sticky = W)
    mezo3.grid(row=3, column=2, sticky = W)
    mezo4.grid(row=5, column=2, sticky = W)

    abl3.mainloop()
    
def terfogat():

    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo1.get())
        c = eval(mezo1.get())
        felszin = a*b*c
        mezo4.delete(0, END)
        mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title('A téglatest térfogata')
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = 'a:')
    szoveg2 = Label(abl3, text = 'b:')
    szoveg3 = Label(abl3, text = 'c:')
    szoveg4 = Label(abl3, text = 'Eredmény:')
    gomb1 = Button(abl3, text = 'Számítás', command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, columb = 2, sticky = W)
    mezo2.grid(row = 2, columb = 2, sticky = W)
    mezo3.grid(row = 3, columb = 2, sticky = W)
    mezo4.grid(row = 5, columb = 2, sticky = W)
    abl3.mainloop()

foablak = Tk()
foablak.title('A téglatest adatai')
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu1 = Menubutton(menusor, text = 'Fájl', underline = 0)
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label = 'Névjegy', command = nevjegy, underline = 0)
fajl.add_command(label = 'Kilépés', command = foablak.destroy, underline = 0)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text = 'Téglatest', underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = 'Felszín', command = felszin, underline = 0)
teglatest.add_command(label = 'Térfogat', command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

ablak1 = Tk()
ablak1.title('A téglatest adatai')
ablak1.minsize(width = 300, height = 100)

def ujablak():
    abl2 = Toplevel(ablak1)
    abl2.title('Eredmények')
    abl2.minsize(width = 300, height = 100)

    sz1 = Label(abl2, text = 'Felszín: ')
    sz2 = Label(abl2, text = 'Térfogat: ')
    m1 = Entry(abl2)
    m2 = Entry(abl2)

    sz1.grid(row = 1)
    sz2.grid(row = 2)
    m1.grid(row = 1, column = 2, sticky = W)
    m2.grid(row = 2, column = 2, sticky = W)

    a = eval(mezo1.get())
    b = eval(mezo1.get())
    c = eval(mezo1.get())

    felszin = 2*(a*b+a*c+b*c)
    terfogat = a*b*c

    m1.delete(0, END)
    m1.insert(0, str(felszin))
    m2.delete(0, END)
    m2.insert(0, str(terfogat))

    abl2.mainloop()

szoveg1 = Label(ablak1, text = 'a:')
szoveg2 = Label(ablak1, text = 'b:')
szoveg3 = Label(ablak1, text = 'c:')
gomb1 = Button(ablak1, text = 'Számítás', command = ujablak)
mezo1 = Entry(ablak1)
mezo2 = Entry(ablak1)
mezo3 = Entry(ablak1)


szoveg1.grid(row = 1)
szoveg2.grid(row = 2)
szoveg3.grid(row = 3)
gomb1.grid(row = 4, column = 2, sticky = W)
mezo1.grid(row = 1, column = 2, sticky = W)
mezo2.grid(row = 2, column = 2, sticky = W)
mezo3.grid(row = 3, column = 2, sticky = W)

ablak1.mainloop()


