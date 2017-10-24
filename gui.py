from tkinter import *
from ns_api import informatie,ns_api
from stationlijst import *

def tkinter_reis_label():
    stationsnaam = station.get()
    if stationsnaam.lower() in lijst():
        ns_api(stationsnaam)
        home.pack(side=LEFT,padx=10,pady=10)
        welkom.pack_forget()
        knoppen.pack_forget()
        reislabel.pack()
    else:
        station.insert(0, "Dit station kan niet worden gevonden in de database.")

def init():
    welkom.pack(pady=50)
    knoppen.pack(padx=100, pady=100, side=BOTTOM)
    ams.pack(side=LEFT)
    loskaartje.pack(side=LEFT)
    koopovchip.pack(side=LEFT)
    buitenland.pack(side=LEFT)
    reisinfo.pack(side=LEFT)
    station.pack(side=RIGHT, padx=10, pady=10)

def back():
    home.pack_forget()
    reislabel.pack_forget()
    welkom.pack(pady=50)
    knoppen.pack(padx=100, pady=100, side=BOTTOM)
    ams.pack(side=LEFT)
    loskaartje.pack(side=LEFT)
    koopovchip.pack(side=LEFT)
    buitenland.pack(side=LEFT)
    reisinfo.pack(side=LEFT)
    station.pack(side=RIGHT, padx=10, pady=10)

root = Tk()
root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.title("NS Reisinformatie")
root.configure(bg='yellow')
#Settings van het mainframe

background = 'yellow'
backgroundknop = 'blue'
reisinfo = informatie()
foto = PhotoImage(file='nedvlag.gif')
buttonheight = 5
buttonwidth = 20
#Config variabele

bottom = Frame(root,bg='blue',)
bottom.pack(side=BOTTOM,fill=X)
#Bottom container

header = Frame(root,bg='blue')
header.pack(side=TOP, fill=X)
#Header container

knoppen = Frame(master=root, background=background)
#Button container

reislabel = Text(root, width=len(reisinfo.split('\n')[ 0 ]) + 1, height=(reisinfo.count('\n') + 1),background=background, highlightbackground='black')
reislabel.insert(END, reisinfo)
reislabel.config(state=DISABLED)
#Reislabel creeren

home = Button(header,text='back',height=buttonheight,width=buttonwidth,command=back,highlightbackground=backgroundknop,background=background)
#Home button

welkom = Label(master=root,text='Welkom bij NS',foreground='blue',font=('Verdana',50,'bold italic'),background=background)
#NS tekst label

station = Entry(header, width=30, bg='white', highlightbackground='blue')
station.insert(0,'Vul hier een stationnaam in.')
#Station entry

foto = foto.subsample(3,3)
nedvlag = Label(bottom,image=foto,background='blue')
nedvlag.image = foto
nedvlag.pack(side=LEFT,padx=10,pady=10)
#Nederlandse vlag foto label

ams = Button(knoppen, text='Ik wil naar Amsterdam',height=buttonheight,width=buttonwidth ,highlightbackground=background, background='blue')
loskaartje = Button(knoppen, text='Ik wil een los kaartje kopen',height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
koopovchip = Button(knoppen, text='Kopen OV-chipkaart',height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
buitenland = Button(knoppen, text='Ik wil naar het buitenland',height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
reisinfo = Button(knoppen, text='Ik wil de reisinformatie van het aangegeven station',height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue', command=tkinter_reis_label)
#Buttons creeeren

init()
root.mainloop()
#Initialize