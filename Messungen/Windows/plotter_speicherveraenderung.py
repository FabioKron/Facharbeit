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
speicherveraenderung_liste: list = [float(zeile[3]) for zeile in dateiinhalt[1:]]
speicherveraenderung_array: list = [float(zeile[4]) for zeile in dateiinhalt[1:]]

# Grafische Darstellung der Listen
liste, = plt.plot(wiederholung, speicherveraenderung_liste, label="Liste")
array, = plt.plot(wiederholung, speicherveraenderung_array, label="Array")

plt.margins(0)

plt.title(sys.argv[1] + "\nSpeicherveränderung je hinzugefügtes Element")
plt.xlabel("Hinzugefügtes Element")
plt.ylabel("Speicherveränderung in Bytes")

plt.subplots_adjust(left=0.15)

plt.legend((liste, array), ("Liste", "Array"))

plt.show()
