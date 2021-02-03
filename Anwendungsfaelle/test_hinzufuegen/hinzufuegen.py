import time
import numpy
import random
import sys


if __name__ == '__main__':

    #Erstellen der Datei
    args = sys.argv
    filename = sys.argv[1]
    open(filename, "x").close()

    with open(filename, "a") as file:
        file.write(",".join(["Anzahl Elemente", "Speicher Liste", "Speicher Array", "Laufzeit Liste","Laufzeit Array"])+"\n")

    # Erstellen der Liste und des Arrays
    liste = []
    array = numpy.array([], dtype=float)

    # Initalisieren der Variablen, die die Zeit speichern
    array_time = 0
    list_time = 0

    # Festlegen der Anzahl der Durchläufe
    if len(sys.argv) > 2:
        iterations = sys.argv[2]
    else:
        iterations = 10000

    # Zählvariable, wird benötigt um alle Elemente zu speichern
    i = 0

    while i < iterations:
        zahl = random.random()

        start_of_next_array_timeframe = time.time()
        array = numpy.append(array, zahl)
        array_time += time.time() - start_of_next_array_timeframe

        start_of_next_list_timeframe = time.time()
        liste.append(zahl)
        list_time += time.time() - start_of_next_list_timeframe

        i += 1

        # Speichern der Messwerte in der Datei
        with open(filename, "a") as file:
            file.write(",".join([str(i), str(sys.getsizeof(liste)), str(sys.getsizeof(array)), str(list_time), str(array_time)])+"\n")
            print("Status für", i, " Elemente gespeichert.")

