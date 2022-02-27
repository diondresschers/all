print("# Sets {}")

print("Sets zijn items die geen volgorde hebben en waar geen dubbele items in voor komen.")

cs_courses = {
    'History',
    'Math',
    'Physics',
    'CompSci',
}

print(cs_courses)

print("De volgorde kan anders zijn dan je ingegeven hebt, omdat Sets niks geven om de volgorder")

cs_courses = {
    'History',
    'Math',
    'Physics',
    'CompSci',
    'Math',
    'Math',
    'Physics',
    'Cooking',
}

print(cs_courses)

print("Sets zijn ideaal om dubbelen weg te gooie en voor een zogenaamde `membership test`")


print("Sets doen dit efficienter dan Lists en Tuples, omdat deze het sneller doet.")

print('Math' in cs_courses)

print("## Sets - .intersection() ")
print("Sets kunnen ook snel de overeenkomsten en verschillen met anderen weergegeven.")

cs_courses = {
    'History',
    'Math',
    'Physics',
    'CompSci',
}

art_courses = {
    'History',
    'Painting',
    'English',
    'CompSci',
}

# Geef nu de overeenkomsten weer
print(cs_courses.intersection(art_courses))

print("## Sets - .difference() ")

print("Dit zijn nu de Items die wel in `cs_courses` zitten, maar niet in `art_courses`")
print(cs_courses.difference(art_courses))


print("## Sets - .union() ")
print("Geef nu alle unieke Items weer van beide Sets")

print(cs_courses.union(art_courses))

print("## Maak lege Lists, Tuples en Sets")

tekst = """
Lege Lists:
empty_list = []
empty_list = list()

Lege Tuples:
empty_tuple = ()
empty_tuple = tuple()

Lege Sets:
emtpy_set = {} # Dit gaat NIET werken, want dit creeert een lege Dictionary.
empty_set = set() # Dit werkt wel..
"""

print(tekst)



