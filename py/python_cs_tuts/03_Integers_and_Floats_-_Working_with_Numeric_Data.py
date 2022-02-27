num = 3

# type() function
print(type(num))

num = 3.14
print(type(num))

info = """
optellen:                               3 + 2           = 5
aftrekken:                              3 - 2           = 5
vermemingvuldigen:                      3 * 2           = 5
delen:                                  3 / 2           = 1.5
delen, geeft alleen het basisgetal:     3 // 2          = 1     # zo deelt python2 standaard
machtsverheffen:                        3 ** 2          = 9
modulus:                                3 % 2           = 1     # Dit geeft `1`, want 3 delen door 2 is 1, met een rest van 1.    
"""

print(info)

print(3/2)
print(3%2)

#Met de modulus kan je makkelijk checken of een getal even of oneven is.
# Dit resulteert in 1, want 7/2 = 3 met een rest van 1
print(7%2)
# Dit resulteert in 1, want 6/2 = 3 met een rest van 0
print(6%2)

# De volgorde van operations: HMVDWOA
# De volgorde van operations: PEMDAS: Please Excuse My Dear Aunt Sally -> Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction.

print(3 * 2 + 1)
print(3 * (2 + 1))
print(3 + 2 * 1)

num = 5
num = num + 5
print(num)
# Dit is de shorthand voor: num = num + 1
num += 4
print(num)

# Dit is de shorthand voor: num = num * 5

num *= 3
print(num)

# abs() de abs-functie geeft de positieve waarde
print(abs(-7))

# round() deze rondt het getal
print(round(3.12345671))

# round(), het tweede optionele argument rond af met het aantal gegeven plaatsen achter de komma.
print(round(3.12345671, 3))
print(round(3.12345671, 5))

comparison = """
equal:                  3 == 2
not equal:              3 != 2
greater than:           3 > 2
less than:              3 < 2
greater or equal:       3 >= 3
less or equal:          3 <= 2
"""

print(comparison)

print(3 > 2)

# Er kunnen voorbeelden zijn waar het een getal is, maar het eigenlijk niet is. Dit kan bijvoorbeeld bij het inlezen zijn van een file.

num_1 = '100'
num_2 = '200'

print(num_1 + num_2)

# Dit kunnen we oplossen met 'casting'
num_1 = int(num_1)
num_2 = int(num_2)


print(num_1 + num_2)