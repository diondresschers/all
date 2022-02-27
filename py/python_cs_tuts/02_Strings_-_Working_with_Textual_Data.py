print("Hello")

message = "Hello World"

print(message)

blabla = """
Dit is best wel lang.
Ja dat is echt zo.
En nog een lijn
"""

print(blabla)

print(message)

# De totale lengte (is 11)
print(len(message))

print("eerste karakter: ")

# Het eerste karater
print(message[0])

# Het laatste karakter (dus niet 11, want we beginnen bij 0)
print(message[10])

# Ook het laatste karakter
print(message[-1])

# Ook het laatste karater
lengte = len(message)
print(message[lengte-1])

# Print van karater 0 tot karater 7. Het laatste karakter 7 (de `o` wordt niet meegenomen).
print(message[0:7])

# Print vanaf 2 tot karakter 5, Dit heet 'slicing'
print(message[2:5])

# Print vanaf 0 tot 4
print(message[:4])

# Print vanaf 4 tot en met eind
print(message[7:])

# Je kan de method (de OOP functie), lower() gebruiken
print(message.lower())

# Maak gebruik van je (Integrated Development Environment) IDE, om alle methods te zien. 
print(message.upper())

# Tel hoe vaak de de tekst  `Hello` in de hele string `Hello World` voorkomt.
print(message.count('Hello'))
print(message.count('l'))

# Return een nieuwe sting, maar vervang het de initiele waarde niet. De method replace(), doet de vervanging niet 'in place' maar retourneert alleen de waarde.
print(message.replace('World', 'Universe'))
nieuwe_tekst = message.replace('World', 'Universe')
print(nieuwe_tekst)
print(message)

# Dit kan echter ook
message = message.replace('World', 'Universe')
print(message)

# Concatenate
greeting = 'Hello'
name = 'Dion'
new_message = greeting + name
print(new_message)
new_message  = greeting + ", " + name + ", Welcome!"
print(new_message)

# Er is ook een formattted-string
new_message = "{}, {}, Welcome!".format(greeting, name)
print(new_message)

# Vanaf Python 3.6 zijn er ook f-strings
new_message = f'{greeting}, {name}, Welcome!'
print(new_message)

# Je kan ook nog coden binnen een f-string:
new_message = f'{greeting.upper()}, {name[1:]}, Welcome!'
print(new_message)

# De dir() functie. Deze geeft alle methods and properties!?
print(dir(name))

print(type(name))
# De help() function
print(help(str))

print(help(str.lower))