from tkinter import*


foablak = Tk()


foablak.geometry('550x550')
foablak.title('Boroshordó')
vaszon=Canvas(foablak, width=160, height=160, bg='white')
kep = PhotoImage(file = 'D:\\IKT Konrád\\IKT-pythonSK\\hordo.png')

mennyiseg = Label(foablak, text= 'Bor mennyisége(l):')
mennyiseg.grid(column = 1, row = 1)
mennyib = Entry(foablak)
mennyib.grid(column = 2, row = 1, columnspan = 2)

sugar= Label(foablak, text= 'Hordó sugara(r):')
sugar.grid(column = 1, row = 2)
sugarg = Entry(foablak)
sugarg.grid(column = 2, row = 2, columnspan = 2)

magassag = Label(foablak, text= 'Hordó magassága(dm):')
magassag.grid(column = 1, row = 3)
magasg = Entry(foablak)
magasg.grid(column = 2, row = 3, columnspan = 2)

gomb1 = Button(foablak, text = 'kiszámítás')
gomb1.grid(column = 3, row = 4)

foablak.mainloop()