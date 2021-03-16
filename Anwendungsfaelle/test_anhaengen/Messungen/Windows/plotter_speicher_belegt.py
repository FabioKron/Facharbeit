import matplotlib.pyplot as plt
import sys

# Einlesen der Datei als String
with open(str(sys.argv[1]), "r") as datei:
    dateiinhalt: str = datei.read()

# Umwandeln des Dateiinhalts von String in Liste
dateiinhalt: list = dateiinhalt.split("\n")
dateiinhalt: list = [zeile.split(",") for zeile in dateiinhalt if zeile]

# Sortieren der benoetigten Daten in seperate Listen
wiederholung: list = [int(zeile[0]) for zeile in dateiinhalt[1:]]
speicher_liste_gesamt: list = [float(zeile[1]) for zeile in dateiinhalt[1:]]
speicher_array_gesamt: list = [float(zeile[2]) for zeile in dateiinhalt[1:]]

# Grafische Darstellung der Listen
liste, = plt.plot(wiederholung, speicher_liste_gesamt, label="Liste")
array, = plt.plot(wiederholung, speicher_array_gesamt, label="Array")

plt.margins(0)

plt.title(sys.argv[1] + "\nSpeicherbelegung nach Anzahl der Wiederholungen")
plt.xlabel("Anzahl der Wiederholungen")
plt.ylabel("Speicherbelegung in Bytes")

plt.subplots_adjust(left=0.15)

plt.legend((liste, array), ("Liste", "Array"))

plt.show()
