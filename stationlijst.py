import requests
import xmltodict

def lijst():
    try:
        stations = list()
        ns_inlog_gegevens = ('mike.vandenbrink@student.hu.nl', 'MVZ2I5XRllKXyuJ1nc5inwMMwGkh3GCCUg2B_Z2uBTGT6lwHngk5XA')
        ns_url = 'http://webservices.ns.nl/ns-api-stations-v2'
        ns_response = requests.get(ns_url, auth=ns_inlog_gegevens)
        ns_response = xmltodict.parse(ns_response.text)
        for station in ns_response['Stations']['Station']:
            if station['Land'] == 'NL':
                stations.append(station['Namen']['Kort'].lower())
                stations.append(station[ 'Namen' ][ 'Middel' ].lower())
                stations.append(station[ 'Namen' ][ 'Lang' ].lower())
        stations.sort()
        return stations

    except:
        print("Kan niet verbinden met de NS")

lijst()