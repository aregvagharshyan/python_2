#
a, b = 5, 10
a, b = b, a
print(a, b)
#
def get_coordinates():
    return 40.7128, -74.0060

lat, lon = get_coordinates()
print(lat, lon)
#
t = (1, 2, 3, 4, 5)
a, _, c, _, e = t
print(a, c, e)
#
first, *middle, last = (10, 20, 30, 40, 50)
print(first)
print(middle)
print(last)
#
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, char in pairs:
    print(num, char)
#
words = ['hello', 'world']
for index, word in enumerate(words):
    print(index, word)
#
def add(a, b, c):
    return a + b + c

nums = (1, 2, 3)
print(add(*nums))
#
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

person = {'name': 'Alice', 'age': 25}
greet(**person)
#
data = ('John', ('Python', 'JavaScript'))
name, (lang1, lang2) = data
print(name)
print(lang1)
print(lang2)
#
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
