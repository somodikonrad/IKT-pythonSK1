from tkinter import*
import math

gyoker = 'D:\\IKT Konrád\\IKT-pythonSK\\'



def szamitas():
    r = int(sugarb.get())
    m = int(magasg.get())
    terfogat = math.pi * r * r * m
    
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

terfogat = Label(foablak, text= 'Térfogat(cm³):')
terfogat.grid(column = 1, row = 4, columnspan = 1)
terfb = Entry(foablak)
terfb.grid(column = 2, row = 4, columnspan = 2)

Vashenger = Label(foablak, text= 'Vashenger(cm):')
Vashenger.grid(column = 1, row = 5)
vashengb = Entry(foablak)
vashengb.grid(column = 2, row = 5, columnspan = 2)

fahenger = Label(foablak, text= 'Fahenger(cm):')
fahenger.grid(column = 1, row = 6)
fahengb = Entry(foablak)
fahengb.grid(column = 2, row = 6, columnspan = 2)


photo = PhotoImage(file = gyoker + 'shiba.gif')
foablak.iconphoto(True, photo)
foablak.mainloop()