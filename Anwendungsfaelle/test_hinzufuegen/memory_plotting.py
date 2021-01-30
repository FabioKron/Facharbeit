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
plt.plot(iterations, memory_list)
plt.plot(iterations, memory_array)

plt.show()