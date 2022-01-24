#Import von Packages
import csv
import pandas as pd
from tabulate import tabulate


#Festlegen der Begriffe in der Kopfzeile
FIELDNAMES = ['Hauptartikelnr', 'Artikelname', 'Hersteller', 'Beschreibung', 'Materialangaben', 'Geschlecht', 'Produktart', 'Ärmel', 'Bein', 'Kragen', 'Herstellung', 'Taschenart', 'Grammatur', 'Material', 'Ursprungsland', 'Bildname']


#Funktion zum Ausgeben der Tabelle
def display_csv():
    table = pd.read_csv("Artikel.csv", delimiter=";")
    df = pd.DataFrame(table)
    df = df.fillna("")
    print(tabulate(df, headers=FIELDNAMES, tablefmt="fancy_grid"))


#Funktion zum Lesen der csv-Datein
def read_csv():
    with open('Artikel.csv', 'r', encoding='utf-8') as csv_datei:
        reader = list(csv.reader(csv_datei, delimiter=';'))
        return reader


#Funktion zum Anfügen von Datensätzen an die csv-Datei
def write_csv(datensatz):
    with open('Artikel.csv', 'a', encoding='utf-8') as csv_datei:
        writer = csv.DictWriter(csv_datei,delimiter=';', fieldnames=FIELDNAMES)
        writer.writerow(datensatz)


if __name__ == '__main__':
    #Beispiel zum Anfügen von Datensätzen:
    satz = {'Hauptartikelnr': 100, 'Artikelname': "T-Shirt"}
    write_csv(satz)
    display_csv()