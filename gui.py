from tkinter import *
from ns_api import informatie,ns_api
from stationlijst import *

def tkinter_reis_label():
    stationsnaam = station.get()
    if stationsnaam.lower() in lijst():
        ns_api(stationsnaam)
        reisinfo = informatie()
        reislabel = Text(root, width=len(reisinfo.split('\n')[ 0 ]) + 1, height=(reisinfo.count('\n') + 1), background=background, highlightbackground='black')
        reislabel.pack()
        reislabel.insert(END, reisinfo)
        reislabel.config(state=DISABLED)
        welkom.pack_forget()
        knoppen.pack_forget()
    else:
        station.insert(0,"Dit station kan niet worden gevonden in de database.")

root = Tk()

root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.title("NS Reisinformatie")
root.configure(bg='yellow')

background = 'yellow'
backgroundknop = 'blue'

header = Frame(root,bg='blue')
header.pack(side=TOP, fill=X)

welkom = Label(master=root,
               text='Welkom bij NS',
               foreground='blue',
               font=('Verdana',50,'bold italic'),
               background=background)
welkom.pack(pady=50)

station = Entry(header, width=30, bg='white', highlightbackground='blue')
station.insert(0,'Vul hier een stationnaam in.')
station.pack(side=RIGHT,padx=10,pady=10)

bottom = Frame(root,bg='blue',)
bottom.pack(side=BOTTOM,fill=X)

foto = PhotoImage(file='nedvlag.gif')
foto = foto.subsample(3,3)
nedvlag = Label(bottom,image=foto,background='blue')
nedvlag.image = foto
nedvlag.pack(side=LEFT,padx=10,pady=10)


knoppen = Frame(master=root, background=background)
knoppen.pack(padx=100 ,pady=100, side=BOTTOM)

ams = Button(knoppen, text='Ik wil naar Amsterdam', highlightbackground=background, background='blue')
ams.pack(side=LEFT)

loskaartje = Button(knoppen, text='Ik wil een los kaartje kopen', highlightbackground=background, background='blue')
loskaartje.pack(side=LEFT)

koopovchip = Button(knoppen, text='Kopen OV-chipkaart', highlightbackground=background, background='blue')
koopovchip.pack(side=LEFT)

buitenland = Button(knoppen, text='Ik wil naar het buitenland', highlightbackground=background, background='blue')
buitenland.pack(side=LEFT)

reisinfo = Button(knoppen, text='Ik wil de reisinformatie van het aangegeven station', highlightbackground=background, background='blue', command=tkinter_reis_label)
reisinfo.pack(side=LEFT)

root.mainloop()