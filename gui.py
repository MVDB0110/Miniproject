from tkinter import *
from ns_api import opvragen

def reisinformatie():
    info = opvragen()
    reisinfo = "{:35}{:20}{:30}{:3}\n".format("Bestemming", "Tijd van vertrek", "Soort trein", "Treinspoor")
    for trein in info['ActueleVertrekTijden']['VertrekkendeTrein']:
        vertrektijd = trein[ 'VertrekTijd' ].split('T')
        vertrektijd = vertrektijd[1]
        vertrektijd = vertrektijd.split('+')
        vertrektijd = vertrektijd[0]
        reisinfo +="{:35}{:20}{:30}{:8}\n".format(trein['EindBestemming'], vertrektijd, trein['TreinSoort'], trein['VertrekSpoor']['#text'])
    reislabel = Text(root, width=len(reisinfo.split('\n')[0])+1, height=reisinfo.count('\n'), background=background, highlightbackground='black')
    reislabel.pack()
    reislabel.insert(END,reisinfo)
    reislabel.config(state=DISABLED)
    welkom.pack_forget()
    knoppen.pack_forget()

root = Tk()

root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.title("NS Reisinformatie")
root.configure(bg='yellow')

background = 'yellow'
backgroundknop = 'blue'

welkom = Label(master=root,
               text='Welkom bij NS',
               foreground='blue',
               font=('Verdana',50,'bold italic'),
               background=background)
welkom.pack(pady=50)


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

reisinfo = Button(knoppen, text='Ik wil de reisinformatie van het aangegeven station', highlightbackground=background, background='blue', command=reisinformatie)
reisinfo.pack(side=LEFT)

root.mainloop()