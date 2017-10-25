import requests
import xmltodict

def schrijven(reisinformatie):
    try:
        with open('vertrektijden.xml', 'w') as station:
            try:
                station.write(reisinformatie)
            except:
                print("Kan bestand niet schrijven.")
    except:
        print("Kan bestand niet openen.")

def ns_api(station):
    try:
        ns_inlog_gegevens = ('mike.vandenbrink@student.hu.nl', 'MVZ2I5XRllKXyuJ1nc5inwMMwGkh3GCCUg2B_Z2uBTGT6lwHngk5XA')
        ns_url = 'http://webservices.ns.nl/ns-api-avt?station='+str(station)
        ns_response = requests.get(ns_url, auth=ns_inlog_gegevens)
        ns_response = xmltodict.unparse(xmltodict.parse(ns_response.text),pretty=True)

    except:
        print("Kan niet verbinden met de NS")
    schrijven(ns_response)

def opvragen():
    try:
        with open('vertrektijden.xml', 'r') as station:
            vertrektijden = xmltodict.parse(station.read())
            return vertrektijden
    except:
        return "Kan bestand niet openen."

def informatie():
    info = opvragen()
    reisinfo = "{:35}{:20}{:30}{:3}\n".format("Bestemming", "Tijd van vertrek", "Soort trein", "Treinspoor")
    for trein in info['ActueleVertrekTijden']['VertrekkendeTrein']:
        vertrektijd = trein[ 'VertrekTijd' ].split('T')
        vertrektijd = vertrektijd[1]
        vertrektijd = vertrektijd.split('+')
        vertrektijd = vertrektijd[0]
        reisinfo +="{:35}{:20}{:30}{:8}\n".format(trein['EindBestemming'], vertrektijd, trein['TreinSoort'], trein['VertrekSpoor']['#text'])
    return reisinfo