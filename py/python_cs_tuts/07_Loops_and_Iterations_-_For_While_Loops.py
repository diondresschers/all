print("# Loops")


print("## Loops - for ... in ...:")
numbers = [1, 2, 3, 4, 5, ]

for number in numbers:
    print(number)

print("## Loops - break")

for number in numbers:
    if number == 3:
        print("We hebben hem ({}) gevonden!, en nu gaan we een `break` uitvoeren :)".format(number))
        break
    print(number)

print("## Loops - break")


for number in numbers:
    if number == 3:
        print("We hebben hem ({}) gevonden!, en nu gaan we een `continue` doorvoeren :)".format(number))
        continue
    print(number)

print("## Loops - nested loops")
for number in numbers:
    for letter in 'abc':
        print(number, letter)

print("## Loops - for ... in range(...):")

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(100, 200, 5):
    print(i)

print("## Loops - while ...:")

x = 0

while x < 10:
    print(x)
    x += 1

x = 0

print("## Loops - while loop met break")

while x < 10:
    if x == 5:
        print("Got em: {}".format(x))
        break
    print(x)
    x += 1

print("## Loops - while True: 'oneindige' loop")


x = 0

while True:
    if x == 6:
        print("Got em: {}".format(x))
        break
    print(x)
    x += 1

print("in een echt oneindige loop kan je uitlomen met [CTRL]+[C]")




















