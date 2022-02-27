print("# Lists []")

courses = [
    "History",
    "Math",
    "Fysics",
    "CompSci",
]

print(courses)

# print(help(courses))

print(len(courses))

# shows first item in the list
print(courses[0])

# Print de laatste list in de lijst
print(courses[-1])

# Print de laatste item:
laatste_item = len(courses) - 1
print(courses[laatste_item])

# Geef een range aan van 0 tot 2
print(courses[0:2])

print(courses[:2])

print(courses[2:3])

print(courses[2:])

print("## Lists - methods()")

print("## Lists - methods() - .append()")
# Voeg het item 'Art' toe aan het einde.
courses.append('Art')

print(courses)


# Voeg een item toe op een specifieke locatie, het voegt alleen toe, het vervangt niks

print("## Lists - methods() - .inserts()")
courses.insert(0, 'Biologie')

print("## Lists - methods() - .extend()")

print(courses)

courses_2 = ['Cooking','English']

# This will insert the List in a List (a nested list) at position 2.
courses.insert(0,courses_2)

print(courses)

# Als je nu het eerste item van de List wilt printen, dan print hij de hele List bij positie 1

# Je kan extend() gebruiken als je een List wilt toevoegen aan een List, zonder dat deze genest gaan worden.

courses = [
    "History",
    "Math",
    "Fysics",
    "CompSci",
]

print(courses)

print(courses_2)

courses.extend(courses_2)

print(courses)

print("## Lists - methods() - .remove()")

courses.remove('Math')

print(courses)

print("## Lists - methods() - .pop()")

# Haal de laatste weg en returneer de waarde

verwijderde_waarde = courses.pop()

print(verwijderde_waarde)

# Deze is dus zonder de `verwijderde_waarde`
print(courses)

print("## Lists - methods() - .reverse()")

courses.reverse()
print(courses)

print("## Lists - methods() - .sort()")

print("De sorted function past meteen de List aan")
# We flippen ze weer, zodat we daarna weer kunnen sorteren
courses.reverse()
print(courses)

courses.sort()
print(courses) 

nummertjes = [
    6,
    8,
    2,
    235,
    -2,
    3.2,
    -500,
    3
]

print(nummertjes)

nummertjes.sort()

print(nummertjes)

nummertjes.sort(reverse=True)

print(nummertjes)

print("## sorted()")

nummertjes_2 = [4,6,2,4,7,2,2,6,7,-2,35,-355]

print(sorted(nummertjes_2))
print(nummertjes_2)

print("## min()")

print(min(nummertjes))

print("## min()")

print(max(nummertjes))

print("## sum()")

print(sum(nummertjes))

print("## Lists - methods() - .index()")

# Je kan de index vinden van een List item

print(courses.extend(courses_2))

print(courses)

print(courses.index('Fysics'))

# print(courses.index('Physics')) # Dit resulteert in een Error.

print("# Check if een item voorkomt in een List, resultaat is `True` of `False`")

print('Art' in courses)

print('Fysics' in courses)

print('Physics' in courses)

print("# Loop door Lists")

for blabla in courses: 
    print(blabla)

# Het maakt niks uit hoe je het eerste keywoord gebruikt, maar verstanding is om het enkele item bijvoorbeeld `course` te noemen en de List in meervoud te noemen dus bijvoorbeeld `courses`

print("## enumerate()")

# Enumerate geeft niet alleen de waarde terug, maar ook de index
for course in enumerate(courses):
    print(course)
    print("Alleen de index: " + str(course[0]))
    print("Alleen de waarde: {}".format(course[1]))

for course in enumerate(courses, start=2):
    print(course)

print("## join()")

# Je kan van een List een string maken, je kan ook de scheiding/separator doorgeven
print(courses)

courses_string = ', '.join(courses)

print(courses_string)

courses_string = ' <-> '.join(courses)

print(courses_string)

print("## split() ")

#Split is het tegenovergestelde van join() en maakt van een string een List op basis van het scheidingsteken

print(courses_string)

new_list_with_courses = courses_string.split(" <-> ")
print(new_list_with_courses)

for course in new_list_with_courses:
    print(course)




