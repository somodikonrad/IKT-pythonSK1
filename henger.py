from tkinter import*
import math

foablak = Tk()


sugar = Label(foablak, text= 'Sugár(cm):')
sugar.grid(column = 1, row = 1)
sugarb = Entry(foablak)
sugarb.grid(column = 2, row = 1, columnspan = 2)

magassag = Label(foablak, text= 'Magasság(cm):')
magassag.grid(column = 1, row = 2)
magasg = Entry(foablak)
magasg.grid(column = 2, row = 2, columnspan = 2)

gomb1 = Button(foablak, text = 'kiszámítás')
gomb1.grid(column = 3, row = 3)

terfogat = Label(foablak, text= 'Térfogat(cm3):')
terfogat.grid(column = 1, row = 4, columnspan = 1)
terfb = Entry(foablak)
terfb.grid(column = 2, row = 4, columnspan = 2)

Vashenger = Label(foablak, text= 'Vashenger(cm):')
Vashenger.grid(column = 1, row = 5)
vashengb = Entry(foablak)
vashengb.grid(column = 2, row = 5, columnspan = 2)

foablak.mainloop()