import random

dziala = True
niedzala = False

i = random.randint(1, 9)
while dziala:
    answer = raw_input("Sprobuj zgadnac! ")
    if int(answer) == i:
        print "Zgadles!"
        dziala = True
        break
    elif int(answer) > i:
        print "Niestety to bylo zbyt duzo:"
        print "Sprobuj ponownie!"
        niedziala = False
    elif int(answer) < i:
        print "Niestety to bylo zbyt malo:"
        print "Sprobuj ponownie!"
        niedziala = False