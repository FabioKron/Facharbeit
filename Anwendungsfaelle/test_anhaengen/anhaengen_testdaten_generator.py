import numpy
import random
import time
import sys
import typing


def messe_anhaengen(dateiname: str, wiederholungen_gesamt: int):
    # Ausgeben einer Statusmeldung vor dem Generieren der Messdaten
    print("Messdaten werden generiert...")

    _erstelle_datei(dateiname=dateiname)

    # Initialisieren der Liste und des Arrays
    liste: list = []
    array: numpy.ndarray = numpy.arange(0)

    # Initialisieren der Variablen zum Speichern der Laufzeit
    gesamtlaufzeit_liste: float = 0.0
    gesamtlaufzeit_array: float = 0.0

    # Zaehlvariable
    derzeitige_wiederholung: int = 0

    # Oeffnen der Datei zum Speichern der Messdaten
    datei: typing.TextIO = open(dateiname, "a")

    # Wiederholen der Aktion + Speichern der Messdaten
    while derzeitige_wiederholung < wiederholungen_gesamt:
        derzeitige_wiederholung += 1

        # Speichern des Speicherplatzes vor dem Anhaengen
        speicherplatz_liste_davor: int = sys.getsizeof(liste)
        speicherplatz_array_davor: int = sys.getsizeof(array)

        # Generieren einer Zufallszahl zum anhaengen an den Datenstrukturen
        zufallszahl: float = random.random()

        # Anhaengen der Zufallszahl an Liste + Messen der Zeit
        start_zeit_anhaengen_liste: float = time.time()
        liste.append(zufallszahl)
        gesamtlaufzeitveraenderung_liste: float = time.time() - start_zeit_anhaengen_liste

        # Anhaengen der Zufallszahl an Array + Messen der Zeit
        start_zeit_anhaengen_array: float = time.time()
        array = numpy.append(array, zufallszahl)
        gesamtlaufzeitveraenderung_array: float = time.time() - start_zeit_anhaengen_array

        # Berechnen der uebrigen Messdaten
        gesamtlaufzeit_liste += gesamtlaufzeitveraenderung_liste
        gesamtlaufzeit_array += gesamtlaufzeitveraenderung_array

        speicherplatz_liste_danach: int = sys.getsizeof(liste)
        speicherplatz_array_danach: int = sys.getsizeof(array)
        speicherplatzveraenderung_liste: int = speicherplatz_liste_danach - speicherplatz_liste_davor
        speicherplatzveraenderung_array: int = speicherplatz_array_danach - speicherplatz_array_davor

        # Speichern der Messdaten in der Datei

        datei.write(",".join([str(e) for e in [derzeitige_wiederholung,
                                               speicherplatz_liste_danach, speicherplatz_array_danach,
                                               speicherplatzveraenderung_liste, speicherplatzveraenderung_array,
                                               gesamtlaufzeit_liste, gesamtlaufzeit_array,
                                               gesamtlaufzeitveraenderung_liste, gesamtlaufzeitveraenderung_array]
                              ]) + "\n")

        # Ausgeben einer Statusmeldung nach 1000 Wiederholungen
        if derzeitige_wiederholung % 1000 == 0:
            print("Messdaten fuer", derzeitige_wiederholung, "Wiederholungen generiert")

    # Schliessen der Datei
    datei.close()

    # Ausgeben einer Statusmeldung nach Beenden des Generieren der Messdaten
    print("Messdaten in", dateiname, "gespeichert")


def _erstelle_datei(dateiname: str):
    open(dateiname, "x").close()

    with open(dateiname, "a") as datei:
        datei.write("Wiederholung,Speicher Liste gesamt,Speicher Array gesamt,Speicherveraenderung Liste," +
                    "Speicherveraenderung Array,Gesamtlaufzeit Liste,Gesamtlaufzeit Array," +
                    "Gesamtlaufzeitveraenderung Liste,Gesamtlaufzeitveraenderung Array\n")
