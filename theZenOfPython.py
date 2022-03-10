from time import sleep

#file openen
file = open("README.md", "r")

# regel voor regel printen wat in het bestand stat
line = True
while line:
    line = file.readline().removesuffix("\n") # haalt enter aan einde weg
    if line != "": # zodat er geen lege regel word geprint
        print(line)
        sleep(1)
input()