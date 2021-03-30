import numpy
import random
import time
import sys
import typing

INDEX_BELEGTER_SPEICHER_LISTE: int = 1
INDEX_BELEGTER_SPEICHER_ARRAY: int = 2
INDEX_SPEICHERVERAENDERUNG_LISTE: int = 3
INDEX_SPEICHERVERAENDERUNG_ARRAY: int = 4
INDEX_GESAMTLAUFZEIT_LISTE: int = 5
INDEX_GESAMTLAUFZEIT_ARRAY: int = 6
INDEX_LAUFZEITVERAENDERUNG_LISTE: int = 7
INDEX_LAUFZEITVERAENDERUNG_ARRAY: int = 8


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

    # Oeffnen der Datei zum Speichern der Messdaten
    datei: typing.TextIO = open(dateiname, "a")

    # Zaehlvariable
    derzeitige_wiederholung: int = 0

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
        speicherplatzveraenderung_liste: int = speicherplatz_liste_danach - \
            speicherplatz_liste_davor
        speicherplatzveraenderung_array: int = speicherplatz_array_danach - \
            speicherplatz_array_davor

        # Speichern der Messdaten in der Datei

        datei.write(",".join([str(e) for e in [derzeitige_wiederholung,
                                               speicherplatz_liste_danach, speicherplatz_array_danach,
                                               speicherplatzveraenderung_liste, speicherplatzveraenderung_array,
                                               gesamtlaufzeit_liste, gesamtlaufzeit_array,
                                               gesamtlaufzeitveraenderung_liste, gesamtlaufzeitveraenderung_array]
                              ]) + "\n")

        # Ausgeben einer Statusmeldung nach 1000 Wiederholungen
        if derzeitige_wiederholung % 1000 == 0:
            print("Messdaten fuer", derzeitige_wiederholung,
                  "Wiederholungen generiert")

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


# noinspection PyTypeChecker
def berechne_maximalabweichungen(dateinamen_messdaten: list, dateiname_mittelwerte: str,
                                 dateiname_maximalabweichungen: str, wiederholungen_je_datei: int):
    print("Maximalabweichungen werden berechnet...")

    # Erstellen der Datei, die die Maximalabweichungen speichert
    _erstelle_datei(dateiname=dateiname_maximalabweichungen)

    # Speichern der Messdaten aller Dateien in einer Liste
    messdaten: list = []
    for dateiname in dateinamen_messdaten:
        with open(dateiname, "r") as datei_messdaten:
            messdaten.append([zeile.split(",")
                              for zeile
                              in datei_messdaten.read().split("\n")
                              if zeile])

    # Speichern der Mittelwerte in einer Liste
    with open(dateiname_mittelwerte) as datei_mittelwerte:
        mittelwerte: list = [zeile.split(",")
                             for zeile
                             in datei_mittelwerte.read().split("\n")
                             if zeile]

    # Oeffnen der Datei, die die Maximalabweichungen speichert
    datei_maximalabweichungen = open(dateiname_maximalabweichungen, "a")

    # Vergleichen der verschiedenen Messdaten mit dem Durchschnitt und Filtern der groessten Abweichungen
    wiederholung: int = 0
    while wiederholung < wiederholungen_je_datei:
        wiederholung += 1

        # Initialisieren der Variablen der Mittelwerte
        mittelwert_belegter_speicher_liste: float = float(
            mittelwerte[wiederholung][INDEX_BELEGTER_SPEICHER_LISTE])
        mittelwert_belegter_speicher_array: float = float(
            mittelwerte[wiederholung][INDEX_BELEGTER_SPEICHER_ARRAY])

        mittelwert_speicherveraenderung_liste: float = float(
            mittelwerte[wiederholung][INDEX_SPEICHERVERAENDERUNG_LISTE])
        mittelwert_speicherveraenderung_array: float = float(
            mittelwerte[wiederholung][INDEX_SPEICHERVERAENDERUNG_ARRAY])

        mittelwert_gesamtlaufzeit_liste: float = float(
            mittelwerte[wiederholung][INDEX_GESAMTLAUFZEIT_LISTE])
        mittelwert_gesamtlaufzeit_array: float = float(
            mittelwerte[wiederholung][INDEX_GESAMTLAUFZEIT_ARRAY])

        mittelwert_gesamtlaufzeitveraenderung_liste: float = float(
            mittelwerte[wiederholung][INDEX_LAUFZEITVERAENDERUNG_LISTE])
        mittelwert_gesamtlaufzeitveraenderung_array: float = float(
            mittelwerte[wiederholung][INDEX_LAUFZEITVERAENDERUNG_ARRAY])

        # Berechnen der Maximalabweichungen
        maximalabweichung_belegter_speicher_liste: float = max(
            [
                float(messung[wiederholung][INDEX_BELEGTER_SPEICHER_LISTE]
                      ) - mittelwert_belegter_speicher_liste
                for messung in messdaten
            ], key=abs)

        maximalabweichung_belegter_speicher_array: float = max(
            [
                float(messung[wiederholung][INDEX_BELEGTER_SPEICHER_ARRAY]
                      ) - mittelwert_belegter_speicher_array
                for messung in messdaten
            ], key=abs)

        maximalabweichung_speicherveraenderung_liste: float = max(
            [
                float(messung[wiederholung][INDEX_SPEICHERVERAENDERUNG_LISTE]
                      ) - mittelwert_speicherveraenderung_liste
                for messung in messdaten
            ], key=abs)

        maximalabweichung_speicherveraenderung_array: float = max(
            [
                float(messung[wiederholung][INDEX_SPEICHERVERAENDERUNG_ARRAY]
                      ) - mittelwert_speicherveraenderung_array
                for messung in messdaten
            ], key=abs)

        maximalabweichung_gesamtlaufzeit_liste: float = max(
            [
                float(messung[wiederholung][INDEX_GESAMTLAUFZEIT_LISTE]
                      ) - mittelwert_gesamtlaufzeit_liste
                for messung in messdaten
            ], key=abs)

        maximalabweichung_gesamtlaufzeit_array: float = max(
            [
                float(messung[wiederholung][INDEX_GESAMTLAUFZEIT_ARRAY]
                      ) - mittelwert_gesamtlaufzeit_array
                for messung in messdaten
            ], key=abs)

        maximalabweichung_gesamtlaufzeitveraenderung_liste: float = max(
            [
                float(
                    messung[wiederholung][INDEX_LAUFZEITVERAENDERUNG_LISTE]
                ) - mittelwert_gesamtlaufzeitveraenderung_liste
                for messung in messdaten
            ], key=abs)

        maximalabweichung_gesamtlaufzeitveraenderung_array: float = max(
            [
                float(
                    messung[wiederholung][INDEX_LAUFZEITVERAENDERUNG_ARRAY]
                ) - mittelwert_gesamtlaufzeitveraenderung_array
                for messung in messdaten
            ], key=abs)

        # Speichern der Maximalabweichungen
        datei_maximalabweichungen.write(",".join(
            [str(wiederholung),
             str(maximalabweichung_belegter_speicher_liste), str(
                 maximalabweichung_belegter_speicher_array),
             str(maximalabweichung_speicherveraenderung_liste), str(
                 maximalabweichung_speicherveraenderung_array),
             str(maximalabweichung_gesamtlaufzeit_liste), str(
                 maximalabweichung_gesamtlaufzeit_array),
             str(maximalabweichung_gesamtlaufzeitveraenderung_liste),
             str(maximalabweichung_gesamtlaufzeitveraenderung_array)])
            + "\n")

    datei_maximalabweichungen.close()

    print("Maximalabweichungen erfolgreich gespeichert...")


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
        summe_speicher_liste: int = sum([int(messung[wiederholung][INDEX_BELEGTER_SPEICHER_LISTE])
                                         for messung in messdaten])
        summe_speicher_array: int = sum([int(messung[wiederholung][INDEX_BELEGTER_SPEICHER_ARRAY])
                                         for messung in messdaten])

        summe_speicherveraenderung_liste: int = sum([int(messung[wiederholung][INDEX_SPEICHERVERAENDERUNG_LISTE])
                                                     for messung in messdaten])
        summe_speicherveraenderung_array: int = sum([int(messung[wiederholung][INDEX_SPEICHERVERAENDERUNG_ARRAY])
                                                     for messung in messdaten])

        summe_gesamtlaufzeit_liste: float = sum([float(messung[wiederholung][INDEX_GESAMTLAUFZEIT_LISTE])
                                                 for messung in messdaten])
        summe_gesamtlaufzeit_array: float = sum([float(messung[wiederholung][INDEX_GESAMTLAUFZEIT_ARRAY])
                                                 for messung in messdaten])

        summe_gesamtlaufzeitveraenderung_liste: float = sum(
            [float(messung[wiederholung][INDEX_LAUFZEITVERAENDERUNG_LISTE])
             for messung in messdaten])
        summe_gesamtlaufzeitveraenderung_array: float = sum(
            [float(messung[wiederholung][INDEX_LAUFZEITVERAENDERUNG_ARRAY])
             for messung in messdaten])

        # Berechnen der Mittelwerte aus den Summen
        mittelwert_speicher_liste: float = summe_speicher_liste / anzahl_dateien_mit_messdaten
        mittelwert_speicher_array: float = summe_speicher_array / anzahl_dateien_mit_messdaten

        mittelwert_speicherveraenderung_liste: float = summe_speicherveraenderung_liste / \
            anzahl_dateien_mit_messdaten
        mittelwert_speicherveraenderung_array: float = summe_speicherveraenderung_array / \
            anzahl_dateien_mit_messdaten

        mittelwert_gesamtlaufzeit_liste: float = summe_gesamtlaufzeit_liste / \
            anzahl_dateien_mit_messdaten
        mittelwert_gesamtlaufzeit_array: float = summe_gesamtlaufzeit_array / \
            anzahl_dateien_mit_messdaten

        mittelwert_gesamtlaufzeitveraenderung_liste: float = \
            summe_gesamtlaufzeitveraenderung_liste / anzahl_dateien_mit_messdaten
        mittelwert_gesamtlaufzeitveraenderung_array: float = \
            summe_gesamtlaufzeitveraenderung_array / anzahl_dateien_mit_messdaten

        # Speichern der Mittelwerte
        datei_mittelwerte.write(",".join(
            [str(wiederholung),
             str(mittelwert_speicher_liste), str(mittelwert_speicher_array),
             str(mittelwert_speicherveraenderung_liste), str(
                 mittelwert_speicherveraenderung_array),
             str(mittelwert_gesamtlaufzeit_liste), str(
                 mittelwert_gesamtlaufzeit_array),
             str(mittelwert_gesamtlaufzeitveraenderung_liste), str(mittelwert_gesamtlaufzeitveraenderung_array)])
            + "\n")

    print("Mittelwerte erfolgreich gespeichert...")


if __name__ == "__main__":
    anzahl_dateien: int = int(
        input("Anzahl an Dateien mit Messdaten, die generiert werden:"))
    dateiname_anfang: str = input("Anfang des Dateinamen:")
    wiederholungen: int = int(input("Anzahl an Wiederholungen je Datei:"))
    dateinamen: list = [dateiname_anfang +
                        str(i + 1) + ".csv" for i in range(anzahl_dateien)]

    for name in dateinamen:
        messe_anhaengen(dateiname=name, wiederholungen_gesamt=wiederholungen)

    name_datei_mittelwerte = dateiname_anfang + "_mittelwerte.csv"
    berechne_mittelwerte(dateinamen_messdaten=dateinamen,
                         dateiname_mittelwerte=name_datei_mittelwerte,
                         wiederholungen_je_datei=wiederholungen)

    name_datei_maximalabweichungen = dateiname_anfang + "_maximalabweichungen.csv"
    berechne_maximalabweichungen(dateinamen_messdaten=dateinamen,
                                 dateiname_mittelwerte=name_datei_mittelwerte,
                                 dateiname_maximalabweichungen=name_datei_maximalabweichungen,
                                 wiederholungen_je_datei=wiederholungen)
