from tkinter import*
import math

foablak = Tk()


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