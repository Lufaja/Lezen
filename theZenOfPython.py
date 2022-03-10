from time import sleep

#file openen
with open("README.md", "r") as file:
# regel voor regel printen wat in het bestand staat
    for line in file:
        print(line.removesuffix("\n"))# haalt enter aan einde weg
        sleep(1)

input()