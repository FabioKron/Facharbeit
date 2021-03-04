import anhaengen_float

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
