import numpy
import random
import time
import sys
import typing


def messe_anhaengen(dateiname: str, wiederholungen_gesamt: int):
    """
    Es werden Elemente an die Liste und den Array angehaengt;
    der Prozess wird gemessen;
    die Daten werden in einer Datei gespeichert.
    """

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


def berechne_mittelwerte(dateinamen_messdaten: list, dateiname_mittelwerte: str, wiederholungen_je_datei: int):
    print("Mittelwerte werden berechnet...")

    anzahl_dateien_mit_messdaten: int = len(dateinamen_messdaten)

    # Erstellen der Datei, die den Mittelwert speichert
    _erstelle_datei(dateiname=dateiname_mittelwerte)

    # Speichern der Dateiinhalte in einer Liste
    messdaten: list = []
    for dateiname in dateinamen_messdaten:
        with open(dateiname, "r") as datei_messdaten:
            messdaten.append([zeile.split(",")
                              for zeile
                              in datei_messdaten.read().split("\n")
                              if zeile])

    # Oeffnen der Datei, die die Mittelwerte speichert
    datei_mittelwerte: typing.TextIO = open(dateiname_mittelwerte, "a")

    # Berechnen des Durchschnitts jedes Elements und speichern in datei_mittelwert
    wiederholung: int = 0
    while wiederholung < wiederholungen_je_datei:
        wiederholung += 1

        # Berechnen der Summe der Messdaten nach der Wiederholung
        summe_speicher_liste: int = 0
        summe_speicher_array: int = 0

        summe_speicherveraenderung_liste: int = 0
        summe_speicherveraenderung_array: int = 0

        summe_gesamtlaufzeit_liste: float = 0
        summe_gesamtlaufzeit_array: float = 0

        summe_gesamtlaufzeitveraenderung_liste: float = 0
        summe_gesamtlaufzeitveraenderung_array: float = 0

        for messung in messdaten:
            summe_speicher_liste += int(messung[wiederholung][1])
            summe_speicher_array += int(messung[wiederholung][2])

            summe_speicherveraenderung_liste += int(messung[wiederholung][3])
            summe_speicherveraenderung_array += int(messung[wiederholung][4])

            summe_gesamtlaufzeit_liste += float(messung[wiederholung][5])
            summe_gesamtlaufzeit_array += float(messung[wiederholung][6])

            summe_gesamtlaufzeitveraenderung_liste += float(messung[wiederholung][7])
            summe_gesamtlaufzeitveraenderung_array += float(messung[wiederholung][8])

        # Berechnen der Mittelwerte aus den Summen
        mittelwert_speicher_liste: float = summe_speicher_liste / anzahl_dateien_mit_messdaten
        mittelwert_speicher_array: float = summe_speicher_array / anzahl_dateien_mit_messdaten

        mittelwert_speicherveraenderung_liste: float = summe_speicherveraenderung_liste / anzahl_dateien_mit_messdaten
        mittelwert_speicherveraenderung_array: float = summe_speicherveraenderung_array / anzahl_dateien_mit_messdaten

        mittelwert_gesamtlaufzeit_liste: float = summe_gesamtlaufzeit_liste / anzahl_dateien_mit_messdaten
        mittelwert_gesamtlaufzeit_array: float = summe_gesamtlaufzeit_array / anzahl_dateien_mit_messdaten

        mittelwert_gesamtlaufzeitveraenderung_liste: float = \
            summe_gesamtlaufzeitveraenderung_liste / anzahl_dateien_mit_messdaten
        mittelwert_gesamtlaufzeitveraenderung_array: float = \
            summe_gesamtlaufzeitveraenderung_array / anzahl_dateien_mit_messdaten

        # Speichern der Mittelwerte
        datei_mittelwerte.write(",".join(
            [str(wiederholung),
             str(mittelwert_speicher_liste), str(mittelwert_speicher_array),
             str(mittelwert_speicherveraenderung_liste), str(mittelwert_speicherveraenderung_array),
             str(mittelwert_gesamtlaufzeit_liste), str(mittelwert_gesamtlaufzeit_array),
             str(mittelwert_gesamtlaufzeitveraenderung_liste), str(mittelwert_gesamtlaufzeitveraenderung_array)])
                                + "\n")

    print("Mittelwerte erfolgreich gespeichert...")


if __name__ == "__main__":
    anzahl_dateien: int = int(input("Anzahl an Dateien mit Messdaten, die generiert werden:"))
    dateiname_anfang: str = input("Anfang des Dateinamen:")
    wiederholungen: int = int(input("Anzahl an Wiederholungen je Datei:"))
    dateinamen: list = [dateiname_anfang + str(i + 1) + ".csv" for i in range(anzahl_dateien)]

    for dateiname in dateinamen:
        messe_anhaengen(dateiname=dateiname, wiederholungen_gesamt=wiederholungen)

    berechne_mittelwerte(dateinamen_messdaten=dateinamen,
                         dateiname_mittelwerte=dateiname_anfang + "_mittelwerte.csv",
                         wiederholungen_je_datei=wiederholungen)
