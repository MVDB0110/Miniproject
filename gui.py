from tkinter import *
from ns_api import informatie,ns_api
from stationlijst import *
from tkinter.messagebox import showinfo
import re

def tkinter_reis_label():
    stationlijst = lijst()
    stationsnaam = station.get()
    if stationsnaam.lower() in stationlijst:
        global reislabel
        ns_api(stationsnaam)
        reisinfo = informatie()
        #Opgevraagde informatie over stationnamen en de vertrekinformatie

        reislabel = Text(root, height=(len(reisinfo.split('\n'))+1), background=background, highlightbackground=background)
        #Reislabel definieren

        reislabel.insert(END, reisinfo)
        reislabel.config(state=DISABLED)
        reislabel.pack(fill=X,pady=20)
        home.pack(side=LEFT,padx=10,pady=10)
        #Informatie in reislabel stoppen en packen van reislabel en back button

        welkom.pack_forget()
        knoppen.pack_forget()
        #Home screen 'hiden'

    else:
        search = list()
        #Search output lijst creeeren

        suggestie = "Bedoelde u:\n"
        #Suggestie string creeeren

        stations = ".*" + stationsnaam + "*."
        station.delete(0,END)
        #Regular Expression 'pattern' en station-entry leegmaken

        for stationnamen in stationlijst:
            if re.search(stations,stationnamen) != None:
                search.append(re.search(stations,stationnamen).string)
        #Kijken voor elke naam in stationlijst of deze redelijker wijs overeenkomt met mijn pattern

        for stationnamen in search:
            suggestie += "- "+stationnamen+"\n"
        #Output van search in string zetten

        showinfo("Suggestie",suggestie)
        #Suggesties laten zien op scherm

def init():
    buttonpadding = 5
    welkom.pack(pady=50)
    knoppen.pack(padx=100, pady=100, side=BOTTOM)
    ams.pack(side=LEFT,padx=buttonpadding)
    loskaartje.pack(side=LEFT,padx=buttonpadding)
    koopovchip.pack(side=LEFT,padx=buttonpadding)
    buitenland.pack(side=LEFT,padx=buttonpadding)
    reisinfo.pack(side=LEFT,padx=buttonpadding)
    station.pack(side=RIGHT, padx=10, pady=10)
    #Packen van homescherm

def back():
    global reislabel
    home.pack_forget()
    reislabel.destroy()
    init()
    #Homescherm terugbrengen

root = Tk()
root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.title("NS Reisinformatie")
root.configure(bg='yellow')
#Settings van het mainframe

background = 'yellow'
backgroundknop = 'blue'
foto = PhotoImage(file='nedvlag.gif')
buttonheight = 5
buttonwidth = 30
buttontext = 'white'
#Config variabele

bottom = Frame(root,bg='blue',)
bottom.pack(side=BOTTOM,fill=X)
#Bottom container

header = Frame(root,bg='blue',height=20)
header.pack(side=TOP, fill=X)
#Header container

knoppen = Frame(master=root, background=background)
#Button container

reislabel = Text()
#Reislabel globaal creeren

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

ams = Button(knoppen, text='Ik wil naar Amsterdam', foreground=buttontext,height=buttonheight,width=buttonwidth ,highlightbackground=background, background='blue')
loskaartje = Button(knoppen, text='Ik wil een los kaartje kopen', foreground=buttontext,height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
koopovchip = Button(knoppen, text='Kopen OV-chipkaart', foreground=buttontext,height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
buitenland = Button(knoppen, text='Ik wil naar het buitenland', foreground=buttontext,height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue')
reisinfo = Button(knoppen, text='Reisinformatie van aangegeven station', foreground=buttontext,height=buttonheight,width=buttonwidth , highlightbackground=background, background='blue', command=tkinter_reis_label)
#Buttons creeeren

init()
root.mainloop()
#Initialize