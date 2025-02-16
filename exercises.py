numbers = (10, 20, 30, 40, 50, 20, 10)
print(numbers.count(20))
print(numbers.index(40))
result = list(numbers)
result.append(60)
result_tuple = tuple(result)
print(result_tuple)
reversed_tuple = result_tuple[::-1]
print(reversed_tuple)
#
person = ("Alice", 25, "Engineer", "New York")
x, y, z, a = person
print(x, y, z, a)
c, d, *others = person
print(c, d, *others)
#
a = 5
b = 10
a, b = b, a
print(a, b)
#
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
zipped = list(zip(names, ages))
print(zipped)
#
colors = ("red", "green", "blue", "yellow")
colors_index = enumerate(colors, start = 1)
for index, color in colors_index:
    print(f'{index}: {color}')
#
