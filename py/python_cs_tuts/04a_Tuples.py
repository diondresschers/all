print("# Tuples ()")

print("Tuples lijken op Lists, alleen kunnen ze NIET aangepast worden")

print("Lists zijn `mutable`")

print("Tuples zijn `immutable`")

gewone_list = [
    'History',
    'Math',
    'Physics',
    'CompSci',s
]

list_2  = gewone_list

print(gewone_list)
print(list_2)

print("#Tuples, nu laten we het verschil zien tussen `mutable` en `immutable`")

gewone_list[0] = 'Art'

print(gewone_list)

print(list_2)

print("Door het aanpassen van `gewone_list` hebben we niet alleen de `gewone_list` aangepast, maar ook de `list_2`")

print("Als je niet wilt dat je lijst gewijzigd wordt, gebruik dan een Tuple")

print("# Tuples, nu laten we het verschil zien tussen `mutable` en `immutable`")

gewone_tuple = [
    'History',
    'Math',
    'Physics',
    'CompSci',
]

tuple_2  = gewone_tuple

print(gewone_tuple)
print(tuple_2)

print("Dit gaat gewoon niet werken...")
gewone_tuple[0] = 'Art'

print(gewone_tuple)

print(tuple_2)