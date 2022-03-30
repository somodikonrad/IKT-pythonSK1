from tkinter import*
foablak = Tk()

gyoker = 'D:\\IKT Konrád\\IKT-pythonSK\\'

img = PhotoImage(file= gyoker + "hordo.gif")
foablak.iconphoto(True, img)

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


mennyiseg = Label(foablak, text= 'Ennyi literes a hordó: ')
mennyiseg.grid(column = 1, row = 5)
mennyib = Entry(foablak)
mennyib.grid(column = 2, row = 5, columnspan = 2)

sugar= Label(foablak, text= 'Ennyi liter fér még bele:')
sugar.grid(column = 1, row = 6)
sugarg = Entry(foablak)
sugarg.grid(column = 2, row = 6, columnspan = 2)

magassag = Label(foablak, text= 'Ennyi százalékig van a hordó:')
magassag.grid(column = 1, row = 7)
magasg = Entry(foablak)
magasg.grid(column = 2, row = 7, columnspan = 2)


foablak.mainloop()