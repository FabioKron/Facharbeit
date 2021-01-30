import matplotlib.pyplot as plt
import sys

# Einlesen der Datei
with open(str(sys.argv[1]), "r") as file:
    file_data = file.read()

# Umwandeln der Daten zu Liste
file_data = file_data.split("\n")
file_data = [row.split(",") for row in file_data if row]

