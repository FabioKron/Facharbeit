import time
import numpy
import random
import sys


def gen_test_data(filename, iterations=10000):
    # Erstellen der Datei
    open(filename, "x").close()

    with open(filename, "a") as file:
        file.write(",".join(
            ["iterations", "memory list", "memory array", "execution time list", "execution time array"]
        ) + "\n")

    # Erstellen der Liste und des Arrays
    list_to_track = []
    array_to_track = numpy.arange(0)

    # Initalisieren der Variablen, die die Zeit speichern
    array_time = 0
    list_time = 0

    # Zählvariable, wird benötigt um alle Elemente zu speichern
    i = 0

    while i < iterations:
        i += 1

        # Vorbereitung der Aktion des Durchlaufs
        random_number = random.random()

        # Aktion beim Array
        start_of_next_array_timeframe = time.time()
        array_to_track = numpy.append(array_to_track, random_number)
        array_time += time.time() - start_of_next_array_timeframe

        # Aktion bei der Liste
        start_of_next_list_timeframe = time.time()
        list_to_track.append(random_number)
        list_time += time.time() - start_of_next_list_timeframe

        # Speichern der Messwerte in der Datei
        with open(filename, "a") as file:
            file.write(",".join(
                [str(i), str(sys.getsizeof(list_to_track)), str(sys.getsizeof(array_to_track)), str(list_time),
                 str(array_time)]) + "\n")

        # Ausgeben einer Statusmeldung
        if not i % 1000:
            print("Status saved for", i, " iteration")
