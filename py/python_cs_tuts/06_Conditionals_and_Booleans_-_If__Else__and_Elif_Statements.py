print("# Conditionals and Booleans - If, Else, Elif Statements")

print("# if ... :")

if True:
    print("Conditional is True")

if False:
    print("Dit is echt bullshit!")

taal = 'Python'

if taal == 'Python':
    print("Jaa, gebruikt {} !!!".format(taal))

comparison = """
Conditionals: 

equal:                  3 == 2
not equal:              3 != 2
greater than:           3 > 2
less than:              3 < 2
greater or equal:       3 >= 3
less or equal:          3 <= 2
Object Identity:        is      # Checkt of het het zelfde ID heeft, oftewel of het hetzelfde object in het geheugen is.
"""

print(comparison)

print("# if ...: else:")

taal = 'Python'

if taal == 'Python':
    print("Jaa, gebruikt {} !!!".format(taal))
else:
    print("Sjit, je gebruikt {} ...".format(taal))

taal = 'JavaScript'

print("# if ...: elif ...: else:")

if taal == 'Python':
    print("Jaa, gebruikt {} !!!".format(taal))
elif taal == 'JavaScript':
    print("Okay, niet heel verkeerd, je gebruikt {}".format(taal))
else:
    print("Sjit, je gebruikt {} ...".format(taal))

print("Je kan zoveel `elif` ertussen zetten, dus het is een soort 'switch'-statement uit andere talen.")

taal = "AmigaBASIC"

if taal == 'Python':
    print("Jaa, gebruikt {} !!!".format(taal))
elif taal == 'JavaScript':
    print("Okay, niet heel verkeerd, je gebruikt {}".format(taal))
elif taal == 'AmigaBASIC':
    print("You oldskooler! You use {} !!! :)".format(taal))
elif taal == 'Commodore Basic':
    print("Yeah, Biatch! Je gebruikt {}".format(taal))
else:
    print("Sjit, je gebruikt {} ...".format(taal))

print("# Boolean operators")

booleans = """
and
or
not
"""

print(booleans)

print("# if ... and ...:")

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Admin page!")
else:
    print("Bad credentials...")

print("# if ... or ...:")

user = 'Admin'
logged_in = True

if user == 'Dion' or user == 'Admin':
    print("You are the boss...")
else:
    print("You are nozzing!")

print("# if not ...:")

name = 'Dion'

if not name == 'Dion':
    print("What a shitty name")
else:
    print("Way to go, handesome!")

print("# The 'is' Object Identity / Zelfde in memory")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

print(a is b) # Het zijn twee verschillende objecten in het geheugen

print("# id() functie om het geheugenadres te zien")

print(id(a))
print(id(b))

c = [4, 5, 6]
d = c
print(id(c))
print(id(d))

print(c == d)
print(c is d)

print("Evaluaties...")

condition = False      # -> False
condition = None       # -> False
condition = 0          # -> False
condition = 10         # -> True
condition = ''         # -> False
condidion = []         # -> False
condition = ()         # -> False
condition = {}         # -> False

print("if ... is True: = if ...:")
if condition is True:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("Als het niet 'False' is, dan is automatisch True")







