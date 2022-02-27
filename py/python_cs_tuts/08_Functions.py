print("# Functions")

print("# Functions - def ...()")

def hello_func():
    pass

print("# Functions - `pass`-keyword")

def hello_func_2():
    pass

# print(hello_func_2) # Dit geeft de foutmelding: <function hello_func_2 at 0x7f449be501e0>

def hello_func_3():
    print("Hello function") 
 
hello_func_3()

print("\"Keeping your code dry\" means: Don't repeat yourself!")

print("# Functions - `return` keyword")

def hello_func_4():
    return "Hello from the function!"

bla = hello_func_4()
print(bla)

print(hello_func_4())

print(len(hello_func_4()))

print("## Functions - Een voordeel van de `return` keyword...")
print(hello_func_4().upper())

print("## Function - Arguments doorgeven aan de funtie.")

def hello(greeting):
    return "{} my dear friend, from the Function".format(greeting)

bla = hello('heya')
print(bla)

blatoo  = hello('Ajo')
print(blatoo)

print("## Function - met een default Argument.")

def hello2(greeting="Koekkoek!"):
    return "{} my dear friend, from the Function".format(greeting)

bla = hello2()
print(bla)

def hello3(greeting, name='You'):
    return("{}, vandaag, mijn lieve {}".format(greeting, name))

bla = hello3('hoooi', 'Eric')
print(bla)

bla = hello3('hooooooooooi')
print(bla)


print("## Function - *args en **kwargs")

tekst = """
De ARG zijn de ArgumentS, de KWargs zijn de Key Word ARGumentS, je hoeft deze conventie niet te gebruiken, door de sterren weet Python welke de args en kwargs zijn.
"""
print(tekst)

print("Als je niet weet hoeveel waardes je binnen krijgt. De kwargs zijn de Keyword Args, oftewel de Dictionary")
print("De args komen in een Tuple, en de kwargs komen in een Dictionary")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Science', name='John', lastname='Doe')

courses = ['Math', 'Biologie', 'English']
info = {'name': 'John', 'age': 22}

print("Dit gaat niet goed")
student_info(courses, info) # Dit gaat niet werken...

print("Gebruik args met * en kwargs met ** ervoor")

student_info(*courses, **info)




















