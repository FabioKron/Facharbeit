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
runtime_list = [float(row[3]) for row in file_data[1:]]
runtime_array = [float(row[4]) for row in file_data[1:]]

# Grafische Darstellung der Listen
liste, = plt.plot(iterations, runtime_list)
array, = plt.plot(iterations, runtime_array)

plt.margins(0)

plt.title("Laufzeit nach Anzahl der Ausführungen")
plt.xlabel("Anzahl der Ausführungen")
plt.ylabel("Laufzeit in Sekunden")

plt.subplots_adjust(left=0.15)


plt.legend((liste, array), ("Liste", "Array"))

plt.show()