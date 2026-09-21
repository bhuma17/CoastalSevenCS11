

#Loops

age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

for number in range(1, 6):
    print(number)

count = 1

while count <= 5:
    print(count)
    count += 1

for number in range(1, 11):

    if number == 5:
        break

    print(number)

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

for number in range(5):

    if number == 2:
        pass

    print(number)

numbers = range(1, 10, 2)

for number in numbers:
    print(number)

numbers = [number * 2 for number in range(1, 6)]

print(numbers)

#Functions

def greet():
    print("Hello!")


greet()

def greet(name):
    print("Hello!",name)


greet("Supriya")

def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Ravi")

def add(a, b):
    result = a + b
    return result


answer = add(10, 20)

print(answer)

def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


x, y = calculate(10, 5)

print("Addition:", x)
print("Subtraction:", y)

# Args

def add_numbers(*args):

    total = 0

    for number in args:
        total += number

    return total


result = add_numbers(10, 20, 30, 40)

print(result)

#Kwargs

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(course="Python", day="18-Sep-2026")
print_info(name="Arjun", age=21, city="Delhi")

# Lambda

square = lambda x: x * x
add = lambda a, b: a + b

print("square(6):", square(6))
print("add(3,5):", add(3, 5))

#Local& Global

message = "Global"


def test():
    message = "Local"
    print("Inside function:", message)


test()

print("Outside function:", message)

#LEGB

name = "Global"


def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print(name)

    inner()


outer()

def fizzbuzz(n=30):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(30)

number = int(input("Enter a number: "))

if number <= 1:

    print("Not a prime number")

else:

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:

            is_prime = False
            break

    if is_prime:

        print("Prime number")

    else:

        print("Not a prime number")

def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


temperature = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(temperature)

print("Temperature in Fahrenheit:", result)

#List Curd

tasks = []

# ---------- CREATE ----------
def create_task(name):
    tasks.append(name)
    print(f"Created: {name}")

# ---------- READ ----------
def read_all_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")

def read_task(index):
    if 0 <= index < len(tasks):
        return tasks[index]
    return None

# ---------- UPDATE ----------
def update_task(index, new_name):
    if 0 <= index < len(tasks):
        old = tasks[index]
        tasks[index] = new_name
        print(f"Updated: '{old}' -> '{new_name}'")
    else:
        print("Invalid index.")

# ---------- DELETE ----------
def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid index.")


# ---------- DEMO ----------
create_task("Buy milk")
create_task("Call Sam")
create_task("Finish report")

print("\nAll tasks:")
read_all_tasks()

update_task(1, "Call Sam at 5 PM")

delete_task(0)

print("\nFinal tasks:")
read_all_tasks()

numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])

print("Last:", numbers[-1])

print("First three:", numbers[0:3])

print("Middle:", numbers[1:4])

print("Reverse:", numbers[::-1])

#Tuples

person = ("Supriya", 25, "Hyderabad")

print("Name:", person[0])

print("Age:", person[1])

print("City:", person[2])

print("Complete tuple:", person)

#Set

set_a = {1, 2, 3, 4}

set_b = {3, 4, 5, 6}


# UNION

print("Union:", set_a.union(set_b))


# INTERSECTION

print("Intersection:", set_a.intersection(set_b))


# DIFFERENCE

print("Difference:", set_a.difference(set_b))

#Dictionary

person = {
    "name": "Supriya",
    "age": 25,
    "city": "Hyderabad"
}


# ACCESS

print(person["name"])


# GET

print(person.get("age"))


# KEYS

print(person.keys())


# ITEMS

for key, value in person.items():
    print(key, bhu":", value)

squares = {
    number: number * number
    for number in range(1, 6)
}

print(squares)

students = [
    ["Ravi", 80],
    ["Priya", 90],
    ["Anil", 75]
]


print(students[1])

print(students[1][0])

print(students[2][1])



