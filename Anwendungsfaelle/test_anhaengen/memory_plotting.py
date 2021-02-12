import matplotlib.pyplot as plt
import sys

# Einlesen der Datei
with open(str(sys.argv[1]), "r") as file:
    file_data = file.read()

# Umwandeln der Daten zu Liste
file_data = file_data.split("\n")
file_data = [row.split(",") for row in file_data if row]

# Sortieren der Daten in seperate Listen
iterations = [int(row[0]) for row in file_data[1:]]
memory_list = [int(row[1]) for row in file_data[1:]]
memory_array = [int(row[2]) for row in file_data[1:]]

# Grafische Darstellung der Listen
liste, = plt.plot(iterations, memory_list, label="Liste")
array, = plt.plot(iterations, memory_array, label="Array")

plt.margins(0)

plt.title(sys.argv[1] + "\nSpeicherbelegung nach Anzahl der Ausführungen")
plt.xlabel("Anzahl der Ausführungen")
plt.ylabel("Speicherbelegung in Bytes")

plt.subplots_adjust(left=0.15)

plt.legend((liste, array), ("Liste", "Array"))

plt.show()
