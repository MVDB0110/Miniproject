import requests
import xmltodict

def schrijven(reisinformatie):
    try:
        with open('vertrektijden.xml', 'w') as station:
            try:
                station.write(reisinformatie)
            except:
                print("Kan bestand niet schrijven.")
    #Schrijf naar bestand 'vertrektijden.xml'

    except:
        print("Kan bestand niet openen.")

def ns_api(station):
    try:
        ns_inlog_gegevens = ('mike.vandenbrink@student.hu.nl', 'MVZ2I5XRllKXyuJ1nc5inwMMwGkh3GCCUg2B_Z2uBTGT6lwHngk5XA')
        ns_url = 'http://webservices.ns.nl/ns-api-avt?station='+str(station)
        ns_response = requests.get(ns_url, auth=ns_inlog_gegevens)
        ns_response = xmltodict.unparse(xmltodict.parse(ns_response.text),pretty=True)
    #Verbinding maken met NS API

    except:
        print("Kan niet verbinden met de NS")

    schrijven(ns_response)
    #Stuur informatie naar schrijf functie

def opvragen():
    try:
        with open('vertrektijden.xml', 'r') as station:
            vertrektijden = xmltodict.parse(station.read())
            return vertrektijden
        #Open bestand 'vertrektijden.xml' en maak het verwerkbaar
    except:
        return "Kan bestand niet openen."

def informatie():
    info = opvragen()
    reisinfo = "{:35}{:35}{:35}{:35}{:35}{:35}\n".format("Bestemming", "Tijd van vertrek", "Vertraging", "Soort trein", "Treinspoor","Reistip")
    #Variabele creeeren

    for trein in info['ActueleVertrekTijden']['VertrekkendeTrein']:
        vertrektijd = trein[ 'VertrekTijd' ].split('T')
        vertrektijd = vertrektijd[1]
        vertrektijd = vertrektijd.split('+')
        vertrektijd = vertrektijd[0]

        try:
            vertrekspoor = trein['VertrekSpoor']['#text']
        except:
            vertrekspoor = "niet bekend"

        try:
            vertraging = str(trein['VertrekVertragingTekst']).replace('min','') + 'minuten'
        except:
            vertraging = '0 minuten'

        try:
            tip = trein['ReisTip']
        except:
            tip = 'Geen tip bekend'
        #Informatie verwerken naar gewenste layout

        reisinfo +="{:35}{:35}{:35}{:35}{:35}{}\n".format(trein['EindBestemming'], vertrektijd, vertraging, trein['TreinSoort'], vertrekspoor, tip)
        #Informatie in een formatted string zetten
    return reisinfo