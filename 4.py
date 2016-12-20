rz = raw_input("kto? ")
rz2 = raw_input("z kim? ")
cz = raw_input("co robili? ")
prz = raw_input("jak? ")
x = raw_input("co z tego wyniklo? ")


def historyjka():
    return "{} {} {} {} i wynikla z tego {}".format(rz, rz2, cz, prz, x)


print historyjka()