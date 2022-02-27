print("# Dictionary ")
student = {
    'name': 'John',
    'age': 25,
    'courses': [
        'Math',
        'CompSci'
    ]
}

print(student)


print("# Dictionary via index")

# print(student[0]) # Dit geeft een error
print(student['name'])

print("# Dictionary - .get() ")

print("Als er geen index is, wordt er een fout gegenereerd, dit is te voorkomen met de .get() method")

print(student.get('name'))
print(student.get('baloney')) # Dit resulteert niet in een foutmelding, maar in 'None'.

print(student.get('baloney_too',"Deze bestaat helaas niet lieverd"))

print("# Dictionary - Item toevoegen")

student['phone'] = '555-1234567890'

print(student.get('phone'))

print("Je kan ook velden updaten..")

student['age'] = 80
print(student.get('age'))
print(student)

print("# Dictionary - .update()")

print("De .update() method is handig als je meerdere Items in een keer wilt updaten, waarbij de dictionary een dictionary als een argument neemt")

student.update({
    'name': 'Trella',
    'age': 40,
    'courses': [
        'Programmere',
        'Tekenles'
    ],
    'phone': "035 7 11 9 11",
})

print(student)

print("# Dictionary - del")

del student['phone']
print(student)

naampje = student.pop('name')
print(student)
print(naampje)

print("## Dictionay - len()")

student.update({
    'name': 'Trella',
    'age': 40,
    'courses': [
        'Programmere',
        'Tekenles'
    ],
    'phone': "035 7 11 9 11",
})

print(len(student))

print("## Dictionary - .keys() method")

print("Onderstaande geeft alle keys weer")

print(student.keys())

print("## Dictionary - .values() method")


print("Onderstaande geeft alle values weer")
print(student.values())


print("## Dictionary - .iets() method")

print("Onderstaande geeft alle Keys en Values weer in pairs")

print(student.items())

print("# Dictionary - loopen door een Dictionary")

print("Onderstaande geeft alleen de keys weer")
for bla in student:
    print(bla)

print("Dit is de juiste manier, deze geeft de paartjes weer ")
for bla in student.items():
    print(bla)

print("Dit is de Key plus Value")
for bla, ja in student.items():
    print(bla + " -> " + str(ja))