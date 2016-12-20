import random

working = True
while working :
    answer = raw_input("Again? ")
    if answer == 'no':
        working = False
    elif answer == 'yes':
        print "turlam... "
        print random.randint(1, 6)
        working = True

