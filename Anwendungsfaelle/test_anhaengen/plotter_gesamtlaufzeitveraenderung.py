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
gesamtlaufzeitveraenderung_liste: list = [float(zeile[7]) for zeile in dateiinhalt[1:]]
gesamtlaufzeitveraenderung_array: list = [float(zeile[8]) for zeile in dateiinhalt[1:]]

# Grafische Darstellung der Listen
liste, = plt.plot(wiederholung, gesamtlaufzeitveraenderung_liste, label="Liste")
array, = plt.plot(wiederholung, gesamtlaufzeitveraenderung_array, label="Array")

plt.margins(0)

plt.title(sys.argv[1] + "\nGesamtlaufzeitveränderung nach Anzahl der Ausführungen")
plt.xlabel("Anzahl der Ausführungen")
plt.ylabel("Gesamtlaufzeitveränderung in Sekunden pro Ausführung")

plt.subplots_adjust(left=0.15)

plt.legend((liste, array), ("Liste", "Array"))

plt.show()
