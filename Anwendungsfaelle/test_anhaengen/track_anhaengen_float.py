import anhaengen_float


def add_average_file():
    global iterations, numOfTestFiles, filenames
    print("calculating average...")

    index_of_list_memory = 1
    index_of_array_memory = 2
    index_of_list_time = 3
    index_of_array_time = 4

    # Erstellen der Datei, um den Durchschnitt zu speichern
    average_file = filenames + "_average.csv"
    open(average_file, "x").close()

    with open(average_file, "a") as file:
        file.write(",".join(
            ["iterations", "memory list", "memory array", "execution time list", "execution time array"]
        ) + "\n")

    # Berechnen des Durchschnitts jeder Zeile und anhängen an average_file
    line = 0
    while line < iterations:
        line += 1
        current_file_index = 0
        sum_of_list_memory = 0
        sum_of_array_memory = 0
        sum_of_list_time = 0
        sum_of_array_time = 0
        while current_file_index < numOfTestFiles:
            current_file_index += 1
            with open(filenames + str(current_file_index) + ".csv", "r") as current_file:
                current_file_and_line = current_file.readlines()[line]
                data_of_line = [float(e) for e in current_file_and_line.split(",")]
                sum_of_list_memory += data_of_line[index_of_list_memory]
                sum_of_array_memory += data_of_line[index_of_array_memory]
                sum_of_list_time += data_of_line[index_of_list_time]
                sum_of_array_time += data_of_line[index_of_array_time]

        average_list_memory = sum_of_list_memory / numOfTestFiles
        average_array_memory = sum_of_array_memory / numOfTestFiles
        average_list_time = sum_of_list_time / numOfTestFiles
        average_array_time = sum_of_array_time / numOfTestFiles

        with open(average_file, "a") as file:
            file.write(",".join(
                [str(line), str(average_list_memory), str(average_array_memory), str(average_list_time),
                 str(average_array_time)]
            ) + "\n")
    print("calculation of average finished...")


iterations = int(input("Iterations for each run: "))
numOfTestFiles = int(input("Number of test runs: "))
filenames = input("Filename without type-end to save data: ")

# Generieren der Testergebnisse
current_run = 0
while current_run < numOfTestFiles:
    current_run += 1
    print("starting run", current_run, "...")
    anhaengen_float.gen_test_data(filenames + str(current_run) + ".csv", iterations)
    print("finished run", current_run, "...")

add_average_file()
